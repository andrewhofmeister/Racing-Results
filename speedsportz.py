from fetch import getRaces, getLeagueRaces
# Enter race dates in a nested list format and return a list of
# all races from those dates. Relevant races still need to be found.

round_1 = ['2019', '08', '21']
round_2 = ['2019', '09', '04']
round_3 = ['2019', '09', '26']
round_4 = ['2019', '10', '02']
round_5 = ['2019', '10', '16']
round_6 = ['2019', '11', '14']
round_7 = ['2019', '11', '21']

rounds = (round_1, round_2, round_3, round_4, round_5, round_6, round_7)
all_races = []
# for index, n in enumerate(rounds):
#     year = int(rounds[index][0])
#     month = int(rounds[index][1])
#     day = int(rounds[index][2])
#     races = getRaces(year, month, day)
#     all_races.append(races)
#
#
# print("'"+all_races[0][1]+"'")
getLeagueRaces(str(19984))

# print(all_races)
# league_races = []
# for index, n in enumerate(all_races):
#     leagueRaces = getLeagueRaces(all_races[index][n])
#     print(leagueRaces)
#     league_races.append(leagueRaces)


# print(league_races)
