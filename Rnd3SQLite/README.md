# Rnd3SQLite Project

Technical Skills Assessment Study Document

1. Problem-Solving Framework

1.1 Clarify the Problem

    Ask Questions: Ensure you understand the requirements, constraints, and goals.

        ##Example: "What is the expected output format for this data transformation?"

        ##Example: "Should we prioritize performance over readability in this solution?"

    Confirm Inputs and Outputs: Validate the provided data structure, expected results, and context of the problem.

1.2 Break Down the Problem

Understand the Scope: Decompose complex issues into smaller, manageable tasks.

Example: "First, I’ll extract data from the JSON structure. Then, I’ll transform it into a relational database format."

Plan the Steps:

Extract data from JSON.

Transform and normalize the data.

Load the data into a relational database.

Perform specific data manipulations and verify changes.

1.3 Articulate Technical Tradeoffs

Consider: Performance vs. Maintainability

Example: Using SQL string manipulation for immediate changes versus Python for greater control.

Consider: Automation vs. Manual Work

Example: Writing scripts for repeated tasks instead of manual intervention for efficiency.

2. Key Technical Concepts

2.1 Working with Nested JSON

Why It Matters: Real-world data is often hierarchical and unstructured.

Approach:

Traverse the nested structure to locate required fields.

Flatten hierarchical data into tabular format for relational database compatibility.

2.2 SQL Data Management

**Table Creation:**
```sql
CREATE TABLE TeamMembers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ProjectId VARCHAR(255),
    ProjectName VARCHAR(255),
    TeamMember VARCHAR(255)
);
```

**Data Insertion:**
```
INSERT INTO TeamMembers (ProjectId, ProjectName, TeamMember)
VALUES (?, ?, ?);
```

**Data Manipulation:**
**Removing characters:**
```
UPDATE TeamMembers
SET ProjectId = CONCAT(SUBSTRING(ProjectId, 1, 1), SUBSTRING(ProjectId, 3))
WHERE ProjectId LIKE 'P1%';
```

**Restoring original format:**
```
UPDATE TeamMembers
SET ProjectId = CONCAT(SUBSTRING(ProjectId, 1, 1), '1', SUBSTRING(ProjectId, 2))
WHERE ProjectId LIKE 'P%';
```

2.3 Python Integration

JSON Parsing and Extraction:

def extract_team_members(data):
    rows = []
    projects = data["Item"]["Projects"]["L"]
    for project in projects:
        project_id = project["M"]["ProjectId"]["S"]
        project_name = project["M"]["ProjectName"]["S"]
        team_members = project["M"]["TeamMembers"]["L"]
        for member in team_members:
            rows.append((project_id, project_name, member["S"]))
    return rows

Updating Records:

# Remove second digit in ProjectId
for row in rows:
    updated_project_id = row[0][0] + row[0][2:]  # P1001 -> P001
    cursor.execute(
        "UPDATE TeamMembers SET ProjectId = %s WHERE ProjectId = %s",
        (updated_project_id, row[0])
    )

3. Communication Strategies

3.1 Stakeholder Engagement

Adapt Language: Tailor explanations to the audience’s technical level.

Example (Non-Technical Audience): "We’re simplifying the data structure to make it easier to use in other tools."

Example (Technical Audience): "Flattening the JSON hierarchy allows efficient relational joins and optimizes query performance."

3.2 Justify Decisions

Always explain why you’ve chosen a particular approach.

Example: "I used SQL string functions for transformations because it’s faster for small datasets compared to Python."

3.3 Discuss Tradeoffs

Be transparent about limitations or potential risks.

Example: "Using Python for data manipulation adds overhead but provides better readability and reuse for future tasks."

4. Practice Exercise

Scenario:

You’re provided with a nested JSON object containing project and team member data.

Your task is to extract the data, store it in a database, and update specific fields.

Steps:

Extract Data:

Parse the JSON structure.

Identify key fields (e.g., ProjectId, ProjectName, TeamMembers).

Store in Database:

Create a MySQL table.

Insert extracted rows into the table.

Transform Data:

Update ProjectId to remove the second digit.

Revert the changes.

Verify Results:

Query the database to confirm updates.

Expected Deliverables:

A clear explanation of how you tackled each step.

Discussion of any challenges encountered and how you resolved them.

Justification for your choices.

5. Key Takeaways

Technical Proficiency: Showcase your ability to navigate nested structures, use SQL effectively, and integrate Python.

Problem-Solving Mindset: Emphasize structured thinking and adaptability.

Communication: Clearly articulate your reasoning, constraints, and tradeoffs to diverse stakeholders.