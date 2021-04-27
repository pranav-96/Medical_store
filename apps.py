from flask import Flask, render_template, request, redirect
import pymysql

apps = Flask(__name__)

@apps.route('/')

def info():
     
    return render_template('info.html')
    
@apps.route('/insert', methods=["POST","GET"])

def insert():
     
     c = request.form['c']
     n = request.form['n']
     p = request.form['p']
     s = request.form['s']
     d = request.form['d']
     dt = request.form['dt']
     
     servername = "localhost"
     username = "root"
     password = ""
     dbname = "mytodolist"
     
     try:
         db = pymysql.connect(servername,username,password,dbname)
         cu = db.cursor()
         
         sql = "insert into data(code,med_name,price,stock,description,date)values('{}','{}','{}','{}','{}','{}')".format(c,n,p,s,d,dt)
         
         cu.execute(sql)
         db.commit()
         
         return redirect('/dashboard1')
         
     except Exception:
     
         db.rollback()
     
         return "Error"
         
@apps.route('/dashboard1')

def display():

     servername = "localhost"
     username = "root"
     password = ""
     dbname = "mytodolist"
     
     try:
     
         db = pymysql.connect(servername,username,password,dbname)
         cu = db.cursor()
         
         sql = "select * from data"
         
         cu.execute(sql)
         data = cu.fetchall()
         
         return render_template('dashboard1.html',d = data)
         
     except Exception:
         
         db.rollback()
         return "error in connection"
         
@apps.route('/delete/<code>')

def delete(code):

     servername = "localhost"
     username = "root"
     password = ""
     dbname = "mytodolist"
     
     try:
     
         db = pymysql.connect(servername,username,password,dbname)
         cu = db.cursor()
         
         sql = "delete from data where code={}".format(code)
         
         cu.execute(sql)
         db.commit()
         
         return redirect('/dashboard1')
         
     except Exception:
         
         db.rollback()
         return "error in try block"
         
@apps.route('/edit/<code>')

def edit(code):

     servername = "localhost"
     username = "root"
     password = ""
     dbname = "mytodolist"
     
     try:
         
         db = pymysql.connect(servername,username,password,dbname)
         cu = db.cursor()
         
         sql = "select * from data where code={}".format(code)
         
         cu.execute(sql)
         data = cu.fetchone()
         
         return render_template('editinfo.html',d = data)
         
     except Exception:
     
         db.rollback()
         return "coneection failed"
         
@apps.route('/update', methods=["POST","GET"])

def update():

     n = request.form['n']
     p = request.form['p']
     s = request.form['s']
     d = request.form['d']
     dt = request.form['dt']
     c = request.form['c']
         
     servername = "localhost"
     username = "root"
     password = ""
     dbname = "mytodolist"
         
     try:
     
         db = pymysql.connect(servername,username,password,dbname)
         cu= db.cursor()
         
         sql = "update data SET med_name='{}',price='{}',stock='{}',description='{}',date='{}' where code={}".format(n,p,s,d,dt,c)
         
         cu.execute(sql)
         db.commit()
         
         return redirect('/dashboard1')
         
     except Exception:
     
         return "Failed"
         
     
apps.debug = True    
apps.run()