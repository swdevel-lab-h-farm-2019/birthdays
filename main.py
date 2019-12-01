#! /usr/bin/env python3

import birthdays
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name_surname", help="display the birthdays of Albert Einstein, Benjamin Franklin, Ada Lovelace, Donald Trump, Rowan Atkinson")
args = parser.parse_args()
print('the choosen person is ' + args.name_surname)

birthdays.return_birthday(args.name_surname)

