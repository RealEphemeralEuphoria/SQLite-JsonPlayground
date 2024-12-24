import sqlite3
import os
import shutil
import json
import random

def create_mixed_json_table(source_db, new_db):
    """
    Copies an existing SQLite database, then creates an 'employeesWithJSON' table
    that mirrors the original 'employees' table with a mix of clean and messy (JSON) data.

    :param source_db: Absolute path to the source database file.
    :param new_db: Absolute path to the new database file.
    """

    # Ensure the source database exists
    if not os.path.exists(source_db):
        print(f"[ERROR] Source database not found at {source_db}.")
        return

    # Copy the source database to the new location
    if os.path.exists(new_db):
        print(f"[INFO] Overwriting existing {new_db}.")
        os.remove(new_db)

    shutil.copy(source_db, new_db)
    print(f"[INFO] Copied {source_db} to {new_db}.")

    # Connect to the copied database
    conn = sqlite3.connect(new_db)
    cursor = conn.cursor()

    # Modify the 'employees' table to introduce JSON messiness
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    # Iterate through rows and introduce JSON data for some records
    for row in employees:
        employee_id, full_name, role, department, salary, hire_date, termination_date, email = row

        # Randomly decide to mess up data in 'role' or 'department'
        if random.random() > 0.7:  # ~30% chance
            if random.random() > 0.5:
                # Replace 'role' with nested JSON
                role = json.dumps({
                    "title": role,
                    "responsibilities": ["Plan", "Lead", "Report"] if "Manager" in role else ["Develop", "Test"]
                })
            else:
                # Replace 'department' with nested JSON
                department = json.dumps({
                    "name": department,
                    "location": random.choice(["HQ", "Remote", "Regional Office"])
                })

        # Update the row in the table
        cursor.execute("""
            UPDATE employees
            SET role = ?, department = ?
            WHERE employeeId = ?
        """, (role, department, employee_id))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"[INFO] Created {new_db} with mixed JSON and clean data.")

if __name__ == "__main__":
    # Get the current working directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Source database path (absolute)
    source_db_path = os.path.join(current_dir, "../dbs/Employees.db")
    source_db_path = os.path.normpath(source_db_path)

    # New database path (absolute)
    new_db_path = os.path.join(current_dir, "../dbs/Employees_JSON_Mixed.db")
    new_db_path = os.path.normpath(new_db_path)

    # Run the script to create the new mixed-data database
    create_mixed_json_table(source_db=source_db_path, new_db=new_db_path)
