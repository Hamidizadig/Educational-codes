Use dbTest2
GO
Insert INTO States([StateCode],[StateName]
				Values(4,N'ااا')
---------------------------------------
Insert INTO States(StateCode,StateName)
			Values(5,N'ß2'),
					(6,N'ß3'),
					(7,N'ß4'),
					(8,N'ß5')
---------------------------------------
Select [StateCode],[StateName]
From States
GO
Select [CityCode],[CityName],[StateId]
From Cities
---------------------------------------
Use dbTest
GO
Select *
From Users
Use dbTest2
GO
select as N'Cod Ostan',CityName as N'Name ß'
From Cities
---------------------------------------
Select *
From Cities
GO
Select Top 3 *
From Cities