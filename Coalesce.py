import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
    'Sale_Price': [1200, None, 300, None],
    'Suggested_Price': [1150, None, 250, 70],
    'Default_Price': [1000, 20, 50, 50]
}
Data = pd.DataFrame(data)

print("-----Original Data Frame-----")
print(Data)

query_1 = """
SELECT
    product,
    Sale_Price,
    Suggested_price,
    coalesce(sale_price, suggested_price) as Final_Price
    from Data;"""
result_1 = sqldf(query_1)
print("-----Coalesce with Vector-----")
print(result_1)

query_2 = """
select product, sale_price, coalesce(sale_price, 1000) as Sales_Price from Data;"""
result_2 = sqldf(query_2)
print("-----Coalesce with Scalar-----")
print(result_2)