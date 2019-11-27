import argparse

birthdays = {
    'Albert Einstein'  : '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace'     : '12/10/1815',
    'Donald Trump'     : '06/14/1946',
    'Rowan Atkinson'   : '01/06/1955'}

parser = argparse.ArgumentParser()
parser.add_argument("input_name", help = "Insert name to get birthday")
parser.add_argument ("-v", "--verbose", help = "increase verbosity", default= False, action = "store_true")
parser.add_argument ("input_surname", help = "Insert surname")
args = parser.parse_args()
full_name = args.input_name + " " + args.input_surname

if args.verbose == True:
   print ("verbosity turned on")



def return_birthday(name):
    print (birthdays[name])

return_birthday(full_name)

"""
----------------

import argparse

birthdays = {
    'Albert Einstein'  : '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace'     : '12/10/1815',
    'Donald Trump'     : '06/14/1946',
    'Rowan Atkinson'   : '01/06/1955'}

parser = argparse.ArgumentParser()
parser.add_argument("test1", help = "test 1")
parser.add_argument("--test2", help = "test 2")
parser.add_argument("--test3", help = "test 3")
args = parser.parse_args()

print(args)

'''if len(args) == 3:
    name = str(args[0])
    surname = str(args[2])
    name_surname = name + " " + surname
    def return_birthday(name):
        print (birthdays[name])


    return_birthday(namesurname)'''



 
'''counter = len(args.test1) + len(--test2) + len(--test3)

if counter == 3:
    namesurname = str(args.test1)+" " + str(--test3)

    def return_birthday(name):
        print (birthdays[name])


    return_birthday(args.namesurname)
elif counter == 1:
    
    def return_birthday(name):
        print (birthdays[name])
    
    return_birthday(args.test1)
else:
    print("WARNING: wrong input")
    print("the format is: Name Surname")'''
"""
