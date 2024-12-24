-- Migration #3: Add email and terminationDate columns and populate them

-- Add the 'email' column to the 'employees' table
ALTER TABLE employees
ADD COLUMN email TEXT;

-- Add the 'terminationDate' column to the 'employees' table
ALTER TABLE employees
ADD COLUMN terminationDate TEXT;

-- Update the email column with the formatted email addresses
UPDATE employees
SET email = 
    LOWER(REPLACE(fullName, ' ', '.') || '@securingbytes.com')
WHERE fullName IS NOT NULL;

-- Set termination dates for 10 employees
-- For simplicity, termination date is 5 years after their hire date
UPDATE employees
SET terminationDate = (
    SELECT DATE(hireDate, '+5 years')  -- Termination date is 5 years after hire date
)
WHERE employeeId IN (2, 5, 8, 11, 14, 17, 20, 23, 26, 29);