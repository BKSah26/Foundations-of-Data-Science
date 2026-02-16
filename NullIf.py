import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Revenue': [5000, 200, 1500, 0],
    'Units_Sold': [10, 5, 0, 0],
    'Category': ['Electronics', '', 'Electronics', 'Unknown']
}
Data = pd.DataFrame(data)

print("-----Original Data Frame-----")
print(Data)

query_1 = """
Select product, revenue/NULLIF(units_sold, 0) as Revenue, NULLIF(Category, '') as Category from Data;"""
result_1 = sqldf(query_1)
print("-----Data Frame using NULLIF-----")
print(result_1)