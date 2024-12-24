import sys
import os
import sqlite3

# Add the project root directory to the Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(PROJECT_ROOT)

from config import DB_PATH

def clone_data_from_staging_to_production():
    """
    Clones data from the 'Staging' table to the 'Production' table.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Clear the Production table before cloning
        cursor.execute("DELETE FROM Production;")
        conn.commit()

        # Copy data from Staging to Production
        cursor.execute("""
            INSERT INTO Production (employeeId, fullName, role, department, salary, hireDate, email, terminationDate)
            SELECT 
                employeeId,
                fullName,
                roleTitle AS role,
                departmentName AS department,
                salary,
                hireDate,
                email,
                terminationDate
            FROM Staging;
        """)
        conn.commit()
        print("Data successfully cloned from Staging to Production.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    clone_data_from_staging_to_production()
