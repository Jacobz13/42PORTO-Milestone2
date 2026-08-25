def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return (temp)


def test_temperature() -> None:
    raw = ["25", "abc"]
    i = 0
    while (i < 2):
        print("\nInput data is \'"+raw[i]+"\'")
        try:
            print(f"Temperature is now {input_temperature(raw[i])}°C")
        except Exception:
            print("Caught input_temperature error: ", end="")
            print("invalid literal for int() with base 10: "+raw[i])
        i = i + 1


print("=== Garden Temperature ===")
test_temperature()
print("\nAll tests completed - program didn't crash!")
