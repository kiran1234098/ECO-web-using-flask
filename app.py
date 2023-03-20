from flask import Flask, render_template, request,jsonify
import pymongo
from flaskext.mysql import MySQL
# import mysql.connector
#import mysql.connector
import requests
app=Flask(__name__)

car = app.config(
  host="localhost",
  user="abc",
  password="password"
)

cur = car.cursor()
cur.execute("create database practice")





client = pymongo.MongoClient("mongodb+srv://kiran:abcdef_kiran@cluster0.zmkp9hd.mongodb.net/?retryWrites=true&w=majority")
                
db = client['eccommerce']
                    
review_col = db['web']
data={"name":"Prakash","email":"gautamprakash@gmail.com","class":99}
data1={"name":"bitti","address":"betul","class":"first"}
review_col.insert_one(data)
review_col.insert_one(data1)

                    




#app=Flask(__name__)

'''app.config['host']="https://green-baker-agntn.ineuron.app/?folder=/config/workspace",
app.config['user']="abc",
app.config['password']="password"
app.config['db']="practice"
mysql = MySQL()
mysql.init_app(app)
cursor = mysql.get_db().cursor()
'''

@app.route("/",methods=['GET'])
def HomePage():
    result=5000
    cur.execute("insert into practice2 values(3,'pooja',30,'usa')")
    car.commit()
    return render_template("index.html",result=result)


@app.route("/electronic",methods=['GET'])
def electronic():
    return render_template("electronic.html")

@app.route("/fashion",methods=['GET'])
def fashion():
    return render_template("fashion.html")

@app.route("/jewellery",methods=['GET'])
def jewellery():
    return render_template("jewellery.html")

@app.route("/aboutus",methods=['GET'])
def aboutus():
    return "i am"



if __name__ == "__main__":
     app.run(host="0.0.0.0") 


