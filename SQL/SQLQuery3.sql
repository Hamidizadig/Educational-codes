Use dbTest
Go
Create Table PeopleGroup(
	PeopleGroupeID tinyint PRIMARY KEY NOT NULL,
	PeopleGroupTitle NVarChar(30) NOT NULL
	)
GO
Insert INTO PeopleGroup(PeopleGroupId,PeopleGroupTitle)
					Values(1,N'st'),
							(2,N'eng'),
							(3,N'doc'),
							(4,N'ar'),
							(5,N'an'),
							(6,N'ne'),
							(7,N'ku')
---------------------------------------------------------
Create Table People(
	PersonId int IDENTITY(1,1) NOT NULL,
	[Name] nvarchar(30) NOT NULL,
	Family nvarchar(30) NOT NULL,
	Age Tinyint NULL,
	[Avg] decimal(4,2) NULL,
	PhoneNumber char(115) NULL,
	[PeopleGroupId] tinyint NULL,
	CONSTRAINT PK_People PRIMARY KEY(PersonId),
	CONSTRAINT FK_People_PersonId Foreign Key(PeopleGroupId) References PeopleGroup(PeopleGroupId)
)
Go
Insert Into People
			Values('mas','sad',22,17.25,'021-00000000',1),
				('ads','sop',29,12.52,'022-00000000',2),
				('hix','far',19,11.88,'033-00000000',3),
				('max','wem',45,19.04,'044-00000000',2),
				('poy','kox',19,17.39,'019-00000000',2),
				('sha','ris',26,15.00,'055-00000000',6)
---------------------------------------------------------
select * 
from People
GO
select *
from People
where Age>25
GO
select *
from People
where [Name]='hix'
GO
select *
from People
where [Name]='max' AND Age<20

select *
from People
where [Name]='sha' OR [Family]='kox' OR [Avg]>19

select *
from People
where [Name]='poy' OR [Name]='ads' OR [Name]='max'

select *
from People
where [Name] IN('mas','hix','hix')

select *
from People
where [Age] IN(12,13,44,45,19,87,45)

select *
from People
where 30<=[Age] AND [AGE]<=40

select *
from People
where [Age] Between 30 AND 40
