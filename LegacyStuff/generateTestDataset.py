import json

# Generate 369 employee objects
employees = [
    {
        "id": i,
        "name": f"Employee {i}" if i != 369 else "FoxxiKurama",  # Special name for Employee 369
        "role": ["Developer", "Designer", "Manager", "QA Engineer", "DevOps"][i % 5],
        "salary": 60000 + (i % 10) * 1000  # Salary varies slightly for demonstration
    }
    for i in range(1, 370)  # Create 369 entries (1 to 369)
]

# Save to a JSON file
with open("EmployeeData.json", "w") as file:
    json.dump(employees, file, indent=2)

print("369 Employee records saved to EmployeeData.json")
