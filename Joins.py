import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

#Left Table
employees = {
    "Emp_ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Dept_ID": [10, 20, 10, 40],
}

Employees = pd.DataFrame(employees)

#Right Table
departments = {
    "Dept_ID": [10, 20, 30],
    "Department_Name": ["HR", "IT", "Marketing"]
}
Departments = pd.DataFrame(departments)

print("-----Employees Table-----")
print(Employees)
print()

print("-----Departments Table-----")
print(Departments)
print()

#Inner Join
inner_join = """
SELECT * from Employees e
INNER JOIN Departments d on e.dept_id = d.dept_id
"""
result = sqldf(inner_join)
print("-----Inner Join Result-----")
print(result)
print()

inner_join = """
select e.name, d.department_name from Employees e
inner join Departments d on e.dept_id = d.dept_id
"""
result = sqldf(inner_join)
print("-----Inner Join Result (Selected Columns)-----")
print(result)
print()

#Left Join
left_join = """
SELECT * from Employees e
LEFT JOIN Departments d on e.dept_id = d.dept_id
"""
result = sqldf(left_join)
print("-----Left Join Result-----")
print(result)
print()

#Right Join
right_join = """
SELECT * from Employees e
RIGHT JOIN Departments d on e.dept_id = d.dept_id
"""
result = sqldf(right_join)
print("-----Right Join Result-----")
print(result)
print()

#Full Outer Join
full_outer_join = """
select * from Employees e
Full Outer Join Departments d ON e.dept_id = d.dept_id
"""
result = sqldf(full_outer_join)
print("-----Full Outer Join-----")
print(result)
print()

