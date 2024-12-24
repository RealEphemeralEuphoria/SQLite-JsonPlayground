import sqlite3
import os

def ensure_migrations_table(cursor):
    """
    Ensures the 'migrations' table exists in the database to track applied migrations.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE NOT NULL,
            applied_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

def get_applied_migrations(cursor):
    """
    Retrieves the list of filenames of migrations that have already been applied.
    """
    cursor.execute("SELECT filename FROM migrations")
    return {row[0] for row in cursor.fetchall()}

def mark_migration_as_applied(cursor, migration):
    """
    Marks a migration as applied by inserting its filename into the 'migrations' table.
    """
    cursor.execute("INSERT INTO migrations (filename) VALUES (?)", (migration,))

def check_table_exists(cursor, table_name):
    """
    Checks if a table exists in the database.
    """
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name=?
    """, (table_name,))
    return cursor.fetchone() is not None

def run_migrations(db_name, migrations_folder):
    """
    Applies all SQL migrations in the given folder to the specified database, skipping
    migrations that have already been applied or are irrelevant to the current schema.

    :param db_name: SQLite database file name (e.g., 'Employees.db')
    :param migrations_folder: Folder containing SQL migration files
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Ensure the 'migrations' table exists
    ensure_migrations_table(cursor)

    # Get the list of already applied migrations
    applied_migrations = get_applied_migrations(cursor)

    # Get all migration files in order
    migration_files = sorted(
        [f for f in os.listdir(migrations_folder) if f.endswith(".sql")]
    )

    for migration in migration_files:
        if migration in applied_migrations:
            print(f"[SKIP] Migration already applied: {migration}")
            continue

        migration_path = os.path.join(migrations_folder, migration)

        # Check if this migration targets a table that exists
        if "employees" in migration.lower():
            if not check_table_exists(cursor, "employees"):
                print(f"[SKIP] Table 'employees' does not exist. Skipping migration: {migration}")
                continue

        print(f"[INFO] Applying migration: {migration}")
        with open(migration_path, "r") as f:
            sql = f.read()
            cursor.executescript(sql)

        # Mark this migration as applied
        mark_migration_as_applied(cursor, migration)

    conn.commit()
    conn.close()
    print("[INFO] All migrations applied successfully.")

if __name__ == "__main__":
    # Define the database file and the full path to the migrations folder
    db_name = os.path.normpath(os.path.join(os.path.dirname(__file__), "../dbs/Employees.db"))
    migrations_folder = os.path.normpath(os.path.join(os.path.dirname(__file__), "../migrations"))

    # Run migrations
    run_migrations(db_name, migrations_folder)
