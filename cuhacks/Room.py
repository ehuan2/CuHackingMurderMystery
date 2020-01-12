
class Room():


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ls = []

    def __addPerson__(self, person): # it'll add whatever here, append it
        self.ls.append(person)

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def __removePerson__(self, person):
        self.ls.remove(person)

    def __guiAppear__(self):
        for i in range (len(self.ls)) :

            xAppear = self.x + 10 + 10*(i%10) # the ten can be changed


            yAppear = self.y + 10 + 10*(i/10)

