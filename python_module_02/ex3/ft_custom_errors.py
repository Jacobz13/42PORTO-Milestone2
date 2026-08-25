class GardenError(Exception):

    def __init__(self, error: str = "Unknown plant error") -> None:
        self.error = error
        super().__init__(error)


class PlantError(GardenError):
    def __init__(self, name: str) -> None:
        self.name = name

    def plant_error(self, pl: str) -> None:
        raise PlantError(f" The {self.name} plant is wilting!")


class WaterError(GardenError):
    def __init__(self, liter: float) -> None:
        super().__init__(" Not enough water in the tank!")
        self.liter = liter

    def water_error(self, liter: float) -> None:
        if (liter < 5):
            raise WaterError(liter)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    wt = WaterError(3.4)
    pl = PlantError("tomato")
    name = "Potato"
    try:
        pl.plant_error(name)
    except PlantError as e:
        print("Testing PlantError...")
        print(f"Caught PlantError:{e}")
        print("\n", end="")
    try:
        wt.water_error(4.3)
    except WaterError as e:
        print("Testing WaterError...")
        print(f"Caught WaterError:{e}")
        print("\n", end="")
    print("Testing catching all garden errors...")
    try:
        pl.plant_error(name)
    except GardenError as e:
        print(f"Caught PlantError:{e}")
    try:
        wt.water_error(4.3)
    except GardenError as e:
        print(f"Caught WaterError:{e}")
    print("\nAll custom error types work correctly!")
