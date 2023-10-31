# Python Postgres Assessment
This is the solution of an assessment where I was required to write a Python program that works with a PostgreSQL database. The program needs to perform different operations like adding, updating, deleting, and retrieving data from the database.


## Tech Used
- Python 3.11.0
- pip 23.3.1
- psql (PostgreSQL) 16.0

## Python libraries
- psycopg2
- tabulate

--------------------------
### Installing Dependencies

#### Python 3.11.0
Preferably install Python 3.11.0

#### psql (PostgreSQL) 16.0
Preferably install psql (PostgreSQL) 16.0

#### (OPTIONAL) Set up a Virtual Environment
I am running the script in a Virtual Environment to have a clean and isolated environment.
You can set up a virtual environment by running the following commands in your terminal (in the project path):

On macOS and Linux:
```bash
python3 -m venv env
```
On Windows:
```bash
py -m venv env
```


###### Activate a Virtual Environment:
On macOS and Linux:
```bash
source env/bin/activate
```
On Windows:
```bash
.\env\Scripts\activate
```

#### STEP 1: PIP Dependencies

Once you have your virtual environment setup and running, you can install dependencies by navigating to the **root directory** and run:

```bash
pip install -r requirements.txt
```

This will install all of the required packages inside `requirements.txt` file.


#### Step 2 Setting Up DB Locally:
After successful installing all requirements for the project. You can run and test the script by doing these two steps:

1. Create Databases. 
```
psql -c "CREATE DATABASE python_postgress_assessments" "user=postgres dbname=postgres password=1111"
```

2. Run the application by using the command below
```
python python_postgres.py
```
-------------------------

## Assessment content:
##### Assignment: Python and PostgreSQL Database Manipulation

##### Description:
Write a Python program that works with a PostgreSQL database. Your program needs to perform different operations like adding, updating, deleting, and retrieving data from the database.

##### Requirements:
1. Set up a PostgreSQL database on your computer or use an existing one.
2. Create a Python script that does the following:

##### Tasks:
1. Connects to the PostgreSQL database.
2. Creates a table named "employees" with columns for ID, name, department, and salary.
3. Adds at least 5 employee records to the "employees" table.
4. Updates the salary of an employee with a specific ID.
5. Deletes an employee from the table based on their ID.
6. Retrieves and displays all the information of the employees from the table.

##### Instructions:
1. Write a Python script that carries out the tasks mentioned above.
2. Use comments in your code to explain each step and what it does.
3. Test your program by running it and check if it produces the desired results.
4. Share your Python script with any necessary instructions or information about the PostgreSQL database used.
