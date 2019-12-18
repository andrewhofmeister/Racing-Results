# DEPRECIATED
def getRaceResults(race_id):
    parameters = {
        "key": API_KEY,
    }
    response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + race_id + ".json", params=parameters)['scoreboard']
    scoreboard = response.json()
    for n in scoreboard:
        result = Result(
            race=race_id,
            position=scoreboard[0]['position'],
            first_name=scoreboard[0]['first_name'],
            last_name=scoreboard[0]['last_name'],
            racer_id=scoreboard[0]['racer_id'],
            kart_num=scoreboard[0]['kart_num'],
            gap=scoreboard[0]['gap'],
            fastest_lap_time=scoreboard[0]['fastest_lap_time']
        )
        result.save()


def getRaceResults2(race_id):
    # Returns list of race results in finishing order by driver_id
    payload = {
        "key": API_KEY
    }
    response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + race_id + ".json", params=payload)
    for n in response.json()['scoreboard']:
        return n['racer_id']
