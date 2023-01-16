from mysql.connector import connect,Error
try:
    with connect(host="localhost",user="root",password="1363",database="dbtest") as db:
        myCursor=db.cursor()
        myCursor.execute("SHOW DATABASES")
        for database in myCursor:
            print(database)
            
        myCursor.execute("Create Database dbTest2")
        print("database createed....")
except Error as error:
    print(error)