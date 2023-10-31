# Faisal Alqarni
# Python 3.11.0, psql (PostgreSQL) 10.15, pip 23.3.1

# Prepration for running the script:-
# (OPTIONAL)
# I am running the script in a Virtual Enviornment to have a clean and isolated environment.
# You can set up a virtual environment by running the following commands in your terminal (in the project path):
# On macOS and Linux: python3 -m venv env
# On Windows: py -m venv env

# To activate the virtual environment, run the following command in the project path:
# On macOS and Linux: source env/bin/activate
# On Windows: .\env\Scripts\activate

# Step 1 PIP Dependencies:
# To install the needed dependencies for this script, run the following command in the project path:
# pip install -r requirements.txt

# Step 2 Setting Up DB Locally:
# psql -c "CREATE DATABASE python_postgress_assessments" "user=postgres dbname=postgres password=1111"


# import psycopg2 module library to interact with postgresql database
import psycopg2
import tabulate

# Extra: I am using try and except to handle any errors that might happen during the execution of the script.
try:
    # First task: establish the connection to the database.
    print('FIRST TASK:-')
    print("Creating a connection to the database...")
    connection = psycopg2.connect(database="python_postgress_assessments",
                                  host="localhost",
                                  user="postgres",
                                  password="1111",
                                  port="5432")
    cursor = connection.cursor()
    print("Connection established successfully to the database")
    print("\n===============================================\n")

    # Second task: Create 'employees' table in the database with columns for ID, name, department, and salary.
    # First lets Drop the table if it is exists just to make sure.
    print('SECOND TASK:-')
    print("creating 'employees' table...")
    cursor.execute("DROP TABLE IF EXISTS employees")

    # then prepare the sql query to create the table
    # Note 1: I am using SERIAL data type for the ID column to auto increment the ID value.
    # Note 2: I would suggest creating a department table to store the departments and then reference it in the employees table. but it is out of scope for this assessment.
    create_table_query = '''CREATE TABLE employees(
                  ID SERIAL PRIMARY KEY,
                  name VARCHAR(255) NOT NULL,
                  department VARCHAR(255) NOT NULL, 
                  salary NUMERIC(10, 2) NOT NULL
  )'''

    # execute the query
    cursor.execute(create_table_query)

    # commit the changes to the database
    connection.commit()

    # inform the user about the table creation
    print("Table created successfully in PostgreSQL")
    print("\n===============================================\n")

    # Third task: Insert the following data into the table:
    # prepare the insert query
    print('THIRD TASK:-')

    def add_employees(employee_records):
        insert_records_query = """ INSERT INTO employees(ID, name, department, salary) VALUES (%s,%s,%s,%s)"""
        # prepare the data to be inserted
        print("Inserting %s records:" % (len(employee_records),))
        for record in employee_records:
            # execute the query for each employee record
            cursor.execute(insert_records_query, record)
            # commit the changes to the database
            connection.commit()
            # inform the user about the record insertion
            print("Information of %s with ID %s inserted successfully" %
                  (record[1], record[0]))

    # test add_employees function
    print("Inserting records into the table...")
    employee_records = [
        (1, 'John', 'IT', 1000.00),
        (2, 'Marie', 'HR', 2000.00),
        (3, 'Peter', 'IT', 1500.00),
        (4, 'Mary', 'IT', 2000.00),
        (5, 'Steve', 'HR', 2500.00),
        (6, 'Tom', 'HR', 3000.00),
        (7, 'Kate', 'IT', 3500.00),
        (8, 'Mike', 'IT', 4000.00),
        (9, 'Bob', 'HR', 4500.00),
        (10, 'Alex', 'IT', 5000.00)
    ]
    add_employees(employee_records)
    cursor.execute("SELECT COUNT(*) FROM employees")
    count = cursor.fetchone()[0]
    if count == len(employee_records):
        print("Passed, %s records got inserted successfully" % count)
    else:
        print("Failed, %s records got inserted, but the actual is" %
              (count, len(employee_records)))
    print("\n===============================================\n")

    # Fourth task: Update the salary of employee with ID 5 to 3000.00
    print('FOURTH TASK:-')

    def update_salary(id, new_salary):
        # check if the employee exists
        # if the employee exists, update his salary if it does, else inform the user that the employee does not exist and return false
        cursor.execute("SELECT * FROM employees WHERE ID = %s", (id,))
        employee_record = cursor.fetchone()
        if employee_record:
            # get the old salary of the employee
            old_salary = employee_record[3]
            print("Updating salary of employee with ID %s from %s to %s" %
                  (id, old_salary, new_salary))
            # prepare the update query
            update_salary_query = """ UPDATE employees SET salary = %s WHERE ID = %s"""
            # execute the query
            cursor.execute(update_salary_query, (new_salary, id))
            # commit the changes to the database
            connection.commit()
            # inform the user about the update
            print("Salary of employee with ID %s updated successfully from %s to %s" %
                  (id, old_salary, new_salary))
            return True
        else:
            # if the employee does not exist
            print("Employee with ID %s does not exist" % id)
            return False

    # test update_salary function
    update_salary(1, 9999)
    cursor.execute("SELECT * FROM employees WHERE ID = %s", (1,))
    employee_record = cursor.fetchone()
    if employee_record[3] == 9999:
        print("Passed, Salary of employee with ID %s updated successfully" % 1)
    else:
        print("Failed, Salary of employee with ID %s did not update" % 1)
    print("\n===============================================\n")

    # Fifth task: Delete the employee with ID 2 from the table
    print('FIFTH TASK:-')

    def delete_employee(id):
        # check if the employee exists
        # if the employee exists, delete it if it does, else inform the user that the employee does not exist and return false
        cursor.execute("SELECT * FROM employees WHERE ID = %s", (id,))
        employee_record = cursor.fetchone()
        if employee_record:
            # prepare the delete query
            delete_employee_query = """ DELETE FROM employees WHERE ID = %s"""
            # execute the query
            cursor.execute(delete_employee_query, (id,))
            # commit the changes to the database
            connection.commit()
            # inform the user about the deletion
            print("Employee with ID %s deleted successfully" % id)
            return True
        else:
            # if the employee does not exist
            print("Employee with ID %s does not exist" % id)
            return False

    # test delete_employee function
    id_to_delete = 2
    delete_employee(id_to_delete)
    cursor.execute("SELECT * FROM employees WHERE ID = %s", (id_to_delete,))
    employee_record = cursor.fetchone()
    if employee_record:
        print("Failed, Employee with ID %s still exists" % id_to_delete)
    else:
        print("Passed, Employee with ID %s does not exist" % id_to_delete)
    print("\n===============================================\n")

    # Sixth task: Retrieves and displays all the information of the employees from the table.
    print('SIXTH TASK:-')
    # prepare the select query
    get_employees_query = """ SELECT * FROM employees ORDER BY ID ASC"""
    # execute the query
    cursor.execute(get_employees_query)
    # fetch all the records
    employees = cursor.fetchall()
    # inform the user about the number of records retrieved
    print("Retrieved %s records:" % len(employees))
    # print the records
    print(tabulate.tabulate(employees, headers=[
        "ID", "Name", "Department", "Salary"]))
    print("\n===============================================\n")

except (Exception, psycopg2.Error) as error:
    print("Error happend:", error)

finally:
    # close connection.
    if connection:
        cursor.close()
        connection.close()
        print("connection closed successfully")
