Use TestDB

Select *, 
Case 
	when ride_length_mins >=0 AND ride_length_mins <2 THEN 'Quick Spin'
	when ride_length_mins >=2 AND ride_length_mins <10 THEN 'Short Ride'
	when ride_length_mins >=10 AND ride_length_mins <20 THEN 'Medium Journey'
	when ride_length_mins >=20 AND ride_length_mins <40 THEN 'Extended Trip'
	Else ' Long Haul'
End As Ride_Category

from dbo.all_table