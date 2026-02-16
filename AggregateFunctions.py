import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

data = {
    "Transaction_ID": [1, 2, 3, 4, 5, 6],
    "Category": ["Electronics", "Furniture", "Electronics", "Electronics", "Furniture", "Toys"],
    "Sales_Amount": [1200, 450, 800, 150, 300, 50],
    "Quantity": [1, 2, 1, 3, 2, 5],
    "Discount": [0.1, 0.2, 0.05, 0.15, 0.1, 0]
}
Data = pd.DataFrame(data)

#Distinct Categories
distinct_query = "SELECT DISTINCT Category FROM Data;"
distinct_result = sqldf(distinct_query)
print("-----Distinct Categories-----")
print(distinct_result)
print()

#Greatest and Least
greatest_least_query = "SELECT GREATEST(15000, Sales_Amount), LEAST(500, Sales_Amount) FROM Data;"
greatest_least_result = sqldf(greatest_least_query)
print("-----Greatest and Least Sales Amount-----")
print(greatest_least_result)
print()

# Sum, Avg, Count, Min, Max
aggregate_query = "SELECT SUM(Sales_Amount) AS Total_Revenue, AVG(Sales_Amount) AS Average_Sales, MIN(Sales_Amount) AS Min_Sales, MAX(Sales_Amount) AS Max_Sales, COUNT(Transaction_ID) as No_of_Transactions FROM Data;"
aggregate_result = sqldf(aggregate_query)
print("-----Aggregate Functions by Category-----")
print(aggregate_result)
print()

#Group By
group_by_query = "SELECT Category, SUM(Sales_Amount) AS Category_Revenue, Count(*) as Item_Count FROM Data GROUP BY Category;"
group_by_result = sqldf(group_by_query)
print("-----Total Revenue by Category-----")
print(group_by_result)
print()

#Order By
order_by_query = "SELECT Category, SUM(Sales_Amount) AS Category_Revenue FROM Data GROUP BY Category ORDER BY Category_Revenue DESC;"
order_by_result = sqldf(order_by_query)
print("-----Total Revenue by Category (Ordered)-----")
print(order_by_result)
print()

