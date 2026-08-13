def ft_seed_inventory(p: str, q: int, m: str):
    if (m == "packets"):
        print(p + " seeds: " + str(q) + " " + m + " available")
    elif (m == "grams"):
        print(p + " seeds: " + str(q) + " " + m + " total")
    elif (m == "area"):
        print(p + " seeds: " + "covers " + str(q) + " " + m + " square meters")
