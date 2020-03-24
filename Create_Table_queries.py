# DROP TABLES
# Write queries to drop each table, please don't change variable names,
# You should write respective queries against each varibale

Videoplay_table_drop = "DROP TABLE IF EXISTS Videoplay_fact"
Users_table_drop = "DROP TABLE IF EXISTS Users_dim"
Videos_table_drop = "DROP TABLE IF EXISTS Videos_dim"
Youtubers_table_drop = "DROP TABLE IF EXISTS Youtubers_dim"
Time_table_drop = "DROP TABLE IF EXISTS Time_dim"

# CREATE TABLES
# Write queries to create each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_create = "CREATE TABLE IF NOT EXISTS Videoplay_fact (videoplay_id int, start_time DATE,user_id int, level varchar, video_id varchar,youtuber_id varchar, session_id int, location varchar, user_agent varchar ); "

Users_table_create = "CREATE TABLE IF NOT EXISTS Users_dim (user_id int, first_name varchar,last_name varchar, gender varchar, level varchar); "

Videos_table_create = "CREATE TABLE IF NOT EXISTS Videos_dim (video_id varchar, title varchar,youtuber_id varchar, Year int, duration real);"


Youtubers_table_create = "CREATE TABLE IF NOT EXISTS Youtubers_dim (youtuber_id varchar, name varchar,location varchar, latitude real, longitude real);"

Time_table_create = "CREATE TABLE IF NOT EXISTS Time_dim (start_time DATE, hour int,day int, week int, month int, year int, weekday int);"

# INSERT RECORDS
# Write queries to insert record to each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_insert = "INSERT INTO Videoplay_fact (videoplay_id, start_time ,user_id , level , video_id ,youtuber_id , session_id , location , user_agent) VALUES (%s,%s, %s,%s,%s, %s,%s,%s,%s)"

Users_table_insert = "INSERT INTO Users_dim (user_id , first_name ,last_name , gender , level ) VALUES (%s,%s, %s,%s,%s)"

Videos_table_insert = "INSERT INTO Videos_dim (video_id , title ,youtuber_id , Year , duration) VALUES (%s,%s, %s,%s,%s)"

Youtubers_table_insert = "INSERT INTO Youtubers_dim (youtuber_id , name ,location , latitude , longitude) VALUES (%s,%s, %s,%s,%s)"

Time_table_insert = "INSERT INTO Time_dim (start_time , hour ,day , week , month , year , weekday ) VALUES (%s,%s, %s,%s,%s,%s,%s)"

# QUERY LISTS
create_table_queries = [Users_table_create, Time_table_create, Youtubers_table_create, Videos_table_create, Videoplay_table_create]
drop_table_queries = [Videoplay_table_drop, Users_table_drop, Videos_table_drop, Youtubers_table_drop, Time_table_drop]
