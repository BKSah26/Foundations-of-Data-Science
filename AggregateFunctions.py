import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

#New DataFrame
sales_data = {
    'City': ['NY', 'LA', 'NY', 'LA', 'Chicago'],
    'Sales': [100, 150, 120, 90, 80]
}
Sales = pd.DataFrame(sales_data)

print("-----Original Data Frame-----")
print(Sales)

query = "select City, Sum(Sales) as Total_Sales from Sales group by city order by Total_Sales desc;"
result = sqldf(query)
print("-----Data Filtering using Sum, Group By and Order By-----")
print(result)