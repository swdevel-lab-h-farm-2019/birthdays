'''we have a file birthdays where we can clearly see the list of (in this case)
 5 people: Albert Einstein,Benjamin Franklin,Ada Lovelace,
Donald Trump and Rowan Atkinson. In relation with their date of birth. 
There are two functions: print_birthdays and return_birthdays. 

The first function print a personalized message
( in this case "Welcome to the birthday..."),
then there is a 'for' cycle that print every name in birthdays.

The second function use a 'if/else' cycle where, 
if the name that I insert is in birthdays, it will print the name followed by the date of birth, 
otherwise there is the command "else", that it will print 'Sadly, we don't have {}\'s birthday.' '''

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

