import sys

tam = len(sys.argv)
arg = sys.argv
if (tam == 1):
    print("=== Command Quest ===")
    print(f"Program name: {arg[0]}")
    print("No arguments provided!")
    print(f"Total arguments: {tam}")
else:
    print("=== Command Quest ===")
    print(f"Program name: {arg[0]}")
    print(f"Arguments received: {tam - 1}")
    i = 1
    while (i < tam):
        print(f"Argument {i}: {arg[i]}")
        i = i + 1
    print(f"Total arguments: {tam}")
