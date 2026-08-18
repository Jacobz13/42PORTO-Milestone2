def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if (unit == "packets"):
        print("{} seeds: {} {} available".format(seed_type, quantity, unit))
    elif (unit == "grams"):
        print(seed_type + " seeds: " + str(quantity) + " " + unit + " total")
    elif (unit == "area"):
        print(seed_type + " seeds: covers " + str(quantity) + " square meters")
