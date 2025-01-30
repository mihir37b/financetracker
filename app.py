from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch all rows from the database
def fetch_data():
    conn = sqlite3.connect('budget_data.db') 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM details") 
    rows = cursor.fetchall()
    conn.close()
    return rows

 
@app.route("/")
def display_table():
    data = fetch_data()  
    return render_template("table.html", rows=data) 

if __name__ == "__main__":
    app.run(debug=True)
