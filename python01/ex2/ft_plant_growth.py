class Plant():
    def __init__(self, name, height, Age):
        self.name = name
        self.height = height
        self.Age = Age

    def show(self):
        print("{}: {}cm, {} days old".format(self.name, self.height, self.Age))

    def grow(self):
        self.height = round((self.height + 0.8), 1)

    def age(self):
        self.Age = self.Age + 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    temp = plant1.height
    print("=== Garden Plant Growth ===")
    plant1.show()
    i = 0
    while (i < 7):
        print("=== Day {} ===".format(i + 1))
        plant1.grow()
        plant1.age()
        plant1.show()
        i = i + 1
    print("Growth this week: {}cm".format(round((plant1.height - temp), 1)))
