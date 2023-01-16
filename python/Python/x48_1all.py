from mysql.connector import connect,Error
try:
    with connect(host="127.0.0.1",user="root",password="1363",database="dbTest") as db:
        myCursor=db.cursor()

        
except Error as error:
    print(error)