from mysql.connector import connect,Error
try:
    with connect(host="127.0.0.1",user="root",password="1363",database="dbtest") as db:
        myCursor=db.cursor()
        
        
        # myCursor.execute("delete from t_person where personid=6")
        # db.commit()
        
        id=int(input("Enter Id for delete :"))
        myCursor.execute("delete from t_person where personid="+str(id))
        db.commit()
        
except Error as error:
    print(error)