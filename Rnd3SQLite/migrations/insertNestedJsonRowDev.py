import sys
import os
import sqlite3
import json

# Add the project root directory to the Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(PROJECT_ROOT)

from config import DB_PATH

def insert_nested_json_row():
    """
    Inserts a single row with nested JSON data into the 'Dev' table.
    """
    # Define the nested JSON structure for the role and department
    nested_role = json.dumps({
        "title": "Senior Developer",
        "responsibilities": ["Develop", "Mentor", "Code Review"]
    })
    nested_department = json.dumps({
        "name": "Software Engineering",
        "location": "HQ"
    })

    # Define the row data
    new_employee_data = (
        None,  # Let SQLite auto-generate the employeeId
        "Jamie Doe",  # fullName
        nested_role,  # role (nested JSON)
        nested_department,  # department (nested JSON)
        125000,  # salary
        "2023-12-01",  # hireDate
        "jamie.doe@example.com",  # email
        None  # terminationDate
    )

    # Connect to the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Insert the new row into Dev
        cursor.execute("""
            INSERT INTO Dev (employeeId, fullName, role, department, salary, hireDate, email, terminationDate)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, new_employee_data)
        conn.commit()
        print("Nested JSON row successfully inserted into Dev.")
    except Exception as e:
        print(f"Error inserting nested JSON row: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    insert_nested_json_row()
