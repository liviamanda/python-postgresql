# Finance Project

## Objective

This project aims to evaluate the concepts of Relational Databases and Pandas as follows:

- Ability to create a database in PostgreSQL (DDL)
- Ability to create tables using queries (DDL)
- Ability to insert data into tables (DML)
- Ability to apply transactions in queries (TCL)
- Ability to grant query access on the created database (DCL)
- Ability to preprocess data with Pandas before transferring to the SQL database
- Ability to retrieve data from the created database (DQL)

## Assignment Instructions and Cases

As a Data Engineer, the task is to assist the Finance division in organizing their data by creating a database on a PostgreSQL server.

Currently, they manage and store their data using Microsoft Excel, saved in **.csv** format. The data includes daily revenue and profit per product, segmentation, and country information. This data is not yet clean and ready to be imported into a database.

### 1. Data Exploration
1. Load the data file using Pandas and display the data. Provide insights from this step.
2. Display a summary of the data and explain the findings.
3. List the column names and describe the insights, including any necessary next steps.
4. List unique values for columns `Segment`, `Country`, `Product`, and `Discount Band`, and provide insights from this step.

### 2. Data Cleaning
Based on the exploration steps and findings, clean the data!

**Hint:** The following steps might be useful (adjust based on the data exploration results):
1. Manipulate columns, such as renaming, deleting, or adding columns.
2. Change data types as needed. For instance, remove currency symbols to convert values to the appropriate data type.
3. Check and handle missing values, possibly imputing them with zero if necessary.

### 3. Data Normalization
1. Normalize the cleaned data up to the 3rd Normal Form (3NF).
2. The normalized data should result in five tables, including the main table.
3. Ensure appropriate use of primary and foreign keys between tables.
4. Save all resulting tables as CSV files, named according to their corresponding database table names. Exclude the DataFrame index from the files as the table schema will use auto-incremental primary keys.

### 4. Relational Database & SQL
Create transactional queries covering multiple steps, from table creation to granting access. The guidelines are:
1. Create the database with a separate query outside of the transactional block. Note that creating a database in PostgreSQL cannot be combined with other queries. Run the database creation query and then comment it out.
2. Create a transactional block using TCL, including:
    - Table creation\
      Create tables from the normalized data with appropriate data types and primary/foreign keys. The primary key should be auto-incremental.
    - Data insertion\
      Use the `COPY` command to load data from CSV files into the database.
    - User creation\
      Create at least two users with usernames and passwords.
    - Granting query access\
      Grant `SELECT` command access to one user and restrict `INSERT`, `UPDATE`, `TRUNCATE`, and `DELETE` commands. The other user can have admin access with all query commands.
3. Execute the transactional block to create the tables and insert the data as per the cleaned and normalized CSV files.
4. Save the query as an **.sql** file.

### 5. Database Testing
After creating the tables, test the database and tables with the following cases:

1. Provide a table with the total profit per segmentation type, excluding non-discounted data.
2. Provide a table summarizing the statistics (average, minimum, and maximum) of Sales for each country.

This README provides an overview of the project's objectives and requirements. The main goal is to create a functional financial database, clean and normalize the data, and ensure proper database access and testing.
