# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS times;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays(
    songplay_id     integer SERIAL PRIMARY KEY,
    start_time      integer,
    user_id         integer,
    level           text,
    song_id         text,
    artist_id       text,
    session_id      integer,
    location        text,
    user_agent      text
);
""")

user_table_create = ("""
CREATE TABLE users(
    user_id         integer PRIMARY KEY,
    first_name      text,
    last_name       text,
    gender          text,
    level           text
);
""")

song_table_create = ("""
CREATE TABLE songs(
    song_id         text PRIMARY KEY,
    title           text,
    artist_id       text,
    year            integer,
    duration        numeric
);
""")

artist_table_create = ("""
CREATE TABLE artists(
    artist_id       text PRIMARY KEY,
    name            text,
    location        text,
    latitude        float8,
    longitude       float8
);
""")

time_table_create = ("""
CREATE TABLE times(
    start_time      bigint PRIMARY KEY,
    hour            integer NOT NULL,
    day             integer NOT NULL,
    week            integer NOT NULL,
    month           integer NOT NULL,
    year            integer NOT NULL,
    weekday         text NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT INTO times (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT (song_id, artists.artist_id) 
FROM songs
INNER JOIN artists ON songs.artist_id=artists.artist_id
WHERE title=%s AND name=%s AND duration=%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
