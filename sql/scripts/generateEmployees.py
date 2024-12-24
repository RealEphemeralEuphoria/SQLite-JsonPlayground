import sqlite3
import random
import datetime

def createAndPopulateEmployeesDb(employeesDb="Employees.db", recordCount=50):
    """
    Creates a new SQLite database file (if it does not exist) called 'Employees.db'.
    Defines an 'employees' table, then inserts the specified number of random records.

    :param employeesDb: Name of the SQLite database file (default "Employees.db")
    :param recordCount: Number of employee records to generate (default 50)
    """

    # 1. Connect to the new or existing database
    conn = sqlite3.connect(employeesDb)
    cursor = conn.cursor()

    # 2. Create the 'employees' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employeeId  INTEGER PRIMARY KEY AUTOINCREMENT,
            fullName    TEXT NOT NULL,
            role        TEXT NOT NULL,
            department  TEXT NOT NULL,
            salary      INTEGER NOT NULL,
            hireDate    TEXT NOT NULL
        )
    """)

    # 3. Define some sample data for random generation
    possibleFirstNames = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi"]
    possibleLastNames = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Garcia", "Martinez", "Lee"]
    possibleRoles = ["Engineer", "Manager", "Analyst", "Developer", "Intern", "QATester"]
    possibleDepartments = ["IT", "HR", "Finance", "Marketing", "Operations"]

    def randomHireDate():
        """
        Generates a random hire date within the last 10 years.
        """
        today = datetime.date.today()
        startDate = today.replace(year=today.year - 10)  # 10 years ago
        endDate = today
        daysRange = (endDate - startDate).days
        randomNumDays = random.randint(0, daysRange)
        hireDate = startDate + datetime.timedelta(days=randomNumDays)
        return hireDate.strftime("%Y-%m-%d")

    # 4. Generate and insert data
    for _ in range(recordCount):
        firstName = random.choice(possibleFirstNames)
        lastName = random.choice(possibleLastNames)
        fullName = f"{firstName} {lastName}"

        role = random.choice(possibleRoles)
        department = random.choice(possibleDepartments)
        salary = random.randint(40000, 120000)  # random salary range
        hireDate = randomHireDate()

        cursor.execute("""
            INSERT INTO employees (fullName, role, department, salary, hireDate)
            VALUES (?, ?, ?, ?, ?)
        """, (fullName, role, department, salary, hireDate))

    # 5. Commit and close
    conn.commit()
    conn.close()

    print(f"[INFO] Created '{employeesDb}' and inserted {recordCount} employee records into the 'employees' table.")

if __name__ == "__main__":
    # Generate 50 rows by default
    createAndPopulateEmployeesDb(employeesDb="Employees.db", recordCount=50)
