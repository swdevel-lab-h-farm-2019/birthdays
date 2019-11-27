import argparse

birthdays = {
    'Albert Einstein'  : '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace'     : '12/10/1815',
    'Donald Trump'     : '06/14/1946',
    'Rowan Atkinson'   : '01/06/1955'}

parser = argparse.ArgumentParser()
parser.add_argument("test1", help = "test 1")
#parser.add_argument("test2", help = "test 2")
#parser.add_argument("test3", help = "test 3")
args = parser.parse_args()

def return_birthday(name):
    print (birthdays[name])


return_birthday(args.test1)