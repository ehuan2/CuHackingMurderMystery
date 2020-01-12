import json
import time

with open("MurderMysteryData.json", "r") as f:
    dataset = json.load(f)
    numPeople = [""]

people = {}
for x in dataset:
    if dataset[x]["guest-id"] in people.keys():
        info = dataset[x]
        info['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(x)))
        people[dataset[x]["guest-id"]].append(info)
    else:
        people[dataset[x]["guest-id"]] = []
        info = dataset[x]
        info['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(x)))
        people[dataset[x]["guest-id"]].append(info)


def log(name):
    if name in people.keys():
        print("Name: ", name)
        for dict in people[name]:
            print("Accessed", dict['device'], dict['device-id'], "at", dict['time'] + ',',  dict["event"])

# print(people)
for name in people.keys():
    log(name)