# dictionary

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}


# prints the name of the people in the dictionary

# function used to print the person's name + date of birth if the 
# name is in the dictionary. If not it prints no useful answer 

def get_birthday(name):
    if name in birthdays:
        birthdays[name]
    else:
        return None