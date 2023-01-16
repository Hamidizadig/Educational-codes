from mysql.connector import connect,Error
try:
    with connect(host="127.0.0.1",user="root",password="1363",database="dbtest") as db:
        myCursor=db.cursor()

        # myCursor.execute("Insert INTO T_Person(PersonId, Name, Family, Age, Avg) Values(6, 'Sumix', 'shots', 10, 18.29)")
        # id=int(input("Enter Id : "))
        # name=input("Enter Name : ")
        # family=input("Enter Family : ")
        # age=int(input("Enter Age : "))
        # avg=float(input("Enter Avg : "))    
        # myCursor.execute(f"Insert INTO T_Person(PersonId, Name, Family, Age, Avg) Values({id}, '{name}', '{family}', {age}, {avg})")
        
        # id=int(input("Enter Id : "))
        # name=input("Enter Name : ")
        # family=input("Enter Family : ")
        # age=int(input("Enter Age : "))
        # avg=float(input("Enter Avg : "))
        # val=(id,name,family,age,avg)   
        # myCursor.execute("Insert INTO T_Person(PersonId, Name, Family, Age, Avg) Values(%s,%s,%s,%s,%s)",val)
        
        val=[(10,'slix','posmix',20,3.44),(14,'spax','kospxus',33,2.84)]  
        myCursor.executemany("Insert INTO T_Person(PersonId, Name, Family, Age, Avg) Values(%s,%s,%s,%s,%s)",val)
        db.commit()
except Error as error:
    print(error)