
# Goal: read two numbers from input and sum them together

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

def get_number():
    print("Please input a valid number:")
    while number := input():
        try:
            return float(number)
        except ValueError as _:
            print("\nThat was not a valid number: ")
            continue

def return_menu():
    print("Press Enter to Return to Menu")
    input()
    clear()
    handler()

def addition():
    clear()
    print("Lets input two numbers:\n")
    number1 = get_number()
    number2 = get_number()
    print("\nAdding these two numbers equals:", number1 + number2)
    return_menu()
    
def substract():
    clear()
    print("Lets input two numbers:\n")
    number1 = get_number()
    number2 = get_number()
    print("\nSubstracting these two numbers equals:", number1 - number2)
    return_menu()

def multiply():
    clear()
    print("Lets input two numbers:\n")
    number1 = get_number()
    number2 = get_number()
    print("\nMultiplying these two numbers equals:", number1 * number2)
    return_menu()

def divide():
    clear()
    print("Lets input two numbers:\n")
    number1 = get_number()
    number2 = get_number()
    print("\nDividing these two numbers equals:", number1 / number2)
    return_menu()


choice_menu = """Pick a choice from the following: 
1) Addition two numbers.
2) Substract two numbers.
3) Multiply two numbers.
4) Divide two numbers. 
5) Exit.

Your selection:"""


def handler():
    clear()
    while (choice := input(choice_menu)) != "5":
        if choice == "1":
            addition()
        elif choice == "2":
            substract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        else:
            print("Invalid option. Press ENTER and try again!")
            input()
            clear()


def main():
    clear()
    handler()
    clear()

if __name__ == "__main__":
    main()
