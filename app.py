import sqlite3
from flask import Flask, render_template, request, redirect
from dbconnection import createconnection 
from todo import Todo
app = Flask(__name__) 
@app.route("/test")
def test():
    connection=createconnection()
    cursor=connection.cursor()
    cursor.execute("select * from to_do_list")
    rows=cursor.fetchall()
    print(rows)
    return rows

@app.route("/List")
def list():
    connection=createconnection()
    cursor=connection.cursor()
    cursor.execute("select * from to_do_list")
    cur = connection.cursor()
    cur.execute("select * from author")
    rows = cur.fetchall()
    print(rows)
    # for row in rows:
    # print(row)
    return render_template("viewauthors.html", authors=rows)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/new")
def new():
    return render_template("newitem.html")
@app.route("/insert",methods=["post"])
def insert():
    task=request.form["task"]
    due_date=request.form["due_date"]
    note=request.form["note"]
    status=request.form["status"]
    print(task,due_date,note,status)
    connection=createconnection()
    cursor=connection.cursor()
    cursor.execute("INSERT INTO to_do_list (task,due_date,note, status)VALUES (?, ?, ?, ?)",(task,due_date,note,status))
    connection.commit()
    cur=connection.cursor()
    cur.execute("select * from to_do_list")
    rows = cur.fetchall()
    print(rows)
    return render_template("to_do_list.html", to_do_list=rows)

@app.route("/to_do_list")
def to_do_list():
    todo_list=[]
    connection = createconnection()
    cur = connection.cursor()
    cur.execute(
        "select * from to_do_list")
    rows = cur.fetchall()
    for row in rows:
        todo = Todo(row[0],row[1],row[2],row[3],row[4])
        print(todo)
        todo_list.append(todo)
    return render_template("to_do_list.html", to_do_list=todo_list)
@app.route("/edit/<int:id>")
def edit_task(id):
    connection = createconnection()
    cur = connection.cursor()
    cur.execute(
        "select * from to_do_list where id = ? ",(str(id), ))
    row = cur.fetchone()
    todo=Todo(row[0],row[1],row[2],row[3],row[4])

    print(row)
    print(id)
    return render_template("editpage.html", todo=todo)
@app.route("/remove/<int:id>")
def remove(id):
    connection = createconnection()
    cur = connection.cursor()
    cur.execute("delete from to_do_list where id = ? ",(str(id),))
    print(id)
    connection.commit()
    connection = createconnection()
    cur = connection.cursor()
    cur.execute("select * from to_do_list")
    rows = cur.fetchall()
    print("rows",rows)
    return render_template("to_do_list.html", to_do_list=rows)

@app.route("/delete/<int:id>")
def delete(id): 
    connection = createconnection()
    cur = connection.cursor()
    cur.execute("select * from to_do_list where id = ? ",(str(id),))
    row = cur.fetchone()
    print(row)
    print(id)
    return render_template("delete.html", aTask=row) 
@app.route("/view/<int:id>")
def view_task(id):
    connection = createconnection()
    cur = connection.cursor()
    cur.execute("select * from to_do_list where id = ? ",(str(id),))
    row = cur.fetchone()
    print(row)
    print(id)
    return render_template("viewpage.html", aTask=row) 
@app.route("/update",methods=["post"])
def update(id):
    id=request.form["id"]
    print(id)
    task=request.form["task"]
    due_date=request.form["due_date"]
    note=request.form["note"]
    status=request.form["status"]
    print(task,due_date,note,status)
    connection=createconnection()
    cursor=connection.cursor()
    cursor.execute("UPDATE to_do_list SET task = ?,due_date = ?,note = ?,status=? WHERE id = ?",(task,due_date,note,status,id))
    connection.commit()
    # connection = createconnection()
    # cur = connection.cursor()
    # cur.execute("select * from to_do_list")
    # rows = cur.fetchall()
    # print("rows",rows)
    # return render_template("to_do_list.html", to_do_list=rows)
    return redirect("to_do_list")    




