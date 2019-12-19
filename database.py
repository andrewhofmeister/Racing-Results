# Initialize sqlite3 database schema and functions to add/delete entries.
import sqlite3
from fetch import getRaces, getLeagueRaces, getRaceInfo
# Initialize db in RAM for every run of script for developemnt and testing
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE races (
        race_id INTEGER,
        race_date TEXT,
        race_name TEXT
        )""")

c.execute("""CREATE TABLE results (
        race_id INTEGER,
        racer_id INTEGER,
        posistion INTEGER,
        gap REAL,
        fastest_lap_time REAL,
        kart_num INTEGER
        )""")

c.execute("""CREATE TABLE racers (
        racer_id INTEGER,
        first_name TEXT,
        last_name TEXT
        )""")

conn.commit()


def insert_race(race):
    with conn:
        c.execute("INSERT INTO races VALUES(:race_id, :race_date, :race_name)",
                  {'race_id': race[0],
                   'race_date': race[1],
                   'race_name': race[2]
                   })


def insert_results(results):
    with conn:
        c.execute("""INSERT INTO results VALUES(
                  : race_id,
                  : racer_id,
                  : position,
                  : gap,
                  : fastest_lap_time,
                  : kart_num
                  )""",
                  {'race_id': results[0],
                   'racer_id': results[1],
                   'position': results[2],
                   'gap': results[3],
                   'fastest_lap_time': results[4],
                   'kart_num': results[5]
                   })


def get_race_info(race_id):
    pass


def insert_racer(racer):
    pass


def remove_racer(racer):
    pass


# Testing Workspace
# all_races = getRaces(2019, 11, 21)
# league_races = getLeagueRaces(all_races)
# print(league_races)
race1 = getRaceInfo('21385')
insert_race(race1)

c.execute("SELECT * FROM races")
print(c.fetchall())

c.execute("SELECT * FROM results")
