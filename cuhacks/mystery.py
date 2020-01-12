import json
import time


class Data:
    def __init__(self):
        self.dataset = {}
        with open("murder-data.json", "r") as f:
            self.dataset = json.load(f)

        self.people = {}
        for x in self.dataset:
            if self.dataset[x]["guest-id"] in self.people.keys():
                info = self.dataset[x]
                info['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(x)))
                self.people[self.dataset[x]["guest-id"]].append(info)
            else:
                self.people[self.dataset[x]["guest-id"]] = []
                info = self.dataset[x]
                info['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(x)))
                self.people[self.dataset[x]["guest-id"]].append(info)

    def log(self, name):
        if name in self.people.keys():
            print("Name: ", name)
            for d in self.people[name]:
                print("Accessed", d['device'], d['device-id'], "at", d['time'] + ',', d["event"])

fuck = Data()
print([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(x))) for x in fuck.dataset.keys()])
