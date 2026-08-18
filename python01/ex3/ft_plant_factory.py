class Plant():
    def __init__(self, name, height, Age):
        self.name = name
        self.height = round(height, 1)
        self.Age = Age

    def show(self):
        print("{}: {}cm, {} days old".format(self.name, self.height, self.Age))

    def grow(self):
        self.height = round((self.height + 0.8), 1)

    def age(self):
        self.Age = self.Age + 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant4 = Plant("Orchidea", 29, 20)
    plant5 = Plant("Lotus", 16, 42)
    print("=== Plant Factory Output ===")
    print("Created: ", end='')
    plant1.show()
    print("Created: ", end='')
    plant2.show()
    print("Created: ", end='')
    plant3.show()
    print("Created: ", end='')
    plant4.show()
    print("Created: ", end='')
    plant5.show()
