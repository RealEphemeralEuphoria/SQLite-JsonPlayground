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


def run_migrations(db_name, migrations_folder):
    """
    Applies all SQL migrations in the given folder to the specified database, skipping
    migrations that have already been applied.

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
    db_name = "Employees.db"

    # Use the parent directory of this script to construct the migrations path
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    migrations_folder = os.path.join(current_script_path, "../migrations")

    # Normalize the migrations folder path
    migrations_folder = os.path.normpath(migrations_folder)

    # Run migrations
    run_migrations(db_name, migrations_folder)
