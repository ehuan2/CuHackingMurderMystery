import json

class Data:
    def __init__(self):
        self.dataset = {}
        with open("murder-data.json", "r") as f:
            self.dataset = json.load(f)

        self.people = {}
        for x in self.dataset:
            if self.dataset[x]["guest-id"] in self.people.keys():
                info = self.dataset[x]
                info['time'] = int(x) # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(x)))
                self.people[self.dataset[x]["guest-id"]].append(info)
            else:
                self.people[self.dataset[x]["guest-id"]] = []
                info = self.dataset[x]
                info['time'] = int(x) # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(x)))
                self.people[self.dataset[x]["guest-id"]].append(info)

        for k in self.dataset.copy().keys():
            if self.dataset[k]["device-id"] == "stairwell":
                del(self.dataset[k])

    def log(self, name):
        if name in self.people.keys():
            print("Name: ", name)
            for d in self.people[name]:
                print("Accessed", d['device'], d['device-id'], "at", d['time'] + ',', d["event"])

    def getEvents(self, interval):
        return {t: self.dataset[t] for t in self.dataset.keys() if interval <= int(t) < interval + 15*60}
