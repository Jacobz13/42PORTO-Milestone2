class Plant():
    def __init__(self, name, height, Age):
        self._name = name
        self._height = round(height, 1)
        self._Age = Age

    def set_height(self, height):
        if (height >= 0):
            self._height = round(height, 1)
        else:
            self._height = round(0, 1)
            print("{}: Error, height can't be negative".format(self._name))

    def set_age(self, Age):
        if (Age >= 0):
            self._Age = Age
        else:
            print("{}: Error, age can't be negative".format(self._name))
            self._Age = 0

    def get_height(self):
        return (self._height)

    def get_age(self):
        return (self._Age)

    def show(self):
        print("{}: {}cm".format(self._name, self._height), end="")
        print(", {} days old".format(self._Age))

    def grow(self):
        self._height = round((self._height + 0.8), 1)

    def age(self):
        self._Age = self._Age + 1


if __name__ == "__main__":
    pl = Plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    pl.show()
    print("\n")
    pl.set_height(pl.get_height())
    if (pl.get_height() == round(0, 1)):
        print("Height update rejected")
    else:
        print("Height updated: {}cm".format(pl.get_height()))

    pl.set_age(pl.get_age())
    if (pl.get_age() == 0):
        print("Age update rejected")
    else:
        print("Age updated: {} days".format(pl.get_age()))
    print("\nCurrent state: ", end="")
    pl.show()
