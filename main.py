#! /usr/bin/env python3

import sys
from birthdays import return_birthday
if len (sys.argv)==3:
  name= str(sys.argv[1])
  surname= str(sys.argv[2])
  user_input= name+" " + surname

return_birthday(user_input)

