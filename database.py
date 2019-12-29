# Initialize sqlite3 database schema and functions to add/delete entries.
import sqlite3
from fetch import getRaceInfo, getRaceResults, getRacers, getRacerInfo
# Initialize db in RAM for every run of script for developemnt and testing
conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS races (
        race_id INTEGER NOT NULL,
        race_date TEXT NOT NULL,
        race_name TEXT NOT NULL,
        PRIMARY KEY (race_id)
        )""")


c.execute("""CREATE TABLE IF NOT EXISTS classes (
        class_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )""")


c.execute("""CREATE TABLE IF NOT EXISTS racers (
        racer_id INTEGER NOT NULL,
        first_name TEXT,
        last_name TEXT,
        class TEXT,
        PRIMARY KEY (racer_id)
        FOREIGN KEY (class) REFERENCES classes(class_id)
            ON DELETE CASCADE
        )""")


c.execute("""CREATE TABLE IF NOT EXISTS results (
        result_id INTEGER PRIMARY KEY AUTOINCREMENT,
        race_id INTEGER NOT NULL,
        racer_id INTEGER NOT NULL,
        posistion INTEGER NOT NULL,
        gap REAL NOT NULL,
        fastest_lap_time REAL NOT NULL,
        kart_num INTEGER NOT NULL,
        FOREIGN KEY (race_id) REFERENCES races(race_id)
            ON DELETE CASCADE,
        FOREIGN KEY (racer_id) REFERENCES racers(racer_id)
            ON DELETE CASCADE
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
                  :result_id,
                  :race_id,
                  :racer_id,
                  :position,
                  :gap,
                  :fastest_lap_time,
                  :kart_num
                  )""",
                  {'result_id': None,
                   'race_id': results[0],
                   'racer_id': results[1],
                   'position': results[2],
                   'gap': results[3],
                   'fastest_lap_time': results[4],
                   'kart_num': results[5]
                   })


def insert_racer(racer):
    if len(racer) == 3:
        with conn:
            c.execute("""INSERT INTO racers VALUES(
                      :racer_id,
                      :first_name,
                      :last_name,
                      :weight_class
                      )""",
                      {'racer_id': racer[0],
                       'first_name': racer[1],
                       'last_name': racer[2],
                       'weight_class': ''
                       })
    elif len(racer) == 4:
        with conn:
            c.execute("""INSERT INTO racers VALUES(
                      :racer_id,
                      :first_name,
                      :last_name,
                      :weight_class
                      )""",
                      {'racer_id': racer[0],
                       'first_name': racer[1],
                       'last_name': racer[2],
                       'weight_class': racer[3]
                       })
    else:
        print('Input Error!!')


def remove_racer(racer):
    pass


# Testing Workspace
# all_races = getRaces(2019, 11, 21)
# league_races = getLeagueRaces(all_races)
# print(league_races)
# race1 = getRaceInfo('21385')
# insert_race(race1)
c.execute("SELECT * FROM races")
print(c.fetchall())
#
# results = getRaceResults('21385', '1000163')
# insert_results(results)
# c.execute("SELECT * FROM results")
# print(c.fetchall())
#
# racers = getRacers('21385')
# racer1 = getRacerInfo(racers[0])
# racer2 = getRacerInfo(racers[1])
# racer2.append('H')
# insert_racer(racer1)
# insert_racer(racer2)
# c.execute("SELECT * FROM racers")
# print(c.fetchall())
