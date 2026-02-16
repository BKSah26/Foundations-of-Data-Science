import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

data = {
    "EmployeeName": ["David", "Edward", "Alice", "Bob", "Charlie", "Fiona"],
    "Salary": [50000, 60000, 55000, 45000, 70000, 52000],
}
Data = pd.DataFrame(data)

# Rank Employees by Salary
query = """
Select EmployeeName, Salary, Row_Number() OVER (ORDER BY Salary DESC) AS Row_Number, Rank() OVER (ORDER BY Salary DESC) AS RankVal,
Dense_Rank() OVER (ORDER BY Salary DESC) AS DenseRankVal,
Round((Percent_Rank() OVER (ORDER BY Salary DESC)), 2) AS PercentRankVal
FROM Data"""
ranking_result = sqldf(query)
print("-----Employee Salary Ranking with Multiple Functions-----")
print(ranking_result)
print()