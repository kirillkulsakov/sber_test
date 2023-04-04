import json
import datetime


def card_hide(param):
    if 'Счет' in param:
        return "Cчет **", param[-4:]
    else:
        return param[:len(param) - 12], " ", param[(len(param) - 8):(len(param) - 6)], "** **** ", param[-4:]


with open("operations.json", "r", encoding='utf-8') as f:
    data = json.load(f)
    counter = 0

    for i in sorted(data, key=lambda k: ['id'][0], reverse=True):
        if i['state'] == 'EXECUTED' and counter <= 5:
            print(datetime.datetime.strptime((i['date'][0:10]), "%Y-%m-%d").strftime("%d.%m.%Y"), i['description'],
                  sep=' ')

            try:
                print("".join(card_hide(i['from'])), "".join(card_hide(i['to'])), sep=" -> ")
            except:
                print("".join(card_hide(i['to'])))

            print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'], sep=' ', end='\n\n')
            counter += 1

        else:
            continue
