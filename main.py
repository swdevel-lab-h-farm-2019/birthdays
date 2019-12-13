import argparse
import csv

filename= "Data_file.csv"
def get_names(filename):
    rows = []

    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for i,row in enumerate(reader):
            rows += [ [x for x in row.values()] ]
    return rows

names = get_names(filename)
print ('Welcome to the birthday dataset. We know the birthdays of these people:')
print ("names:", [names[n][0] for n in range(5)])

parser = argparse.ArgumentParser()
parser.add_argument("input_name", help = "Insert name to get birthday")
parser.add_argument ("-v", "--verbose", help = "increase verbosity", default= False, action = "store_true")
parser.add_argument ("input_surname", help = "Insert surname")
args = parser.parse_args()

full_name = args.input_name + " " + args.input_surname

with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    count=0
    for i,row in enumerate(reader):
        if i==10:break
        for k,v in row.items():
            if v == name:
                print('the birthday of '+ name+ " is: " +row['date_birth'])
            else:
                count+=1
        if count>= 5: 
            print: ("Sadly we don't have "+ name+ "'s birthdays")

#import sys
#from birthdays import return_birthday
#if len (sys.argv)==3:
  #name= str(sys.argv[1])
  #surname= str(sys.argv[2])
  #user_input= name+" " + surname
#return_birthday(user_input)

