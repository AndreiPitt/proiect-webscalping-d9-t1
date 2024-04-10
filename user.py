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
            f.write(f"{self.nume};{self.parola}\n")

    @classmethod
    def readFormFile(cls):
        login = []
        f = open("persoane.csv", "r")
        content_1 = f.read().split("\n")

        for line in content_1:
            detalii = line.split(";")
            login.append(detalii)
        # del login[len(login) - 1]
        # for i in range(0, len(login)):
        #     del login[i][1]

        # Pentru verificare
        # print(login)
        return login

    @classmethod
    def loadPersons(cls):
        with open("persoane.csv", 'r') as f:
            content = [line.strip("\n") for line in f.readlines()]
            if content:
                for person in content:
                    details = person.split(";")
                    if not cls.checkPersonByName(details[0]):
                        tempPerson = user(details[0], details[1])
                        cls.persoaneCreate.append(tempPerson)
                        user.counter += 1

    @classmethod
    def checkPersonByName(cls, nume):
        for person in cls.persoaneCreate:
            if person.nume == nume:
                return True
        return False