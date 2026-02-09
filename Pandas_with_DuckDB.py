import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

# 1. Create the DataFrame
data = {
    'EmployeeID' : [101, 102, 103, 105, 107], 
    'LastName' : ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
    'Department' : ['Sales', 'IT', 'Marketing', 'IT', 'HR'],
    'Salary' : [65000, 76000, 85000, 120000, 125000],
    'HireDate' : ['2023-01-05', '2023-01-06', '2023-06-01', '2024-08-20', '2023-10-10']
}
Employees = pd.DataFrame(data)

print("-----Original Data Frame-----")
print(Employees)

# Define simple SQL Query
sql_query = "select * from Employees;"
result_df = sqldf(sql_query)
print("-----New Data Frame using SQL-----")
print(result_df)

query_1 = "select EmployeeID, Salary from Employees;"
new_df_1 = sqldf(query_1)
print("-----Selection of Specified Columns-----")
print(new_df_1)

query_2 = "select * from Employees where Department = 'Sales';"
new_df_2 = sqldf(query_2)
print("-----Filtered by Department of Employees-----")
print(new_df_2)

query_3 = "select * from Employees where Department = 'IT' and Salary>=100000;"
new_df_3 = sqldf(query_3)
print("-----Filtering based on Department and Salary using >= Operator-----")
print(new_df_3)

query_4 = "select * from Employees where Department = 'HR' or HireDate>'2024-06-030;'"
new_df_4 = sqldf(query_4)
print("-----Filtering using OR Operator-----")
print(new_df_4)

query_5 = "select * from Employees where NOT Department = 'IT';"
new_df_5 = sqldf(query_5)
print("-----Filtering using NOT Operator")
print(new_df_5)

query_6 = "select * from Employees where Salary between 75000 and 100000;"
new_df_6 = sqldf(query_6)
print("-----Filtering using Between Operator-----")
print(new_df_6)

query_7 = "select * from Employees where Department in ('IT', 'HR');"
new_df_7 = sqldf(query_7)
print("-----Filtering using IN Operator-----")
print(new_df_7)

# Pattern Matching
query_8 = "select * from Employees where LastName like 'J%' or Department = 'IT';"
new_df_8 = sqldf(query_8)
print("-----Pattern Matching using Like-----")
print(new_df_8)