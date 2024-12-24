import sqlite3
import random
import datetime

def create_and_populate_employees_db(db_name="Employees.db", num_records=50):
    """
    Creates a new SQLite database file (if not exists) called 'Employees.db',
    defines an 'employees' table, and populates it with random test data.

    :param db_name: Name of the SQLite database file (default "Employees.db")
    :param num_records: How many employee records to generate (default 50)
    """

    # 1. Connect to the new or existing database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # 2. Create the 'employees' table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            role TEXT NOT NULL,
            department TEXT NOT NULL,
            salary INTEGER NOT NULL,
            hire_date TEXT NOT NULL
        )
    """)

    # 3. Define some sample data to make the records interesting
    possible_first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi"]
    possible_last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Garcia", "Martinez", "Lee"]
    possible_roles = ["Engineer", "Manager", "Analyst", "Developer", "Intern", "QA Tester"]
    possible_departments = ["IT", "HR", "Finance", "Marketing", "Operations"]

    # Helper function: generate a random date in the last 10 years
    def random_hire_date():
        start_date = datetime.date.today().replace(year=datetime.date.today().year - 10)
        end_date = datetime.date.today()
        days_range = (end_date - start_date).days
        random_num_days = random.randint(0, days_range)
        hire_date = start_date + datetime.timedelta(days=random_num_days)
        return hire_date.strftime("%Y-%m-%d")

    # 4. Generate and insert data
    for _ in range(num_records):
        first_name = random.choice(possible_first_names)
        last_name = random.choice(possible_last_names)
        full_name = f"{first_name} {last_name}"

        role = random.choice(possible_roles)
        department = random.choice(possible_departments)
        salary = random.randint(40000, 120000)  # random salary range
        hire_date = random_hire_date()

        cursor.execute("""
            INSERT INTO employees (full_name, role, department, salary, hire_date)
            VALUES (?, ?, ?, ?, ?)
        """, (full_name, role, department, salary, hire_date))

    # 5. Commit changes and close
    conn.commit()
    conn.close()

    print(f"[INFO] Created '{db_name}' and inserted {num_records} employee records into the 'employees' table.")


if __name__ == "__main__":
    # Generate 50 rows by default
    create_and_populate_employees_db(db_name="Employees.db", num_records=50)
