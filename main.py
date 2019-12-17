"""main.py"""

import sys
import argparse
from datapackage import birthdays
from scripts import dbmanager

"""If the user input is the same of the names in the list 
 the systeam will display the data of birth according to the 
 verbosity level """



"""Define  positional and optional arguments"""

def parse_argument():
    
    parser = argparse.ArgumentParser(
             prog="This program return the birthday of famous people")
    parser.add_argument(
             'n', nargs='+', help='You can insert one or names in the'
             'format: "Name Surname"')
    parser.add_argument('-v', '--verbosity',default=0, action='count', 
                        help='Choose the level of verbosity')

    args = parser.parse_args()
    return args

"""Print the answer"""
def verbosity_levels(name):
    
    for x in name:
        if birthdays.return_birthday(x):
            if args.verbosity >= 2:
                print ('{} was born the {}'.format(
                       x, birthdays.return_birthday(x)))
            elif args.verbosity >= 1:
                print ('{} : {}'.format(x, birthdays.return_birthday(x)))
            else:
                print (birthdays.return_birthday(x))
        else:
            print ('Sorry, {} is not present in our list, '.format(x))
            birthdays.print_birthdays()


if __name__ == "__main__":
    parse_argument()
    args = parse_argument()
    verbosity_levels(args.n)
            


