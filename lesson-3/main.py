import sys

# Goal: handle a command line argument.
#  Take in two numbers, sum them, then return the sum

def main():
    if len(sys.argv) <= 1:
        raise Exception("Not enough params provided")
    print(sys.argv[1])

if __name__ == "__main__":
    main()