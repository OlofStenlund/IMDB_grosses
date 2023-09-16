from create_database_class import MoviesDatabase
import pandas as pd

db = MoviesDatabase("Movies_Database.db")

create_table = """
CREATE TABLE IF NOT EXISTS Movies
(   id INTEGER PRIMARY KEY AUTOINCREMENT,
    Rank INTEGER,
    Title TEXT,
    Lifetime_Gross INTEGER,
    Year INTEGER,
    Movie_id TEXT,
    Image TEXT, 
    Director TEXT
)
"""

create_directors_table = """
CREATE TABLE IF NOT EXISTS Directors
(   id INTEGER PRIMARY KEY AUTOINCREMENT,
    director_id TEXT,
    director_name TEXT
)
"""

insert_movie = """
INSERT INTO Movies
(  
    Rank,
    Title,
    Lifetime_Gross,
    Year,
    Movie_id,
    Image,
    Director
) 
VALUES 
(
    ?, ?, ?, ?, ?, ?, ?
)
"""

update_movie = """
    UPDATE Movies
    SET Image = ?, Director = ?
    WHERE Movie_id = ?
    """

insert_director = """
INSERT INTO Directors
(
    director_id, 
    director_name
)
VALUES
(
    ?, ?
)
"""

look_for_duplicates = """
SELECT * FROM Directors WHERE director_name = ?
"""

replace_none_image_column = """
UPDATE Movies
SET Image = '0'
WHERE Image IS NULL
"""

return_duplicates = """
SELECT * FROM Directors
WHERE id NOT IN (
    SELECT MIN (id)
    FROM Directors
    GROUP BY director_id
    )
"""


delete_duplicates = """
DELETE FROM Directors
WHERE id NOT IN (
    SELECT MIN (id)
    FROM Directors
    GROUP BY director_id
    )
"""

get_movies = """
SELECT * FROM Movies
"""

get_directors = """
SELECT * FROM Directors
"""

get_missing_director_names = """
SELECT * FROM Movies WHERE Director = 0
"""

insert_missing_director = """
UPDATE Movies
SET Director = ?
WHERE Title = ?
"""

