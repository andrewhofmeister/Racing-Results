# Initialize sqlite3 database schema and functions to add/delete entries.
import sqlite3

# Initialize db in RAM for every run of script for developemnt and testing
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE races (
        race_id integer,
        race_date text,
        race_name text
        )""")

c.execute("""CREATE TABLE results (
        race_id integer,
        racer_id integer,
        posistion integer,
        gap real,
        fastest_lap_time real,
        kart_num integer
        )""")

c.execute("""CREATE TABLE racers (
        racer_id integer,
        first_name text,
        last_name text
        )""")

conn.commit()


def insert_race(race):
    pass


def get_results(race):
    pass


def insert_racer(racer):
    pass


def remove_racer(racer):
    pass
