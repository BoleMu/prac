YEAR = 2017
AGE = 50

class guitar:
    def __init__(self, name="", year="", cost=""):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return YEAR

    def vintage(self):
        return self.get_age() >= AGE
