import mysql.connector

def db_connect2():
    global mydb,mycursor
    mydb = mysql.connector.connect(
    host="localhost",
    user="hariff",
    password="hariff123",
    database="speed_sensor"
    )
    mycursor = mydb.cursor()

def your_query(masuk):
    print("Insert to DB")
    sql = "INSERT INTO data (speed, time) VALUES (%d, NOW())" % masuk
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

