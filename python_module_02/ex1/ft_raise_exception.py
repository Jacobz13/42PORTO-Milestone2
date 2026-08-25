def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    st1 = f"Caught input_temperature error{temp}°C"
    if (temp > 40):
        st2 = "C is too hot for plants (max 40°C)"
        raise Exception(st1 + st2)
    elif (temp < 0):
        st2 = " is too cold for plants (min 0°C)"
        raise Exception(st1 + st2)
    return (temp)


def test_temperature() -> None:
    raw = ["25", "abc", "100", "-50"]
    i = 0
    while (i < 4):
        print("\nInput data is \'"+raw[i]+"\'")
        try:
            print(f"Temperature is now {input_temperature(raw[i])}°C")
        except Exception:
            print("Caught input_temperature error: ", end="")
            print("invalid literal for int() with base 10: "+raw[i])
        i = i + 1


print("=== Garden Temperature Checker ===")
test_temperature()
print("\nAll tests completed - program didn't crash!")
