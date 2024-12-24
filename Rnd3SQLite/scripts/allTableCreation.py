import sqlite3
import os

# Define database path
DB_PATH = os.path.join(os.path.dirname(__file__), "../db/employees.db")

def setup_database():
    """
    Creates the SQLite database and sets up the tables:
    - Dev (original data import or experimental transformations)
    - Staging (intermediate transformations and testing)
    - Production (final clean data)
    """
    # Connect to SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create Dev table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Dev (
            employeeId INTEGER PRIMARY KEY,
            fullName TEXT NOT NULL,
            role TEXT NOT NULL,
            department TEXT NOT NULL,
            salary INTEGER NOT NULL,
            hireDate TEXT NOT NULL,
            email TEXT,
            terminationDate TEXT
        );
    """)

    # Create Staging table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Staging (
            employeeId INTEGER PRIMARY KEY,
            fullName TEXT NOT NULL,
            roleTitle TEXT,
            departmentName TEXT,
            salary INTEGER NOT NULL,
            hireDate TEXT NOT NULL,
            email TEXT,
            terminationDate TEXT
        );
    """)

    # Create Production table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Production (
            employeeId INTEGER PRIMARY KEY,
            fullName TEXT NOT NULL,
            role TEXT NOT NULL,
            department TEXT NOT NULL,
            salary INTEGER NOT NULL,
            hireDate TEXT NOT NULL,
            email TEXT NOT NULL,
            terminationDate TEXT
        );
    """)

    conn.commit()
    conn.close()
    print("Database and tables (Dev, Staging, Production) created successfully.")

if __name__ == "__main__":
    # Ensure db/ folder exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    # Run the setup
    setup_database()
