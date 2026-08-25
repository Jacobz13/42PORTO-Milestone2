class GardenError(Exception):

    def __init__(self, error: str) -> None:
        super().__init__("Unknown plant error")
        self.error = error
        self.liter = 0.0


class PlantError(GardenError):
    def __init__(self, error: str) -> None:
        super().__init__("Unknown plant error")
        self.error = error


def water_plant(plant_name: str) -> None:

    if (plant_name.capitalize() == plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        s = f"Caught PlantError: Invalid plant name to water: \'{plant_name}\'"
        print(s)
        raise PlantError(s)


def test_watering_system() -> None:
    pl = ["Tomato", "Lettuce", "Carrots", "eggplant"]
    i = 0
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        while (i < 4):
            water_plant(pl[i])
            i = i + 1
    except PlantError:
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
