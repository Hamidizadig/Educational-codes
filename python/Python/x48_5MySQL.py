from mysql.connector import connect,Error
try:
    with connect(host="127.0.0.1",user="root",password="1363",database="dbtest") as db:
        myCursor=db.cursor()

        q1="""update t_person
            set avg=avg+1
            where age<25"""
        myCursor.execute(q1)
        
        db.commit()
except Error as error:
    print(error)