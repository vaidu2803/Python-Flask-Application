
from flask import * 
from flask import Flask
from flask import Flask, render_template
import os
import sqlite3 

app = Flask(__name__)

@app.route("/")  
def index():  
    return render_template("index.html")

@app.route("/add")  
def add():  
    return render_template("add.html")

@app.route("/delete")  
def delete():  
    return render_template("delete.html")

@app.route("/update")  
def update():  
    return render_template("update.html", flag=True)

@app.route("/add",methods = ["POST","GET"])  
def saveDetails():  
    if request.method == "POST":  
        try:  
            student_id = request.form["id"]  
            name = request.form["name"]  
            contact = request.form["contact"]  
            address = request.form["address"]  
            qualifications = request.form["qualifications"]  
            percentage = request.form["percentage"]  
            passing_year = request.form["passing_year"] 

            with sqlite3.connect("databases.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into student (id, name, contact, address) values (?,?,?,?)",(student_id, name,contact,address))  
                con.commit()  
                cur.execute("INSERT into student_academics (id, qualifications, percentage, passing_year) values (?,?,?,?)",(student_id, qualifications, percentage, passing_year))  
                con.commit()
        except: 
            con.rollback()  
        finally:  
            return render_template("index.html")
            con.close()



@app.route("/delete",methods = ["POST"])  
def deleterecord():  
    student_id = request.form["id"]  
    with sqlite3.connect("databases.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from student where id = ?",student_id)  
            cur.execute("delete from student_academics where id = ?",student_id)  
        except:  
            pass
        finally:  
            return render_template("index.html")

@app.route("/update",methods = ["POST"])  
def updaterecord():  
    if request.method == "POST":  
        try:  
            student_id = request.form["id"]  
            name = request.form["name"]  
            contact = request.form["contact"]  
            address = request.form["address"]  
            qualifications = request.form["qualifications"]  
            percentage = request.form["percentage"]  
            passing_year = request.form["passing_year"] 

            with sqlite3.connect("databases.db") as con:  
                cur = con.cursor()  
                cur.execute("UPDATE student SET name = ? , contact = ? , address = ? WHERE id = ? ;",(name,contact,address, student_id))  
                con.commit()  
                cur.execute("UPDATE student_academics SET qualifications = ? , percentage = ? , passing_year = ? WHERE id = ? ;",(qualifications, percentage, passing_year, student_id))  
                con.commit()   
        except: 
            con.rollback()  
        finally:  
            return render_template("index.html")
            con.close()

@app.route("/update_search",methods = ["POST"])  
def updatesearch():  
    student_id = request.form["id"]  
    with sqlite3.connect("databases.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("select * from student where id = ?",student_id)  
            row_student = cur.fetchone()
            cur.execute("select * from student_academics where id = ?",student_id)  
            row_student_academics = cur.fetchone()
            row = row_student[i] + row_student_academics[i][1:]
            print(row)
        except:  
            pass
        finally:  
            return render_template("update.html", flag=False, student_id=student_id)

@app.route("/view")  
def viewDetails():  
    con = sqlite3.connect("databases.db")  
    cur = con.cursor()  
    cur.execute("select * from student")  
    rows_student = cur.fetchall()
    cur.execute("select * from student_academics")  
    rows_student_academics = cur.fetchall()
    rows = []
    for i in range(len(rows_student)):
        element = rows_student[i] + rows_student_academics[i][1:]
        rows.append(element)
        
    return render_template("view.html",rows = rows)       

if __name__ == "__main__":
    app.run(debug=True)








