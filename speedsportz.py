from fetch import getRaces
rounds = ['2019, 08, 21',
          '2019, 09, 04',
          '2019, 09, 26',
          '2019, 10, 02',
          '2019, 10, 16',
          '2019, 11, 14',
          '2019, 11, 21']

all_races = []
for n in rounds:
    races = getRaces(n)
    all_races.append(races)

print(all_races)
