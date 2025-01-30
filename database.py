import sqlite3

def connect_db():
  connection = sqlite3.connect('budget_data.db')
  return connection

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS details (
            id INTEGER PRIMARY KEY,
            mainIncome INTEGER,
            secondIncome INTEGER,
            sideIncome INTEGER,
            expenses INTEGER,
            housing INTEGER,
            grocery INTEGER,
            taxes INTEGER, 
            healthcare INTEGER,
            entertainment INTEGER,
            child INTEGER,
            debt INTEGER,
            other INTEGER,
            totalIncome INTEGER  
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(main_income, secondary_income, side_income, expenses, housing, groceries,
            taxes, healthcare, entertainment, child, debt, other, total_income):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO details (mainIncome, secondIncome, sideIncome, expenses, housing, grocery, taxes, healthcare, entertainment, child, debt, other, totalIncome)  
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (main_income, secondary_income, side_income, expenses, housing, groceries,
            taxes, healthcare, entertainment, child, debt, other, total_income))
    conn.commit()
    conn.close()     

def update_user(main_income, secondary_income, side_income, expenses, housing, groceries,
                taxes, healthcare, entertainment, child, debt, other, total_income):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE details 
        SET mainIncome=?, secondIncome=?, sideIncome=?, expenses=?, housing=?, 
            grocery=?, taxes=?, healthcare=?, entertainment=?, child=?, debt=?, other=?, totalIncome=?
        WHERE id = 1
    ''', (main_income, secondary_income, side_income, expenses, housing, groceries,
          taxes, healthcare, entertainment, child, debt, other, total_income))

    conn.commit()
    conn.close()

def clear_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM details")  
    conn.commit()
    conn.close()
    print("Table cleared successfully.")

def delete_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS details")
    conn.commit()
    conn.close()
    print("Table cleared successfully.")

def print_all_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM details")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
 
 