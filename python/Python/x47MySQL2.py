from mysql.connector import connect,Error
try:
    with connect(host="127.0.0.1",user="root",password="1363",database="dbTest") as db:
        myCursor=db.cursor()
        q1="""Create Table T_Person(
                    PersonId int Primary key,
                    name VarChar(20),
                    Family VarChar(30),
                    Age Int,
                    Avg Decimal(4, 2))
        """
        myCursor.execute(q1)
        db.commit()
        
except Error as error:
    print(error)