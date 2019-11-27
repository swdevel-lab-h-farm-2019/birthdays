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
