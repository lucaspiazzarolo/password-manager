import mysql.connector
import functions as f

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root", #this password may be different, depending on your MySQL installation
)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE passwords") #creates the "passwords" database