from fetch import getRaces, getLeagueRaces
# Enter race dates in a nested list format and return a list of
# all races from those dates. Relevant races still need to be found.
rounds = [['2019', '08', '21'],
          ['2019', '09', '04'],
          ['2019', '09', '26'],
          ['2019', '10', '02'],
          ['2019', '10', '16'],
          ['2019', '11', '14'],
          ['2019', '11', '21']]

all_races = []
for n in rounds:
    year = int(n[0])
    month = int(n[1])
    day = int(n[2])
    races = getRaces(year, month, day)
    all_races.append(races)

leagueRaces = getLeagueRaces(all_races)
print(leagueRaces)
