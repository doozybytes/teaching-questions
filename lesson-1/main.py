
# Goal: return the text: "Hello, world!"

# Import only system from os
from os import system, name

# Clear screen based on OS type
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Ask for name and print back
def main():
    clear()
    name = input("What is your name?\n")
    clear()
    print("\nHello", name, "!")
    input()
    clear()

if __name__ == "__main__":
    main()
