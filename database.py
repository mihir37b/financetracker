import sqlite3
connection = sqlite3.connect('budget_data.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS details (
        id INTEGER PRIMARY KEY,
        name TEXT,
        mainIncome INTEGER,
        secondIncome INTEGER,
        sideIncome INTEGER,
        expenses INTEGER,
        housing INTEGER,
        grocery INTEGER,
        taxes INTEGER,
        transportation INTEGER,
        healthcare INTEGER,
        entertainment INTEGER,
        child INTEGER,
        debt INTEGER,
        other INTEGER,
        totalIncome INTEGER  
    )
''')

cursor.execute('''
    INSERT INTO details (name,mainIncome,secondIncome,sideIncome,expenses,housing,grocery,taxes,transportation,healthcare,entertainment,child,debt,other,totalIncome) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', ('John Doe', 30, 20,20,40,00,100,100,103,10, 100, 120, 130, 140, 100))

connection.commit()

cursor.execute('SELECT * FROM details')
rows = cursor.fetchall()

for row in rows:
    print(row)
