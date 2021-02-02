from bs4 import BeautifulSoup as bs
import requests, json, pprint, pandas, csv, time
import psutil, asyncio, aiohttp

start_time = time.time()


def string_to_json_print(st):
    json_soup = json.loads(st)
    pprint.pprint(json_soup)


headers = {  # First line of defense
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}


def get_list_o_players(start_id, end_id):
    tutorial_count = 0
    list_of_players = []
    bad_requests = 0
    actual_players = 0
    while start_id < end_id:
        string = ''
        url = 'https://www.simcompanies.com/api/v2/players/' + str(start_id) + '/'
        r = requests.get(url)
        soup = bs(r.content, 'html.parser')
        json_soup = json.loads(str(soup))

        # print(json_soup["player"]["company"][:8])
        try:
            if json_soup["player"]["company"][:8] == 'Tutorial':
                tutorial_count += 1
            else:
                '''print(f'Player: {json_soup["player"]["company"]}, ID: {json_soup["player"]["id"]}, '
                      f'LvL: {json_soup["player"]["level"]}, Rank: {json_soup["player"]["rank"]}, '
                      f'Date Joined: {json_soup["player"]["dateJoined"]}')'''
                # print(f'str(json_soup["player"]["company"]): {str(json_soup["player"]["company"])}')
                string += (str(json_soup["player"]["company"]))
                string += "/" + (str(json_soup["player"]["id"]))
                string += "/" + (str(json_soup["player"]["level"]))
                string += "/" + (str(json_soup["player"]["rank"]))
                joined = (str(json_soup["player"]["dateJoined"][:19]))
                string += "/" + joined.replace('T', '/')
                print(f'string: {string}')
                list_of_players.append(string)
                actual_players += 1
        except:
            bad_requests += 1

        start_id += 1
        # print(f'current_id: {start_id} <====> last_id: {end_id}')

    print(f'Tutorial ID\'s: {tutorial_count}')
    print(f'BAD Requests: {bad_requests}')
    print(f'Actual Players: {actual_players}')
    return list_of_players


# =============================================================
s_id = 1032750  # ||||||||||||||||||||||||||||||||||||||||||||| Starting ID
e_id = 1032760  # ||||||||||||||||||||||||||||||||||||||||||||| Ending ID
# =============================================================
players = get_list_o_players(s_id, e_id)

with open('players.csv', 'w', ) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'ID', 'LvL', 'Rank', 'Join Date', 'Join Time'])
    for player in players:
        writer.writerow([player.split('/')[0], player.split('/')[1], player.split('/')[2],
                         player.split('/')[3], player.split('/')[4], player.split('/')[5]])

pandas.set_option('display.max_columns', 6)
pandas.set_option('display.width', 1000)
print(pandas.read_csv('players.csv'))
print(f'---------------- Elapsed time {round(time.time() - start_time, 6)} seconds ----------------')
CPU_percent = psutil.cpu_percent()
RAM_percent = psutil.virtual_memory().percent
with open('benchmark.csv', 'a', ) as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerow(['Players', 'Time','Cpu Used','RAM Used'])
    writer.writerow([(e_id - s_id), round(time.time() - start_time, 6), CPU_percent, RAM_percent])

print(f'CPU Used: {CPU_percent}% , RAM Used: {RAM_percent}%')
