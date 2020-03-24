# DROP TABLES
# Write queries to drop each table, please don't change variable names,
# You should write respective queries against each varibale

Videoplay_table_drop = "DROP TABLE IF EXISTS Videoplay_fact"
Users_table_drop = ""
Videos_table_drop = ""
Youtubers_table_drop = ""
Time_table_drop = ""

# CREATE TABLES
# Write queries to create each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_create = ("""
""")

Users_table_create = ("""
""")

Videos_table_create = ("""
""")


Youtubers_table_create = ("""
""")

Time_table_create = ("""
""")

# INSERT RECORDS
# Write queries to insert record to each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_insert = ("""
""")

Users_table_insert = ("""
""")

Videos_table_insert = ("""
""")

Youtubers_table_insert = ("""
""")


Time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [Users_table_create, Time_table_create, Youtubers_table_create, Videos_table_create, Videoplay_table_create]
drop_table_queries = [Videoplay_table_drop, Users_table_drop, Videos_table_drop, Youtubers_table_drop, Time_table_drop]
