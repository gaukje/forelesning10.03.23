import sys
import argparse
"""
print ("this is name of your program", sys.argv[0])

print ("total number of arguments", len(sys.argv))

if len(sys.argv) < 2:
    print ("i want at least two arguments")
    sys.exit()
"""

parser = argparse.ArgumentParser(description="positional arguments")
parser.add_argument('name', help="enter your name")
parser.add_argument('num1', help="enter number 1" )
parser.add_argument('num2', help="enter number 2" )

args = parser.parse_args()

print("your name is: ", args.name)

print("you entered number 1:", args.num1)
print("you entered number 2:", args.num2)


parser.add_argument('-n1', '--num1', type=int)

args = parser.parse_args()

print("your number is: ", args.num1)
print("your 2nd number is: ", args.num2)

parser.add_argument('-s', '--server', action='store_true')
