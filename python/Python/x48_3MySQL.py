from mysql.connector import connect,Error
try:
    with connect(host="127.0.0.1",user="root",password="1363",database="dbtest") as db:
        myCursor=db.cursor()

        # myCursor.execute("Select * From T_Person") 
        # people=myCursor.fetchall()
        # for person in people:
        #     print(f"name : {person[1]}\tfamily : {person[2]}")
        
        age1=int(input("Enter Age : "))
        myCursor.execute(f"Select * From T_Person where age<{age1}") 
        people=myCursor.fetchall()
        for person in people:
            print(f"name : {person[1]}\tfamily : {person[2]}")

except Error as error:
    print(error)