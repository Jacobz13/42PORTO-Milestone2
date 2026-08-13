def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 0
    for i in range(days):
        print("Day ", (i+1))
        if ((i+1) == days):
            print("Harvest time!")
