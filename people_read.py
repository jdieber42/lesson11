import json


dict = dict()

with open("people.json", "r") as people_file:
    peoble_list = json.loads(people_file.read())

list = dict["people"]

for dict_el in list:
    for key in dict_el.keys():
        print(dict_el[key])
