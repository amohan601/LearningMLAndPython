#https://docs.python.org/3/library/argparse.html
import argparse
import math
parser = argparse.ArgumentParser('Testing input arguments')
parser.add_argument('-o','--operation', type=str, choices=['add','mult'])
parser.add_argument('-n','--numbers', type=int, nargs='+')
parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag

args = parser.parse_args()

print('input operation {}, numbers {}, verbose {}'.format(args.operation, args.numbers, args.verbose))

if args.operation == 'add':
    print('Sum of numbers {}'.format(sum(args.numbers)))

elif args.operation == 'mult':
    print('Product of numbers {}'.format(math.prod(args.numbers)))

##run as  python ArgumentParserExample.py -o add -n 1 1
##run as  python ArgumentParserExample.py -o mult -n 1 1

