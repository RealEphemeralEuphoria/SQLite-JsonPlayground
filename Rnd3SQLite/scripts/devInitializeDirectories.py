import os
import sqlite3

# Define project structure
PROJECT_DIR = "Rnd3SQLite"
FOLDERS = ["db", "migrations", "scripts", "queries"]
DB_NAME = "employees.db"

def create_project_structure():
    """
    Creates the project folder structure and an empty SQLite database.
    """
    # Create the base project directory
    if not os.path.exists(PROJECT_DIR):
        os.mkdir(PROJECT_DIR)
        print(f"[INFO] Created project directory: {PROJECT_DIR}")
    else:
        print(f"[INFO] Project directory already exists: {PROJECT_DIR}")

    # Create subfolders
    for folder in FOLDERS:
        folder_path = os.path.join(PROJECT_DIR, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
            print(f"[INFO] Created folder: {folder_path}")
        else:
            print(f"[INFO] Folder already exists: {folder_path}")

    # Create the SQLite database
    db_path = os.path.join(PROJECT_DIR, "db", DB_NAME)
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        conn.close()
        print(f"[INFO] Created SQLite database: {db_path}")
    else:
        print(f"[INFO] SQLite database already exists: {db_path}")

    # Create README.md and .gitignore
    create_readme()
    create_gitignore()

def create_readme():
    """
    Creates a basic README.md file in the project directory.
    """
    readme_path = os.path.join(PROJECT_DIR, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write("# Rnd3SQLite Project\n\nThis project is for working with SQLite databases.\n")
        print(f"[INFO] Created README.md: {readme_path}")
    else:
        print(f"[INFO] README.md already exists: {readme_path}")

def create_gitignore():
    """
    Creates a basic .gitignore file in the project directory.
    """
    gitignore_path = os.path.join(PROJECT_DIR, ".gitignore")
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, "w") as f:
            f.write("*.db\n*.sqlite\n__pycache__/\n")
        print(f"[INFO] Created .gitignore: {gitignore_path}")
    else:
        print(f"[INFO] .gitignore already exists: {gitignore_path}")

if __name__ == "__main__":
    create_project_structure()
