import sys
import os
import sqlite3

# Add the project root directory to the Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(PROJECT_ROOT)

from config import DB_PATH

def clone_data_from_dev_to_staging():
    """
    Clones data from the 'Dev' table to the 'Staging' table.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Clear the Staging table before cloning
        cursor.execute("DELETE FROM Staging;")
        conn.commit()

        # Copy data from Dev to Staging
        cursor.execute("""
            INSERT INTO Staging (employeeId, fullName, roleTitle, departmentName, salary, hireDate, email, terminationDate)
            SELECT 
                employeeId,
                fullName,
                role AS roleTitle,
                department AS departmentName,
                salary,
                hireDate,
                email,
                terminationDate
            FROM Dev;
        """)
        conn.commit()
        print("Data successfully cloned from Dev to Staging.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    clone_data_from_dev_to_staging()
