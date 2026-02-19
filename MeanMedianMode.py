import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

properties = {
    "House_ID": [1, 2, 3, 4, 5, 6],
    "Price": [2000000, 25000000, 15000000, 350000, 23500000, 5000000]
}
Properties = pd.DataFrame(properties)

query = """
Select round(avg(price), 2) as mean_price,
median(price) as median_price,
mode(price) as mode_price
from Properties"""
result = sqldf(query)
print(result)
