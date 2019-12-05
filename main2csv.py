import argparse
import csv

filename= "Data_file.csv"
def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    with open(filename, 'r') as csvfile:
         csvreader = csv.reader(csvfile)
    for name in csvfile:
        print(name)
def return_birthday(name):
    with open(filename, 'r') as csvfile:
         csvreader = csv.reader(csvfile)
    if name in csvfile:
        print('{}\'s birthday is {}.'.format(name, filename[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

parser = argparse.ArgumentParser()
parser.add_argument("input_name", help = "Insert name to get birthday")
parser.add_argument ("-v", "--verbose", help = "increase verbosity", default= False, action = "store_true")
parser.add_argument ("input_surname", help = "Insert surname")
args = parser.parse_args()

full_name = args.input_name + " " + args.input_surname

if args.verbose == True:
   print ("verbosity turned on")

def return_birthday(name):
    with open(filename, 'r') as csvfile:
         csvreader = csv.reader(csvfile)
    print (csvfile[name])

return_birthday(full_name)
