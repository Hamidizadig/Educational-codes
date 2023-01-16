from t_person
from t_Person
from ast import Delete
from socket import if_indextoname
from tokenize import Name


Create Database dbTest
------------------------
Person:
    PersonId
    Name
    family
    age
    Avg

Create Table T_Person(
    PersonId int Primary key,
    name VarChar(20),
    Family VarChar(30),
    Age Int,
    Avg Decimal(4, 2)
)
---------------------------------------------
Insert INTO T_Person(PersonId, Name, Family, Age, Avg) Values(1, 'Sumix', 'shots', 10, 18.29)
Insert Into T_Person(PersonId, Name, Family, Age, Avg) Values(2, 'sasham', 'smars', 31, 17.09)
---------------------------------------------
Select PersonId, Name, Family, Age, Avg
From T_Person

Select*
From T_Person

Select Name, Family
From T_Person
where Age > 30
--------------------------------------------
Update T_Person
set Name = 'sayus' Id = 80, Where PersonId = 1
----------
update t_person
set Age = 25
where PersonId = 1
--------------------------------------------
delete
where personId = 1

select *
---------------------------------------------
select *
--------------------------------------------
Deletefrome T_Person, Where PersonId = 1

******************************************
