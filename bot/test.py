import sqlite3
import pandas as pd

conn = sqlite3.connect('data/shelter/date.db') 
          
sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM users
                               ''', conn)

df = pd.DataFrame(sql_query)
print (df)