import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

students_df = {
    'StudentID': [1, 2, 3, 4, 5],
    'Name': ['Zoe', 'Liam', 'Noah', 'Emma', 'Ava'],
    'Score' : [95, 85, 80, 92, 73]
}
Students = pd.DataFrame(students_df)
print("-----Original Data Frame-----")
print(Students)

switch_query = """
Select StudentID, Name, Score,
CASE
    WHEN Score>=90 THEN 'A'
    WHEN Score>=80 THEN 'B'
    WHEN SCORE>=70 THEN 'C'
    WHEN SCORE>=60 THEN 'D'
    ELSE 'F'
END as Grade,
CASE
    WHEN SCORE>=60 then 'Pass'
    Else 'Fail'
END as Status from Students;"""
result = sqldf(switch_query)
print("-----Student Grade Sheet-----")
print(result)