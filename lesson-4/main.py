
# Goal: handle a command line argument.
# It should handle two flags
#   --sum {integers}
#   --mult {integers}
# When run with the respective flags it shoudld return the 
# sum or product of the provided numbers

import argparse

parser = argparse.ArgumentParser(
    prog="MyProgram",
    description="I handle different inputs",
)

parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', ...)
parser.add_argument('--mult', ...)


def main():
    ...

if __name__ == "__main__":
    main()
