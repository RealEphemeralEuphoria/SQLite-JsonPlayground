import sqlite3
import json

# File paths
json_file = "EmployeeData.json"
db_file = "EmployeeData.db"

# Load the JSON data from the file
with open(json_file, "r") as file:
    json_data = json.load(file)

# Convert the JSON data back to a string (to store in the database)
json_string = json.dumps(json_data)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the raw_json table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS raw_json (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT
)
""")

# Insert the JSON string into the table
cursor.execute("INSERT INTO raw_json (data) VALUES (?)", (json_string,))

# Commit the transaction and close the connection
conn.commit()
conn.close()

print(f"JSON data with {len(json_data)} employees has been pushed to the database.")
