import pandas as pd
#database den bilgi okumak için gereken kütüphane immport sqlite3
df = pd.read_csv('csv uzantılı dosyanın adı buraya yazılır')
df = pd.read_json('json uzantılı dosyanın adı buraya yazılır', encoding="UTF-8")
df = pd.read_excel('xlsx uzantılı dosyanın adı buraya yazılır')

#connection = sqlite3.connect("db uzantılı dosya adı buraya yazılır")
#df = pd.read_sql_query("SELECT * FROM student",connnection)

print(df)