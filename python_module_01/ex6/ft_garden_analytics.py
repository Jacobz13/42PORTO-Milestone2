class Plant():
    def __init__(self, name: str, height: float, Age: int) -> None:
        self._name = name
        self._height = round(height, 1)
        self._Age = Age
        self.n_grow = 0
        self.n_age = 0
        self.n_show = 0

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
        print(", {} days old".format(self.get_age()))
        self.n_show = self.n_show + 1

    def grow(self) -> None:
        self.set_height(round((self.get_height() + 0.8), 1))
        self.n_grow = self.n_grow + 1

    def age(self) -> None:
        self.set_age(self.get_age() + 1)
        self.n_age = self.n_age + 1

    @staticmethod
    def is_older_than_year(self, age: int) -> bool:
        if (age > 365):
            return True
        else:
            return False

    @classmethod
    def create_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, Age: int, color: str) -> None:
        super().__init__(name, height, Age)
        self.color = color
        self.n_show: int

    def show(self) -> None:
        print("{}: {}cm".format(self._name, self.get_height()), end="")
        print(", {} days old".format(self.get_age()))
        print("Color: {}".format(self.color))
        if (self.n_grow == 0):
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")
        self.n_show = self.n_show + 1

    def bloom(self) -> None:
        self.show()
        print(f"{self._name} has not bloomed yet")
        print(f"[asking the {self._name} to bloom]")
        self.show()
        print(f"{self._name} is blooming beautifully!")

    def grow(self) -> None:
        print(f"[asking the {self._name.lower()} to grow and bloom]")
        self.set_height(round(self.get_height() + 8.0, 1))
        self.n_grow = self.n_grow + 1


class Tree(Plant):
    def __init__(self, n: str, h: float, Age: int, diameter: float) -> None:
        super().__init__(n, h, Age)
        self.n_show = 0
        self.diameter = diameter
        self.shade = 0

    def show(self) -> None:
        print("{}: {}cm".format(self._name, self.get_height()), end="")
        print(", {} days old".format(self.get_age()))
        print("Trunk diameter: {}cm".format(self.diameter))
        self.n_show = self.n_show + 1

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print("Tree {} now produces a shade of".format(self._name), end="")
        print(f" {self.get_height()}cm long and {self.diameter}cm wide.")
        self.shade = self.shade + 1


class Vegetable(Plant):
    def __init__(self, n: str, h: float, A: int, h_s: str, n_v: int) -> None:
        super().__init__(n, h, A)
        self.harvest_season = h_s
        self.nutrional_value = n_v
        self.n_show = 0

    def show(self) -> None:
        print("{}: {}cm".format(self._name, self._height), end="")
        print(", {} days old".format(self.get_age()))
        print("Harvest season: {}".format(self.harvest_season))
        print("Nutritional value: ", self.nutrional_value)
        self.n_show = self.n_show + 1


class Seed(Flower):
    def __init__(self, name: str, height: float, Age: int, color: str) -> None:
        super().__init__(name, height, Age, color)
        self.n_show = 0
        self.seed = 0

    def show(self) -> None:
        print("{}: {}cm".format(self._name, self._height), end="")
        print(", {} days old".format(self.get_age()))
        print("Color: {}".format(self.color))
        if (self.seed > 0):
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")
        print(f"Seeds = {int(self.seed)}")
        self.n_show = self.n_show + 1

    def grow(self) -> None:
        print(f"[make {self._name.lower()} grow,age and bloom]")
        for i in range(20):
            self.set_height(self.get_height() + 1.5)
            self.set_age(self.get_age() + 1)
            self.seed = self.seed + 2
        self.n_grow = self.n_grow + 1
        self.n_age = self.n_age + 1


def display_statics(plnt: Plant) -> None:
    print(f"[statistics for {plnt._name}]")
    print(f"Stats: {plnt.n_grow} grow, {plnt.n_age} age, {plnt.n_show} show")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ", end="")
    print(f"-> {Plant.is_older_than_year(Plant, 30)}")
    print("Is 400 days more than a year? ", end="")
    print(f"-> {Plant.is_older_than_year(Plant, 400)}")
    print("\n", end="")
    print("=== Flower")
    fl = Flower("Rose", 15.0, 10, "red")
    fl.show()
    display_statics(fl)
    fl.grow()
    fl.show()
    display_statics(fl)
    print("\n", end="")
    print("=== Tree")
    tr = Tree("Oak", 200.0, 365, 5.0)
    tr.show()
    display_statics(tr)
    print(f"{tr.shade} shade")
    tr.produce_shade()
    display_statics(tr)
    print(f"{tr.shade} shade")
    print("\n", end="")
    print("=== Seed")
    sd = Seed("Sunflower", 80.0, 45, "yellow")
    sd.show()
    sd.grow()
    sd.show()
    display_statics(sd)
    print("\n", end="")
    print("=== Anonymous")
    pl = Plant.create_plant()
    pl.show()
    display_statics(pl)
