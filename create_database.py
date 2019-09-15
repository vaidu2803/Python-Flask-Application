import sqlite3  
  
con = sqlite3.connect("databases.db")  
print("Database opened successfully")  
  
con.execute("create table student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, contact TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")
con.execute("create table student_academics (id INTEGER PRIMARY KEY AUTOINCREMENT, qualifications TEXT NOT NULL, percentage TEXT UNIQUE NOT NULL, passing_year TEXT NOT NULL)")
  
print("Table created successfully")  
  
con.close()  