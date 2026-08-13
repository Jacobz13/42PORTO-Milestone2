def ft_aux_count_harvest_recursive(n: int, days: int):
    if ((n+1) == days):
        print("Harvest time!")
    else:
        print("Day ", (n+1))
        ft_aux_count_harvest_recursive(n+1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_aux_count_harvest_recursive(0, days)
