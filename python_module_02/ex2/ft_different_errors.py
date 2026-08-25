"""def garden_operations(operation_number: int) -> None:
    op = operation_number
    if (op == 0):
        print("Testing operation 0...")
    elif (op == 1):
        print("Testing operation 1...")
    elif (op == 2):
        print("Testing operation 2...")
    elif (op == 3):
        print("Testing operation 3...")
    else:
        print("Testing operation 4...")
    return
"""

"""def test_error_types() -> None:
    i = 0
    while (i <= 4):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            if (i == 4):
                print("Operation completed successfully\n")
        except ValueError:
            print("Caught ValueError: ", end="")
            print(ValueError)
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: ", end="")
            print(ZeroDivisionError)
        except FileNotFoundError:
            print("Caught FileNotFoundError: ", end="")
            print(FileNotFoundError)
        except TypeError:
            print("Caught TypeError: ", end="")
            print(TypeError)
        i = i + 1"""


def garden_operations(operation_number: int) -> None:
    op = operation_number
    if (op == 0):
        print(int('abc'))
    elif (op == 1):
        print(9 / 0)
    elif (op == 2):
        open('/non/existent/file')
    elif (op == 3):
        "String" + 2
    else:
        print("Operation completed successfully\n")
    return


def test_error_types() -> None:
    i = 0
    while (i <= 4):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        i = i + 1
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
