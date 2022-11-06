import os
import sqlite3

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()


query_sql = ''' 
 SELECT SUM(UnitPrice * Quantity)
    FROM invoice_items;
'''

rows = cur.execute(query_sql).fetchall()

for row in rows:
    print(*row)


