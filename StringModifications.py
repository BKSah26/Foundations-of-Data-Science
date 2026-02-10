import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

#Creating sample DataFrame
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['alice', 'BOB SMITH', 'Charlie.D', 'dave ', 'eve '],
    'ProductCode': ['A-101-L', 'b-102-XL', 'C-303-S', 'A-101-M', 'D-404-M'],
    'Email': ['aLice@mail.com', 'BOB@work.net', 'charLIE@web.io', 'dave@corp.co', 'eve@home.net']
}

Customer = pd.DataFrame(data)

# Upper and Lower
query_1 = "select CustomerID, UPPER(TRIM(Name)) as Standardised_Name, LOWER(Email) as Cleaned_Email from Customer;"
result_df_1 = sqldf(query_1)
print("-----Upper and Lower Case-----")
print(result_df_1)

# Left and Right Trim
query_2 = "select CustomerID, RTRIM(Name) as Right_Trimmed_Name, LTRIM(Email) as LeftTrimmedEmail from Customer;"
result_df_2 = sqldf(query_2)
print("-----Left and Right Trim-----")
print(result_df_2)

# Replace
query_3 = "select CustomerID, ProductCode, REPLACE(REPLACE(ProductCode, 'L', 'XL'), '-', '') as Cleaned_Product_Code from Customer;"
result_df_3 = sqldf(query_3)
print("-----Replace-----")
print(result_df_3)

#Substring using Left and Right
query_4 = "select CustomerID, ProductCode, LEFT(ProductCode, 3) as Item_Prefix, RIGHT(Email, 4) as Domain_Suffix from Customer;"
result_df_4 = sqldf(query_4)
print("-----Substring using Left and Right-----")
print(result_df_4)

#Substring Function
query_5 = "select CustomerID, ProductCode, SUBSTR(ProductCode, 1, 3) as Item_Prefix, SUBSTR(Email, -4) as Domain_Suffix from Customer;"
result_df_5 = sqldf(query_5)
print("-----Substring using SUBSTR Method-----")
print(result_df_5)


