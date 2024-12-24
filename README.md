# SQLite Playground

This is a sample project structure for version-controlling SQL queries and schemas in SQLite.

## Structure

- **sql/migrations/**: Incremental changes to your database schema.
- **sql/queries/**: Reusable SELECT or reporting queries.
- **sql/schema_latest.sql**: A file to build the full schema from scratch.
- **README.md**: Explanation and docs.
- **.gitignore**: List of files/directories Git should ignore.

## Usage

1. Run migrations with: `sqlite3 my_data.db < sql/migrations/001_create_my_data.sql`
2. Insert or manipulate data as needed.
3. Query data: `sqlite3 my_data.db < sql/queries/analytics_query.sql`
