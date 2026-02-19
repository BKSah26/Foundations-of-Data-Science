import numpy as np
import pandas as pd
import duckdb

def sqldf(query):
    return duckdb.sql(query).df()

data={
    'Student':['Sam','Jia','Leo','Mia','Ted','Zoe','Ben','Eva','Abe','Dan'],
    'Score':[95,88,88,76,72,65,60,55,40,30]
}
Grades = pd.DataFrame(data)
print("-----Grades-----") 
print(Grades)

ntile_query="""SELECT student, score, NTILE(4) OVER (ORDER BY score) AS quartile
        ,CUME_DIST() OVER (ORDER BY score DESC) AS cume FROM Grades"""
ntile_result = sqldf(ntile_query)
print("-----NTILE and CUME_DIST Result-----")
print(ntile_result)


data = { 'Player': ['Apex', 'Brave', 'Cinder', 'Drift', 'Echo', 'Frost'], 
        'Level': [10, 12, 8, 15, 10, 14],
        'Score': [2500, 3200, 1800, 4500, 2900, 4100]
}
Leaderboard = pd.DataFrame(data)
print("-----Leaderboard DataFrame-----")
print(Leaderboard)
query="SELECT Player, Score, LAG(Score) OVER (ORDER BY Score DESC) AS Prev_Score,LEAD(Score) OVER (ORDER BY Score DESC) AS Next_Score,FIRST_VALUE(Score) OVER (ORDER BY Score DESC) AS First_Score,LAST_VALUE(Score) OVER (ORDER BY Score DESC) AS Last_Score FROM Leaderboard"
window_result=sqldf(query)
print("-----Window Function Result-----")
print(window_result)