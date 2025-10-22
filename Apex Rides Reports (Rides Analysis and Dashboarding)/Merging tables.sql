--#Using the Database
Use TestDB;
--Creating a new table with all the datatpe and Column names to insert the data
CREATE TABLE all_table (
rideable_type	nvarchar(50),
started_at_date	date,
started_at_time	time(0),
Time_frame_started_at time(0),
ended_at_date	date,
ended_at_time	time(0),
ride_length_mins	float,
day_of_week	nvarchar(50), 
start_station_name	nvarchar(MAX),
end_station_name	nvarchar(MAX),
member_casual	nvarchar(50)
);
--Inserting the data from all the tables so that we have all data in one file
Insert into all_table
select * from [dbo].[202404-divvy-tripdata]
Union all
select * from [dbo].[202405-divvy-tripdata]
Union all
select * from [dbo].[202406-divvy-tripdata]
Union all
select * from [dbo].[202407-divvy-tripdata]
Union all
select * from [dbo].[202408-divvy-tripdata]
Union all
select * from [dbo].[202409-divvy-tripdata]
Union all
select * from [dbo].[202410-divvy-tripdata]
Union all
select * from [dbo].[202411-divvy-tripdata]
Union all
select * from [dbo].[202412-divvy-tripdata]
Union all
select * from [dbo].[202501-divvy-tripdata]
Union all
select * from [dbo].[202502-divvy-tripdata]
Union all
select * from [dbo].[202503-divvy-tripdata]

select * from [dbo].[all_table]