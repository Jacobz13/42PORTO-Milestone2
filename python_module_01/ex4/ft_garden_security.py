class Plant():
    def __init__(self, name: str, height: float, Age: int) -> None:
        self._name = name
        self._height = round(height, 1)
        self._Age = Age

    def set_height(self, height: float) -> None:
        if (height >= 0):
            self._height = round(height, 1)
        else:
            self._height = round(0, 1)
            print(f"{self._name}: Error, height can't be negative")

    def set_age(self, Age: int) -> None:
        if (Age >= 0):
            self._Age = Age
        else:
            print("{}: Error, age can t be negative".format(self._name))
            self._Age = 0

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._Age)

    def show(self) -> None:
        print("{}: {}cm".format(self._name, self._height), end="")
        print(", {} days old".format(self._Age))

    def grow(self) -> None:
        self._height = round((self._height + 0.8), 1)

    def age(self) -> None:
        self._Age = self._Age + 1


if __name__ == "__main__":
    pl = Plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    pl.show()
    print("\n")
    pl.set_height(-5)
    print("Valor de getHeight {}")
    if (pl.get_height() == 0.0):
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
