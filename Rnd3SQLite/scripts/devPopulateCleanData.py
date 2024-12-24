import sqlite3
import os
import random
import datetime

# Path to the database
DB_PATH = os.path.join(os.path.dirname(__file__), "../db/employees.db")

def random_date(start_year=2015, end_year=2024):
    """
    Generates a random date between the given start and end years.
    """
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    days_range = (end_date - start_date).days
    if days_range <= 0:  # Handle cases where the range is invalid
        return start_date
    random_num_days = random.randint(0, days_range)
    return start_date + datetime.timedelta(days=random_num_days)

def populate_dev_table():
    """
    Populates the Dev table with 50 rows of clean, standardized data.
    """
    # Connect to the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Sample data
    first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Garcia", "Martinez", "Lee"]
    roles = ["Engineer", "Manager", "Analyst", "Developer", "Intern", "QA Tester"]
    departments = ["IT", "HR", "Finance", "Marketing", "Operations"]

    # Generate and insert 50 rows
    rows = []
    for i in range(50):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"
        role = random.choice(roles)
        department = random.choice(departments)
        salary = random.randint(40000, 120000)
        hire_date = random_date(start_year=2015, end_year=2024).strftime("%Y-%m-%d")
        termination_date = random.choice([None, random_date(start_year=2025).strftime("%Y-%m-%d")])
        email = f"{first_name.lower()}.{last_name.lower()}@securingbytes.com"

        rows.append((i + 1, full_name, role, department, salary, hire_date, email, termination_date))

    cursor.executemany("""
        INSERT INTO Dev (employeeId, fullName, role, department, salary, hireDate, email, terminationDate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, rows)

    conn.commit()
    conn.close()

    print("Dev table populated with 50 rows of clean data.")

if __name__ == "__main__":
    populate_dev_table()
