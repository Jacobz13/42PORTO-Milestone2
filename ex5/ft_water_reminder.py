def ft_water_reminder():
    number_of_days = int(input("Days since last watering: "))
    if (number_of_days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
