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
            print("{}: Error, height can't be negative".format(self._name))

    def set_age(self, Age: int) -> None:
        if (Age >= 0):
            self._Age = Age
        else:
            print("{}: Error, age can't be negative".format(self._name))
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


class Flower(Plant):
    def __init__(self, name: str, height: float, Age: int, color: str) -> None:
        super().__init__(name, height, Age)
        self.color = color

    def show(self) -> None:
        print("{}: {}cm".format(self._name, self._height), end="")
        print(", {} days old".format(self._Age))
        print("Color: {}".format(self.color))
        pass

    def bloom(self) -> None:
        self.show()
        print("Rose has not bloomed yet")
        print("[asking the rose to bloom]")
        self.show()
        print("Rose is blooming beautifully!")


class Tree(Plant):
    def __init__(self, n: str, h: float, Age: int, diameter: float) -> None:
        super().__init__(n, h, Age)
        self.diameter = diameter

    def show(self) -> None:
        print("{}: {}cm".format(self._name, self._height), end="")
        print(", {} days old".format(self._Age))
        print("Trunk diameter: {}".format(self.diameter))

    def produce_shade(self) -> None:
        self.show()
        print("[asking the oak to produce shade]")
        print("Tree {} now produces a shade of".format(self._name), end="")
        print("  {}cm long and {}cm wide.".format(self._height, self.diameter))


class Vegetable(Plant):
    def __init__(self, n: str, h: float, A: int, h_s: str, n_v: int) -> None:
        super().__init__(n, h, A)
        self.harvest_season = h_s
        self.nutrional_value = n_v

    def show(self) -> None:
        print("{}: {}cm".format(self._name, self._height), end="")
        print(", {} days old".format(self._Age))
        print("Harvest season: {}".format(self.harvest_season))
        print("Nutritional value: ", self.nutrional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.bloom()
    print("\n", end="")
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, round(5.0, 1))
    tree.produce_shade()
    print("\n", end="")
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    days = 20
    i = 0
    print("[make tomato grow and age for {} days]".format(days))
    for i in range(days):
        vegetable.grow()
        vegetable.age()
        vegetable.nutrional_value = vegetable.nutrional_value + 1
    vegetable.show()
