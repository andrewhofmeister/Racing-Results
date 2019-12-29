from fetch import getRaces, getLeagueRaces, getRaceInfo
from database import insert_race
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
# print(all_races)
# league_races = []
# for index, n in enumerate(all_races):
#     leagueRaces = getLeagueRaces(all_races[index])
#     print(leagueRaces)
#     league_races.append(leagueRaces)

league_races = [
                '19973', '19977', '19974', '19978', '19981', '19982', '19976',
                '19980', '20119', '20123', '20120', '20124', '20127', '20128',
                '20122', '20126', '20595', '20599', '20596', '20600', '20603',
                '20604', '20598', '20602', '20691', '20692', '20677', '20681',
                '20678', '20682', '20685', '20686', '20680', '20684', '20906',
                '20910', '20907', '20911', '20921', '20922', '20909', '20913',
                '21302', '21306', '21303', '21307', '21310', '21311', '21305',
                '21309', '21378', '21382', '21379', '21383', '21386', '21387',
                '21381', '21385'
                ]

league_races.remove('20691')
league_races.remove('20692')
print(league_races)
for n in league_races:
    race = getRaceInfo(n)
    insert_race(race)
