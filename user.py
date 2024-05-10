import csv


class user:
    persoaneCreate = []
    counter = 0

    def __init__(self, nume, parola):
        self.nume = nume
        self.parola = parola
        self.id = user.counter

    def save(self):
        if not user.checkPersonByName(self.nume):
            self.writeToFile("persoane.csv")
            user.persoaneCreate.append(self)
            user.counter += 1

    def __repr__(self):
        return "id:" + str(self.id) + " ---- " + self.nume + " parola:" + self.parola

    def writeToFile(self, nume):
        with open(nume, 'a') as f:
            scriitor = csv.writer(f)
            scriitor.writerow([self.nume, self.parola])
            # f.write(f"{self.nume};{self.parola}\n")

    @classmethod
    def readFormFile(cls):
        login = []
        with open("persoane.csv", "r") as f:
            cititor = csv.reader(f)
            for persoana in cititor:
                login.append(persoana)
            return login

    @classmethod
    def loadPersons(cls):
        with open("persoane.csv", 'r') as f:
            cititor = csv.reader(f)
            if cititor:
                for person in cititor:
                    if not cls.checkPersonByName(person[0]):
                        tempPerson = user(person[0], person[1])
                        cls.persoaneCreate.append(tempPerson)
                        user.counter += 1

    @classmethod
    def checkPersonByName(cls, nume):
        for person in cls.persoaneCreate:
            if person.nume == nume:
                return True
        return False
