Use dbTest
select * 
from People

select Distinct *
from People

select Distinct [Name]
from People
--------------------------
Select *
from People
where [Name] Like 'max%'

Select *
from People
where [Name] Like '%max'

Select *
from People
where [Name] Like '%max%'

Select *
from People
where [Name] Like '--x'

Select *
from People
where [Name] Like '-a-'

Select *
from People
where [Name] Like '%#%' Escape '#'

Select *
from People
where [Name] Like '%[ax]'

Select *
from People
where [Name] Like '%[d-p]'

Select *
from People
where [Name] Like '%[^m^x]'

Select *
from People
where [Name] Not Like '%max'

Select *
from People
where [Name] Not Like '%[^m^x]'

Select *
from People
where [Name] Not Like '%max%'