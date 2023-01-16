Use master

Create Database dbTest2

Create Database dbTest3
	on (Name='MyDatabase',FileName='F:\Database\MyDatabase.mdf',SIZE=8MB)
	Log on (Name='MyDatabase_Log',FileName='F:\Database\MyDatabase_Log.ldf',SIZE=4MB)
-----------------------------------------------------------------------------------------------

Drop database dbTest2
-----------------------------------------------------------------------------------------------
Use dbTest
GO
Create Schema MySchema2
GO
Drop Schema MySchema2
GO
Alter Schema MySchema Transfer dbo.Users
GO
Alter Schema dbo Transfer MySchema.Users
GO
Drop Schema MySchema
--------------------------------------------------------------------------------------------------

Create Database dbTest2
GO
Use dbTest2
GO
Create Table States(
	StateCode Tinyint Primary Key NOT NULL,
	StateName NVarChar(30) NOT NULL
)

GO

Create Table Cities(
	CityCode Int Primary Key NOT NULL Identity(1000,5),
	CityName NVarChar(30) NOT NULL,
	StateId Tinyint NOT NULL,
	Foreign Key(StateId) References States(StateCode) 
)

----------------------------------------------------------
Drop Database dbTest3
----------------------------------------------------------
Create Database dbTest3
GO
Use dbTest3
GO
Create Table States(
	StateCode Tinyint Primary Key NOT NULL,
	StateName NVarChar(30) NOT NULL
)

GO

Create Table Cities(
	CityCode Int Primary Key NOT NULL Identity(1000,5),
	CityName NVarChar(30) NOT NULL,
	StateId Tinyint NOT NULL,
	Constraint FK_Cities_StateId Foreign Key(StateId) References States(StateCode) 
)

----------------------------------------------------------
Create Database dbTest4
GO
Use dbTest4
GO
Create Table States(
	StateCode Tinyint Primary Key NOT NULL,
	StateName NVarChar(30) NOT NULL
)

GO

Create Table Cities(
	CityCode Int Primary Key NOT NULL Identity(1000,5),
	CityName NVarChar(30) NOT NULL,
	StateId Tinyint NULL,
	Constraint FK_Cities_StateId Foreign Key(StateId) References States(StateCode) 
	on Delete Cascade
	on Update set NULL
)
----------------------------------------------------------
Create Database dbTest5
GO
Use dbTest5
GO
Create Table States(
	StateCode Tinyint Primary Key NOT NULL,
	StateName NVarChar(30) NOT NULL,
	Constraint unique_state_name Unique(StateName)
)

GO

Create Table Cities(
	CityCode Int Primary Key NOT NULL Identity(1000,5),
	CityName NVarChar(30) NOT NULL,
	StateId Tinyint NULL,
	Constraint FK_Cities_StateId Foreign Key(StateId) References States(StateCode) 
	on Delete Cascade
	on Update set NULL
)

----------------------------------------------------------
Create Database dbTest6
GO
Use dbTest6
GO
Create Table States(
	StateCode Tinyint Primary Key NOT NULL,
	StateName NVarChar(30) NOT NULL,
	Constraint unique_state_name Unique(StateName),
	Constraint CK_StateCode Check(1<=[StateCode] ANd [StateCode]<=40)
)

GO

Create Table Cities(
	CityCode Int Primary Key NOT NULL Identity(1000,5),
	CityName NVarChar(30) NOT NULL,
	StateId Tinyint NULL,
	Constraint FK_Cities_StateId Foreign Key(StateId) References States(StateCode) 
	on Delete Cascade
	on Update set NULL
)
