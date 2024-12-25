def clone_data_from_dev_to_staging():
    """
    Clones data from the 'Dev' table to the 'Staging' table,
    transforming records to handle nested JSONs and trimming spaces.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Clear the Staging table before cloning
        print("Clearing Staging table...")
        cursor.execute("DELETE FROM Staging;")
        conn.commit()

        # Fetch data from Dev
        print("Fetching data from Dev table...")
        cursor.execute("SELECT rawData FROM Dev;")  # Assuming rawData contains the delimited strings
        raw_data = cursor.fetchall()

        if not raw_data:
            print("No data found in Dev table.")
            return

        # Transform and insert records
        for row in raw_data:
            if row[0] is None:  # Skip NULL rawData column values but continue processing the row
                print("Skipping invalid rawData field, but processing the record.")
                continue

            try:
                print(f"Processing record: {row[0]}")
                transformed = transform_record(row[0])  # Transform each record

                # Ensure salary is cast to INTEGER to match the database schema
                transformed["salary"] = int(float(transformed["salary"]))

                print(f"Transformed record: {transformed}")
                cursor.execute("""
                    INSERT INTO Staging (
                        employeeId, fullName, roleTitle, departmentName, salary, hireDate, email, terminationDate
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                """, (
                    transformed["employeeId"],
                    transformed["fullName"],
                    transformed["roleTitle"],
                    transformed["departmentName"],
                    transformed["salary"],
                    transformed["hireDate"],
                    transformed["email"],
                    transformed["terminationDate"]
                ))
            except Exception as e:
                print(f"Error processing record {row[0]}: {e}")

        conn.commit()
        print("Data successfully cloned and transformed from Dev to Staging (excluding rawData).")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
