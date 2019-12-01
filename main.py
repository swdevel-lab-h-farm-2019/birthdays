#! /usr/bin/env python3

import birthdays
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name_surname", help="display the birthdays of Albert Einstein, Benjamin Franklin, Ada Lovelace, Donald Trump, Rowan Atkinson")
parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity")
args = parser.parse_args()
na_su = args.name_surname
print('The choosen person is ' + na_su)
if args.verbosity == 2:
    print("The person choosen was born on {}".format(na_su, birthdays.return_birthday(na_su) ))
elif args.verbosity == 1:
    print("Oh! You've selected who was born on {}".format(na_su, birthdays.return_birthday(na_su)))
else:
    print(birthdays.return_birthday(na_su))

birthdays.return_birthday(na_su)

