Провел миграцию бд:

`
(venv) avtrokhachev@i106040781 migrations-db-7-hw % alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 55c9a1bfc192, create tables
`

Логи запуска
`
/Users/avtrokhachev/PycharmProjects/migrations-db-7-hw/venv/bin/python /Users/avtrokhachev/PycharmProjects/migrations-db-7-hw/main.py 
2024-10-19 17:55:29,039 INFO sqlalchemy.engine.Engine select pg_catalog.version()
2024-10-19 17:55:29,039 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-10-19 17:55:29,040 INFO sqlalchemy.engine.Engine select current_schema()
2024-10-19 17:55:29,040 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-10-19 17:55:29,041 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2024-10-19 17:55:29,041 INFO sqlalchemy.engine.Engine [raw sql] {}
2024-10-19 17:55:29,042 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,043 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Thomas Washington', 'BN', 56, 38000)
2024-10-19 17:55:29,043 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,044 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,045 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,046 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Michael Ramirez', '516840', 'BN', '1998-10-05')
2024-10-19 17:55:29,046 INFO sqlalchemy.engine.Engine [generated in 0.00019s] {}
2024-10-19 17:55:29,047 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,048 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,048 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Carolyn Wolfe', '184308', 'BN', '1999-03-20')
2024-10-19 17:55:29,048 INFO sqlalchemy.engine.Engine [generated in 0.00017s] {}
2024-10-19 17:55:29,049 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,050 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,050 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Steven Rodriguez', '260094', 'BN', '1977-08-28')
2024-10-19 17:55:29,050 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,051 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,051 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,052 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('949488', 'BN', 'South Alexis', 2022, '01-01-2022', '05-05-2022')
2024-10-19 17:55:29,052 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,053 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,053 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,054 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('396588', 'James Hall', 'eventType', '949488', 0, 3, 'bookResult')
2024-10-19 17:55:29,054 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {}
2024-10-19 17:55:29,055 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,056 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,056 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('396588', '516840', 'GOLD', 74.0)
2024-10-19 17:55:29,056 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,057 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,058 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,058 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('396588', '184308', 'BRONZE', 76.0)
2024-10-19 17:55:29,058 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,058 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,059 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,059 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('396588', '260094', 'GOLD', 0.0)
2024-10-19 17:55:29,059 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,059 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,060 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,060 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Charlene Houston', 'TM', 67, 34098)
2024-10-19 17:55:29,060 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,061 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,061 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,062 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Carolyn Glenn', '345722', 'TM', '2003-01-02')
2024-10-19 17:55:29,062 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,062 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,063 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,063 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Alexander King', '701228', 'BN', '1996-08-22')
2024-10-19 17:55:29,063 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,064 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,064 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,065 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Fernando Moore', '412079', 'BN', '1983-06-14')
2024-10-19 17:55:29,065 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,065 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,066 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,066 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('451608', 'BN', 'Sherriside', 2010, '01-01-2010', '05-05-2010')
2024-10-19 17:55:29,066 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,066 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,067 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,067 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('411324', 'Lindsey Lane', 'eventType', '451608', 0, 3, 'bookResult')
2024-10-19 17:55:29,067 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,068 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,068 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,069 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('411324', '345722', 'GOLD', 45.0)
2024-10-19 17:55:29,069 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,069 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,069 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,070 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('411324', '701228', 'None', 60.0)
2024-10-19 17:55:29,070 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,070 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,070 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,071 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('411324', '412079', 'GOLD', 47.0)
2024-10-19 17:55:29,071 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,071 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,072 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,072 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Dennis Hall', 'PG', 55, 5763)
2024-10-19 17:55:29,072 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,072 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,073 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,073 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Daniel Taylor', '603809', 'PG', '1993-12-31')
2024-10-19 17:55:29,073 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,074 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,074 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,075 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Jennifer Estes', '643649', 'PG', '1974-12-24')
2024-10-19 17:55:29,075 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,075 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,076 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,076 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Jonathan Greene', '317483', 'BN', '1983-09-29')
2024-10-19 17:55:29,076 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,077 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,077 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,077 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('300941', 'BN', 'Riveraland', 2010, '01-01-2010', '05-05-2010')
2024-10-19 17:55:29,077 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,078 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,079 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,079 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('382518', 'Nathan Cook', 'eventType', '300941', 0, 3, 'bookResult')
2024-10-19 17:55:29,079 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,080 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,080 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,080 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('382518', '603809', 'None', 95.0)
2024-10-19 17:55:29,080 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,081 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,081 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,081 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('382518', '643649', 'None', 9.0)
2024-10-19 17:55:29,081 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,082 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,082 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,082 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('382518', '317483', 'None', 44.0)
2024-10-19 17:55:29,082 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,083 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,083 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,084 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Ashley Smith', 'GY', 27, 29441)
2024-10-19 17:55:29,084 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,084 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,084 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,085 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Joseph Thomas', 'CM', 59, 37770)
2024-10-19 17:55:29,085 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,085 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,086 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,086 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Joshua Daniels', 'DM', 69, 87777)
2024-10-19 17:55:29,086 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,087 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,087 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,087 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Austin Davis', 'ES', 33, 52178)
2024-10-19 17:55:29,088 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,088 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,089 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,089 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Christian Garcia', 'PS', 80, 44138)
2024-10-19 17:55:29,089 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,090 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,090 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,090 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Mark Garza', '947842', 'BN', '2022-01-27')
2024-10-19 17:55:29,091 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,091 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,091 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,092 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('William Decker', '506065', 'BN', '1975-06-08')
2024-10-19 17:55:29,092 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,092 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,093 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,093 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Christine Johnson', '533119', 'ES', '1998-09-05')
2024-10-19 17:55:29,093 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,093 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,094 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,094 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Jennifer Church', '725892', 'BN', '2011-04-04')
2024-10-19 17:55:29,094 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,095 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,095 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,096 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Chris Anderson', '855209', 'PS', '1974-01-03')
2024-10-19 17:55:29,096 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,096 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,097 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,097 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Rodney James', '691531', 'DM', '1986-12-27')
2024-10-19 17:55:29,097 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,098 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,098 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,098 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Claudia Holmes', '579504', 'CM', '2013-07-22')
2024-10-19 17:55:29,099 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,099 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,099 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,100 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Taylor Eaton', '117774', 'DM', '1987-11-17')
2024-10-19 17:55:29,100 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,100 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,101 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,101 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Robert Singh PhD', '762159', 'TM', '2002-09-23')
2024-10-19 17:55:29,101 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {}
2024-10-19 17:55:29,102 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,102 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,103 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Sarah Hill', '699204', 'BN', '1995-12-03')
2024-10-19 17:55:29,103 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,103 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,103 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,104 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('917205', 'CM', 'New Amanda', 2013, '01-01-2013', '05-05-2013')
2024-10-19 17:55:29,104 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,104 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,105 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,105 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('875152', 'Lori Mcclure', 'eventType', '917205', 0, 10, 'bookResult')
2024-10-19 17:55:29,105 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,106 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,106 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,106 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '947842', 'SILVER', 65.0)
2024-10-19 17:55:29,106 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,107 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,107 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,107 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '506065', 'SILVER', 80.0)
2024-10-19 17:55:29,107 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {}
2024-10-19 17:55:29,108 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,108 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,108 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '533119', 'GOLD', 46.0)
2024-10-19 17:55:29,108 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,109 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,109 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,109 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '725892', 'None', 28.0)
2024-10-19 17:55:29,109 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {}
2024-10-19 17:55:29,110 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,110 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,110 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '855209', 'SILVER', 10.0)
2024-10-19 17:55:29,110 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {}
2024-10-19 17:55:29,111 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,111 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,111 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '691531', 'SILVER', 93.0)
2024-10-19 17:55:29,111 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,112 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,112 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,112 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '579504', 'None', 50.0)
2024-10-19 17:55:29,112 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,113 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,113 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,114 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '117774', 'GOLD', 63.0)
2024-10-19 17:55:29,114 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,114 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,114 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,115 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '762159', 'None', 2.0)
2024-10-19 17:55:29,115 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,115 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,115 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,116 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('875152', '699204', 'BRONZE', 25.0)
2024-10-19 17:55:29,116 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,116 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,117 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,117 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Jerry Johnson', 'CH', 92, 4364)
2024-10-19 17:55:29,117 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,118 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,118 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,118 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Victoria Friedman', 'AR', 73, 71877)
2024-10-19 17:55:29,118 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,119 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,119 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,120 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Scott Rodriguez', '685156', 'PG', '2012-07-06')
2024-10-19 17:55:29,120 INFO sqlalchemy.engine.Engine [generated in 0.00019s] {}
2024-10-19 17:55:29,121 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,121 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,121 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Joseph Ali', '535294', 'PG', '2009-12-25')
2024-10-19 17:55:29,122 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,122 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,123 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,123 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('John Wiley DDS', '386293', 'PG', '1977-09-26')
2024-10-19 17:55:29,123 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,123 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,124 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,124 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Richard Roberts', '685735', 'DM', '2007-10-29')
2024-10-19 17:55:29,124 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,125 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,125 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,126 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Laura Bowen', '782441', 'TM', '1975-10-06')
2024-10-19 17:55:29,126 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,126 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,127 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,127 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('959630', 'DM', 'Russellland', 2007, '01-01-2007', '05-05-2007')
2024-10-19 17:55:29,127 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,127 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,128 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,128 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('321404', 'Aaron Mathews', 'eventType', '959630', 0, 5, 'bookResult')
2024-10-19 17:55:29,128 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,129 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,129 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,130 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('321404', '685156', 'GOLD', 83.0)
2024-10-19 17:55:29,130 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,130 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,131 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,131 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('321404', '535294', 'SILVER', 79.0)
2024-10-19 17:55:29,131 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,131 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,132 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,132 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('321404', '386293', 'None', 82.0)
2024-10-19 17:55:29,132 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,132 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,133 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,133 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('321404', '685735', 'None', 96.0)
2024-10-19 17:55:29,133 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {}
2024-10-19 17:55:29,133 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,134 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,134 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('321404', '782441', 'BRONZE', 93.0)
2024-10-19 17:55:29,134 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,134 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,135 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,135 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Eric Roberts', 'GH', 86, 59370)
2024-10-19 17:55:29,135 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {}
2024-10-19 17:55:29,135 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,136 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,136 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Dawn Anderson', 'AM', 6, 80470)
2024-10-19 17:55:29,137 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,137 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,138 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,138 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('William Nielsen', 'GR', 21, 13745)
2024-10-19 17:55:29,138 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,138 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,139 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,139 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Marco Barber DDS', 'SG', 76, 10387)
2024-10-19 17:55:29,139 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,140 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,140 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,141 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Joseph Tran', '690690', 'GR', '2019-05-27')
2024-10-19 17:55:29,141 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,141 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,141 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,142 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Zachary Martinez MD', '390700', 'PS', '2015-06-11')
2024-10-19 17:55:29,142 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,142 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,143 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,143 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Miranda Daniels', '857550', 'SG', '2020-03-31')
2024-10-19 17:55:29,143 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,144 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,144 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,145 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Richard Rodriguez', '309017', 'GY', '1981-02-12')
2024-10-19 17:55:29,145 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,145 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,146 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,146 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Zachary Fields', '636348', 'TM', '1977-12-14')
2024-10-19 17:55:29,146 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,147 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,147 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,147 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Amanda Hester', '513824', 'BN', '1998-08-30')
2024-10-19 17:55:29,148 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,148 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,148 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,149 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Samuel Robles', '762232', 'CM', '1979-08-17')
2024-10-19 17:55:29,149 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,149 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,150 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,150 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Melissa Pierce', '443122', 'ES', '1983-11-08')
2024-10-19 17:55:29,150 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,151 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,151 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,151 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Robert Patterson', '764944', 'SG', '1994-02-27')
2024-10-19 17:55:29,152 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,152 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,152 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,153 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('695951', 'BN', 'West John', 2016, '01-01-2016', '05-05-2016')
2024-10-19 17:55:29,153 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,153 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,154 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,154 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('475443', 'Cory Gonzalez', 'eventType', '695951', 0, 9, 'bookResult')
2024-10-19 17:55:29,155 INFO sqlalchemy.engine.Engine [generated in 0.00017s] {}
2024-10-19 17:55:29,155 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,155 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,156 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '690690', 'BRONZE', 37.0)
2024-10-19 17:55:29,156 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,156 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,156 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,157 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '390700', 'None', 76.0)
2024-10-19 17:55:29,157 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,157 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,157 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,158 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '857550', 'GOLD', 67.0)
2024-10-19 17:55:29,158 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,158 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,158 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,159 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '309017', 'SILVER', 14.0)
2024-10-19 17:55:29,159 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,159 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,159 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,160 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '636348', 'BRONZE', 8.0)
2024-10-19 17:55:29,160 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {}
2024-10-19 17:55:29,160 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,161 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,161 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '513824', 'GOLD', 92.0)
2024-10-19 17:55:29,161 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,161 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,162 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,162 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '762232', 'GOLD', 43.0)
2024-10-19 17:55:29,162 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,162 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,163 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,163 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '443122', 'SILVER', 41.0)
2024-10-19 17:55:29,163 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,163 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,164 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,164 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('475443', '764944', 'GOLD', 83.0)
2024-10-19 17:55:29,164 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,164 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,165 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,165 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Christina Galvan', 'AO', 29, 58485)
2024-10-19 17:55:29,165 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,166 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,166 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,166 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Sheila Shepherd', 'CA', 75, 5545)
2024-10-19 17:55:29,166 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,167 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,167 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,168 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Wesley Johnson', 'SV', 63, 34142)
2024-10-19 17:55:29,168 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,168 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,169 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,169 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Cynthia Davis', 'ET', 35, 99065)
2024-10-19 17:55:29,169 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,169 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,170 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,170 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Samantha Soto', '206127', 'ES', '1988-09-07')
2024-10-19 17:55:29,171 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,171 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,171 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,172 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Darren Hall', '656980', 'CM', '1975-08-09')
2024-10-19 17:55:29,172 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,172 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,173 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,173 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('John Simmons', '837546', 'ES', '1999-02-24')
2024-10-19 17:55:29,173 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,174 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,174 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,174 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Natasha Proctor', '251679', 'PG', '2005-04-30')
2024-10-19 17:55:29,174 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,175 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,175 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,176 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Fred Williams', '795927', 'GR', '1989-03-21')
2024-10-19 17:55:29,176 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,176 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,177 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,177 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Sarah Johnson', '668962', 'PS', '1992-12-14')
2024-10-19 17:55:29,177 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,178 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,178 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,179 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Paul Austin', '405771', 'CA', '1971-02-06')
2024-10-19 17:55:29,179 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,179 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,179 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,180 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Elizabeth Melton', '278001', 'ET', '2013-07-02')
2024-10-19 17:55:29,180 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,180 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,181 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,181 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('375637', 'PS', 'Port Kevinburgh', 2011, '01-01-2011', '05-05-2011')
2024-10-19 17:55:29,181 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,182 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,182 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,183 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('909965', 'Jennifer Rodriguez', 'eventType', '375637', 0, 8, 'bookResult')
2024-10-19 17:55:29,183 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,183 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,183 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,184 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('909965', '206127', 'SILVER', 80.0)
2024-10-19 17:55:29,184 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,184 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,184 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,185 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('909965', '656980', 'None', 40.0)
2024-10-19 17:55:29,185 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,185 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,185 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,186 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('909965', '837546', 'SILVER', 8.0)
2024-10-19 17:55:29,186 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,186 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,186 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,187 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('909965', '251679', 'SILVER', 80.0)
2024-10-19 17:55:29,187 INFO sqlalchemy.engine.Engine [generated in 0.00009s] {}
2024-10-19 17:55:29,187 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,187 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,188 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('909965', '795927', 'BRONZE', 84.0)
2024-10-19 17:55:29,188 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,188 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,188 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,189 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('909965', '668962', 'GOLD', 37.0)
2024-10-19 17:55:29,189 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,189 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,189 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,190 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('909965', '405771', 'GOLD', 85.0)
2024-10-19 17:55:29,190 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,190 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,190 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,191 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('909965', '278001', 'None', 67.0)
2024-10-19 17:55:29,191 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,191 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,191 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,192 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Gina Escobar', 'UZ', 25, 39996)
2024-10-19 17:55:29,192 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,192 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,193 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,193 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Marilyn Roberts', 'MA', 77, 62455)
2024-10-19 17:55:29,193 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,193 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,194 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,194 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Amy Harris', 'TJ', 54, 73703)
2024-10-19 17:55:29,194 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,194 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,195 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,195 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Kayla Martin', 'LC', 22, 18562)
2024-10-19 17:55:29,195 INFO sqlalchemy.engine.Engine [generated in 0.00016s] {}
2024-10-19 17:55:29,196 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,197 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,197 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Susan Contreras', '397658', 'GR', '2015-03-30')
2024-10-19 17:55:29,197 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {}
2024-10-19 17:55:29,198 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,198 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,199 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Stephen Wyatt', '452049', 'SG', '2004-09-24')
2024-10-19 17:55:29,199 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,200 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,200 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,201 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Stacey Baldwin', '507087', 'CA', '1985-12-22')
2024-10-19 17:55:29,201 INFO sqlalchemy.engine.Engine [generated in 0.00020s] {}
2024-10-19 17:55:29,202 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,203 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,204 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Donald Huff', '531090', 'CA', '1978-02-07')
2024-10-19 17:55:29,204 INFO sqlalchemy.engine.Engine [generated in 0.00017s] {}
2024-10-19 17:55:29,204 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,205 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,206 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Dillon Boyd', '724352', 'SV', '2008-05-09')
2024-10-19 17:55:29,206 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,206 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,207 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,207 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Andrew Chavez', '729322', 'LC', '1977-10-04')
2024-10-19 17:55:29,207 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,208 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,208 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,209 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Brandon Allen', '860779', 'LC', '2023-11-14')
2024-10-19 17:55:29,209 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,209 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,209 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,210 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Melissa Garner', '678359', 'GR', '2004-12-06')
2024-10-19 17:55:29,210 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,210 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,211 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,211 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('748091', 'MA', 'Johnsonshire', 2018, '01-01-2018', '05-05-2018')
2024-10-19 17:55:29,211 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,212 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,212 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,213 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('419234', 'Randall Cox', 'eventType', '748091', 0, 8, 'bookResult')
2024-10-19 17:55:29,213 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,213 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,213 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,214 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('419234', '397658', 'GOLD', 36.0)
2024-10-19 17:55:29,214 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,214 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,215 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,215 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('419234', '452049', 'None', 76.0)
2024-10-19 17:55:29,215 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,215 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,216 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,216 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('419234', '507087', 'None', 70.0)
2024-10-19 17:55:29,217 INFO sqlalchemy.engine.Engine [generated in 0.00016s] {}
2024-10-19 17:55:29,217 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,218 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,218 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('419234', '531090', 'SILVER', 48.0)
2024-10-19 17:55:29,218 INFO sqlalchemy.engine.Engine [generated in 0.00016s] {}
2024-10-19 17:55:29,218 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,219 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,219 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('419234', '724352', 'SILVER', 46.0)
2024-10-19 17:55:29,219 INFO sqlalchemy.engine.Engine [generated in 0.00017s] {}
2024-10-19 17:55:29,220 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,220 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,221 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('419234', '729322', 'SILVER', 2.0)
2024-10-19 17:55:29,221 INFO sqlalchemy.engine.Engine [generated in 0.00019s] {}
2024-10-19 17:55:29,222 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,222 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,223 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('419234', '860779', 'BRONZE', 62.0)
2024-10-19 17:55:29,223 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,224 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,224 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,224 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('419234', '678359', 'BRONZE', 45.0)
2024-10-19 17:55:29,224 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,225 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,225 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,226 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Janice Garcia', 'TN', 61, 19903)
2024-10-19 17:55:29,226 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,226 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,227 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,227 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Melinda Taylor', 'UG', 12, 57838)
2024-10-19 17:55:29,227 INFO sqlalchemy.engine.Engine [generated in 0.00016s] {}
2024-10-19 17:55:29,228 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,228 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,229 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Lisa Powell', 'EE', 43, 22365)
2024-10-19 17:55:29,229 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,229 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,230 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,230 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Jill Hunt', 'TZ', 37, 46080)
2024-10-19 17:55:29,230 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,231 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,231 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,232 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Paul Turner', '451732', 'CH', '1974-02-04')
2024-10-19 17:55:29,232 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,232 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,233 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,233 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Adrian Perry', '246774', 'TJ', '2000-10-28')
2024-10-19 17:55:29,233 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,234 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,234 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,235 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Danny Shelton', '807572', 'CA', '1993-04-04')
2024-10-19 17:55:29,235 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,235 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,236 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,236 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Robin Brown', '807415', 'EE', '1971-10-05')
2024-10-19 17:55:29,236 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,236 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,237 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,237 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Lindsay Morris', '518598', 'EE', '1972-08-03')
2024-10-19 17:55:29,237 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {}
2024-10-19 17:55:29,238 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,238 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,239 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Thomas Chan', '134842', 'CH', '2015-12-24')
2024-10-19 17:55:29,239 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,239 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,240 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,240 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('David Hernandez', '124640', 'CA', '1998-10-22')
2024-10-19 17:55:29,240 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,240 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,241 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,241 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Amy Floyd', '967000', 'MA', '1981-08-09')
2024-10-19 17:55:29,241 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
2024-10-19 17:55:29,242 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,242 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,243 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('853953', 'MA', 'North Robertberg', 2021, '01-01-2021', '05-05-2021')
2024-10-19 17:55:29,243 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,243 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,244 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,244 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('203661', 'Darren Taylor', 'eventType', '853953', 0, 8, 'bookResult')
2024-10-19 17:55:29,244 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,245 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,245 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,245 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('203661', '451732', 'SILVER', 65.0)
2024-10-19 17:55:29,245 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,246 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,246 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,246 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('203661', '246774', 'GOLD', 3.0)
2024-10-19 17:55:29,247 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,247 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,247 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,248 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('203661', '807572', 'SILVER', 36.0)
2024-10-19 17:55:29,248 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,248 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,249 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,249 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('203661', '807415', 'GOLD', 95.0)
2024-10-19 17:55:29,249 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
2024-10-19 17:55:29,249 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,250 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,250 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('203661', '518598', 'BRONZE', 65.0)
2024-10-19 17:55:29,250 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,250 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,251 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,251 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('203661', '134842', 'GOLD', 87.0)
2024-10-19 17:55:29,251 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,252 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,252 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,253 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('203661', '124640', 'None', 80.0)
2024-10-19 17:55:29,253 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {}
2024-10-19 17:55:29,253 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,255 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,255 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('203661', '967000', 'None', 66.0)
2024-10-19 17:55:29,255 INFO sqlalchemy.engine.Engine [generated in 0.00018s] {}
2024-10-19 17:55:29,256 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,257 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,257 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Dr. William Lopez', 'ZA', 41, 80280)
2024-10-19 17:55:29,257 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,258 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,259 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,259 INFO sqlalchemy.engine.Engine INSERT INTO countries (name, country_id, area_sqkm, population) VALUES ('Ivan Moore', 'KZ', 44, 21223)
2024-10-19 17:55:29,259 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,260 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,260 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,261 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Madison Herrera', '334120', 'ZA', '2000-03-09')
2024-10-19 17:55:29,261 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {}
2024-10-19 17:55:29,262 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,262 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,263 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Charles Diaz', '588173', 'AM', '2023-09-29')
2024-10-19 17:55:29,263 INFO sqlalchemy.engine.Engine [generated in 0.00016s] {}
2024-10-19 17:55:29,264 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,264 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,265 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Isabel Johnson', '131764', 'CH', '2016-02-15')
2024-10-19 17:55:29,265 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {}
2024-10-19 17:55:29,266 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,267 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,267 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Carol Byrd', '268572', 'CM', '1999-08-19')
2024-10-19 17:55:29,267 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,268 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,268 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,269 INFO sqlalchemy.engine.Engine INSERT INTO players (name, player_id, country_id, birthdate) VALUES ('Eric Singh', '296494', 'CA', '1984-01-17')
2024-10-19 17:55:29,269 INFO sqlalchemy.engine.Engine [generated in 0.00013s] {}
2024-10-19 17:55:29,270 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,270 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,271 INFO sqlalchemy.engine.Engine INSERT INTO olympics (olympic_id, country_id, city, year, startdate, enddate) VALUES ('239958', 'CA', 'Welchborough', 2005, '01-01-2005', '05-05-2005')
2024-10-19 17:55:29,271 INFO sqlalchemy.engine.Engine [generated in 0.00027s] {}
2024-10-19 17:55:29,272 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,273 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,274 INFO sqlalchemy.engine.Engine INSERT INTO events (event_id, name, eventtype, olympic_id, is_team_event, num_players_in_team, result_noted_in) VALUES ('465276', 'Amber Costa', 'eventType', '239958', 0, 5, 'bookResult')
2024-10-19 17:55:29,274 INFO sqlalchemy.engine.Engine [generated in 0.00017s] {}
2024-10-19 17:55:29,274 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,275 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,275 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('465276', '334120', 'GOLD', 54.0)
2024-10-19 17:55:29,276 INFO sqlalchemy.engine.Engine [generated in 0.00019s] {}
2024-10-19 17:55:29,276 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,277 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,277 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('465276', '588173', 'GOLD', 64.0)
2024-10-19 17:55:29,277 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {}
2024-10-19 17:55:29,278 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,278 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,278 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('465276', '131764', 'GOLD', 59.0)
2024-10-19 17:55:29,279 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,279 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,280 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,281 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('465276', '268572', 'BRONZE', 87.0)
2024-10-19 17:55:29,281 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,281 INFO sqlalchemy.engine.Engine COMMIT
2024-10-19 17:55:29,282 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-10-19 17:55:29,282 INFO sqlalchemy.engine.Engine INSERT INTO results (event_id, player_id, medal, result) VALUES ('465276', '296494', 'None', 64.0)
2024-10-19 17:55:29,282 INFO sqlalchemy.engine.Engine [generated in 0.00015s] {}
2024-10-19 17:55:29,283 INFO sqlalchemy.engine.Engine COMMIT`




Задание 1

print(conn.execute(text("""
        SELECT extract(year from birthdate) as year, COUNT(1) as cnt, sum(sum_medals) as sum_medals
        FROM (
            SELECT p.player_id as player_id, p.birthdate as birthdate, COUNT(1) as sum_medals FROM (
                SELECT * FROM
                (
                    SELECT * FROM events e
                    JOIN results r
                    ON e.event_id = r.event_id
                    WHERE medal = 'GOLD'
                ) r
                JOIN olympics o
                ON r.olympic_id = o.olympic_id
                WHERE o.year = 2004
            ) r
            JOIN players p
            ON p.player_id = r.player_id
            GROUP BY p.player_id, p.birthdate
        )
        GROUP BY extract(year from birthdate)
        """)).fetchall())

[(Decimal('1971'), 1, Decimal('1')), (Decimal('1975'), 1, Decimal('1')), (Decimal('1978'), 2, Decimal('2')), (Decimal('1982'), 1, Decimal('1')), (Decimal('1994'), 1, Decimal('1')), (Decimal('1996'), 1, Decimal('1')), (Decimal('1999'), 1, Decimal('1')), (Decimal('2001'), 1, Decimal('1')), (Decimal('2002'), 1, Decimal('1')), (Decimal('2003'), 1, Decimal('1')), (Decimal('2005'), 1, Decimal('1')), (Decimal('2008'), 1, Decimal('1')), (Decimal('2011'), 1, Decimal('1')), (Decimal('2014'), 1, Decimal('1')), (Decimal('2015'), 1, Decimal('1')), (Decimal('2016'), 1, Decimal('1')), (Decimal('2018'), 1, Decimal('1')), (Decimal('2022'), 1, Decimal('1'))]


# 2

SELECT e.event_id as event_id, COUNT(1) as medals_count FROM events e
        JOIN results r
        ON e.event_id = r.event_id
        WHERE r.medal = 'GOLD' and e.is_team_event = 0
        GROUP BY e.event_id
        HAVING COUNT(1) >= 2

[('511602 ', 3), ('634248 ', 2), ('638829 ', 3), ('879837 ', 2), ('885944 ', 2), ('985074 ', 5)]

# 3

SELECT DISTINCT p.player_id FROM players p
        JOIN results r
        ON r.player_id = r.player_id
        WHERE r.medal != 'None'

[('593583    ',), ('725858    ',), ('612732    ',), ('162069    ',), ('773034    ',), ('518919    ',), ('706934    ',), ('487132    ',), ('905190    ',), ('376824    ',), ('856989    ',), ('936359    ',), ('924705    ',), ('712535    ',), ('715425    ',), ('226340    ',), ('495837    ',), ('559479    ',), ('804593    ',), ('534840    ',), ('551821    ',), ('282827    ',), ('761371    ',), ('484366    ',), ('314724    ',), ('418923    ',), ('195973    ',), ('881026    ',), ('451682    ',), ('147606    ',), ('939067    ',), ('419492    ',), ('755929    ',), ('156979    ',), ('883475    ',), ('310634    ',), ('782233    ',), ('396193    ',), ('894876    ',), ('285397    ',), ('415392    ',), ('739728    ',), ('392185    ',), ('267849    ',), ('870834    ',), ('924509    ',), ('694420    ',), ('784385    ',), ('258370    ',), ('641109    ',), ('792054    ',), ('869950    ',), ('152412    ',), ('297283    ',), ('182290    ',), ('443511    ',), ('812370    ',), ('299014    ',), ('861550    ',), ('515179    ',), ('412766    ',), ('269018    ',), ('932378    ',), ('148249    ',), ('744909    ',), ('835502    ',), ('465697    ',), ('739221    ',), ('301991    ',), ('136045    ',), ('801561    ',), ('752747    ',), ('743072    ',)]

# 4

SELECT country_id FROM (
            SELECT p.country_id as country_id, COUNT(1) as cnt FROM players p
            GROUP BY p.country_id
        ) 
        ORDER BY cnt DESC
        LIMIT 1

[('CM ',)]

# 5

SELECT c.country_id, sum(sum_medals) / c.population as koef
        FROM (
            SELECT p.country_id as country_id, COUNT(1) as sum_medals FROM (
                SELECT * FROM
                (
                    SELECT * FROM events e
                    JOIN results r
                    ON e.event_id = r.event_id
                    WHERE medal != 'None'
                ) r
                JOIN olympics o
                ON r.olympic_id = o.olympic_id
                WHERE o.year = 2000
            ) r
            JOIN players p
            ON p.player_id = r.player_id
            GROUP BY p.country_id
        ) r
        JOIN countries c
        ON c.country_id = r.country_id
        GROUP BY c.country_id, c.population
        ORDER BY koef ASC
        LIMIT 5

[('BY ', Decimal('0.000010372475598751153938')), ('MD ', Decimal('0.000010529862690590514700')), ('NA ', Decimal('0.000010743677345881948473')), ('NE ', Decimal('0.000010825556974906358932')), ('IE ', Decimal('0.000012305723391949595757'))]
