"""defining birthdays funxtions"""

"""Open the birth.csv file and read it"""
import csv


reader = csv.reader(open('datapackage/birthlist.csv', 'r'))
d = {}
for row in reader:
    x, y = row
    d[x] = y


"""Explaining functions"""

"""Print the full list of people"""
def print_birthdays():
    print('We know the birthdays of these people:')
    for e in d:
        print(e)

"""If the imput correspond to a name 
in the list the function is true."""
def return_birthday(name):
    if name in d:
        return d[name]
    else:
        return False
