import pygsheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import random

gc = pygsheets.authorize(service_file='C:\Users\Naman\Desktop\Python\udaan\Preffered-Day-Algo.py')
sh1 = gc.open_by_url(
    'https://docs.google.com/spreadsheets/d/1vhh5sja-eRbznvuuOp0Bd6C_gtXUl9vi6E886_PZFJs/edit#gid=1374159174')
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'Preffered-Day-Algo-77a179afc6ce.json', scope)
gc1 = gspread.authorize(credentials)
data = gc1.open_by_key("1vhh5sja-eRbznvuuOp0Bd6C_gtXUl9vi6E886_PZFJs")
# Google sheet-data
Demo = data.worksheet('preffered_day')
df1 = Demo.get('A:J')
print(df1)

# Get input from google sheet
# Gsheet Link: https://docs.google.com/spreadsheets/d/1vhh5sja-eRbznvuuOp0Bd6C_gtXUl9vi6E886_PZFJs/edit#gid=1374159174
# Query Link: https://data.udaan.io/probes/betsxe
ls = [['ORGXGW1PTD802QS44HP9S787M3F44', 'Lifestyle', 'sufiyan.md@udaan.com', 'Data Set 1', 4, 1, 4, 4, 1, 3], ['ORGZWMV9LFDEV8HX4KNKJF218WQQ4', 'Lifestyle', 'sufiyan.md@udaan.com', 'Data Set 1', 1, 1, 2, 3, 1, 3], ['ORGXGW1PTD802QS44HP9S787M3F44', 'Lifestyle', 'sufiyan.md@udaan.com', 'Data Set 1', 1, 1, 2, 1, 1, 3],
      ['ORGZWMV9LFDEV8HX4KNKJF218WQQ4', 'Lifestyle', 'sufiyan.md@udaan.com', 'Data Set 1', 2, 4, 1, 1, 1, 4], ['ORGXGW1PTD802QS44HP9S787M3F44', 'Lifestyle', 'sufiyan.md@udaan.com', 'Data Set 1', 1, 1, 1, 1, 1, 3], ['ORGZWMV9LFDEV8HX4KNKJF218WQQ4', 'Lifestyle', 'sufiyan.md@udaan.com', 'Data Set 1', 1, 2, 3, 2, 4, 3], ['ORGXGW1PTD802QS44HP9S787M3F44', 'Lifestyle', 'sufiyan.md@udaan.com', 'Data Set 1', 4, 1, 4, 4, 1, 3], ['ORGZWMV9LFDEV8HX4KNKJF218WQQ4', 'Lifestyle', 'sufiyan.md@udaan.com', 'Data Set 1', 4, 1, 4, 4, 1, 3]]


def divide_data_set(list):
    set1 = []
    set2 = []
    for val in list:

        if val[3] == 'Data Set 1':
            set1.append(val)
        elif val[3] == 'Data Set 2':
            set2.append(val)
    dict = {}
    dict['Data Set 1'] = set1
    dict['Data Set 2'] = set2
    return dict


def agent_dict(dict):
    for key, input in dict.items():
        agent = {}
        for val in input:
            if val[2] in agent.keys():
                agent[val[2]].append(val)
            else:
                agent[val[2]] = [val]
        dict[key] = agent
    return dict


def max_buyer_assigned_per_day(list):
    count = len(list)
    equal = count//6
    rem = count % 6
    ls = [equal, equal, equal, equal, equal, equal]
    i = random.choice([i for i in range(6)])
    while rem != 0:
        if i > 5:
            i = 0
        else:
            ls[i] += 1
            i += 1
            rem -= 1
    return ls


def get_index_positions(list_of_elems, element):

    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    for i, val in enumerate(index_pos_list):
        # here 4 is beacuse first 4 elements in list need to be excluded to get exact
        # weekday Monday = 0 and Saturday = 5
        index_pos_list[i] = val - 4
    return index_pos_list


def assign_preffered_day(val):
    max_val = max(val[4:])
    index_pos_list = get_index_positions(val, max_val)
    preffered_day = random.choice(index_pos_list)
    return preffered_day


dict_of_set = divide_data_set(ls)

data_set = agent_dict(dict_of_set)
print(data_set)
assigned_set = []
for set in data_set.values():
    for agents in set.values():
        counter = [0, 0, 0, 0, 0, 0]
        buyer_max_day = max_buyer_assigned_per_day(agents)
        print('Agent Max Buyer Assigend:', buyer_max_day)
        for val in agents:
            while True:
                preffered_day = assign_preffered_day(val)
                counter[preffered_day] += 1
                buyer_max_day[preffered_day] -= 1
                if buyer_max_day[preffered_day] >= 0:
                    val = val[:4]
                    val.append(preffered_day)
                    assigned_set.append(val)
                    break
                else:
                    counter[preffered_day] -= 1
                    buyer_max_day[preffered_day] += 1
                    val[preffered_day+4] = 0
            print('counter:', counter)
            print('max_buyer_assigned:', buyer_max_day)
            print('New Buyer')
        print('New Agent')
    print('New Data Set')
print(assigned_set)
