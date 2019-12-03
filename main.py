#! /usr/bin/env python3

import sys   # Importing SYS module
from birthdays import return_birthday    # From birthdays.py import return_birthday function
if len (sys.argv)==3:                    # If the length of the list containing the command-line arguments passed to the script is longer than 3 (the case in which the user doesn't use quotes when entering the name and surname)
  name= str(sys.argv[1])                 # Create variable 'name' with the first element of the list, right after the script name which is the element zero 
  surname= str(sys.argv[2])              # Create variable 'surname' with the second element of the list
  user_input= name+" " + surname         # Creating a unique variable 'user_input', by concatenating variables 'name' and 'surname'.

return_birthday(user_input)              # Calling the return_birthday function

