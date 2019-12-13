import sqlite3
import argparse
import hashlib
<<<<<<< HEAD
=======
import csv
>>>>>>> matteo
conn = None
cursor = None

"""---------------------------------------------------------------------------------------------------------------------------------------------------------------"""

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('example-pwd.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
                     (username TEXT, password TEXT,
                      PRIMARY KEY (username))''')

        cursor.execute('''CREATE TABLE wallet
                     (username TEXT, balance INTEGER,
                      PRIMARY KEY (username),
                      FOREIGN KEY (username)
                        REFERENCES user(username))''')

<<<<<<< HEAD

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                                   "(requires -p)", required=False)
    return parser.parse_args()


def save_new_username_correct(username, password):
=======
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)", required=False)
    parser.add_argument('-p', help="the username password", required=True)
    parser.add_argument('-c', help="check for a usernamename and password" "(requires -p)", required=False)
    parser.add_argument("-n", help = "Insert name in quotation marks to get birthday", required=False)
    parser.add_argument ("-v", "--verbose", help = "increase verbosity", default= False, action = "store_true", required=False)
    return parser.parse_args()


def save_new_username(username, password):
>>>>>>> matteo
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?)",
                   (username, digest))
    cursor.execute("INSERT OR REPLACE INTO wallet VALUES (?,?)",
                   (username, 10))
    conn.commit()

<<<<<<< HEAD

def check_for_username_correct(username, password):
=======
args = parse_args()
filename= "Data_file.csv"

def check_for_username(username, password):
>>>>>>> matteo
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                          (username, digest))
    results = rows.fetchall()
    
    if str(username) in str(results):
<<<<<<< HEAD

        if results:
            conn.commit()
            b = cursor.execute ("SELECT balance FROM user JOIN wallet WHERE user.username = wallet.username")
            print( "User is present, password is valid, balance is %s" % b.fetchall()[0][0])
        else:
            print ("User is not present, or password is invalid")
=======
        if results:
            conn.commit()
            with open(filename) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["name"] == args.n:
                        print ("Welcome " +args.c+ ", the birthday of " + args.n+ " is: " +row['date_birth'])
        else:
            print ("Name is not present, or password is invalid")
>>>>>>> matteo

    else:
        print ("Unrecognised User, please try again")

<<<<<<< HEAD
=======

args = parse_args()
open_and_create()
if args.a and args.p:
    save_new_username(args.a, args.p)
    print ("Thanks for registering: you can now access the database with your credentials, use -c *username* and -p *password* to login, plus -n *name* to know name's birthday")
elif args.c and args.p:
    check_for_username(args.c, args.p)
conn.close()







"""
>>>>>>> matteo
#add name argument to be asked

args = parse_args()
open_and_create()
if args.a and args.p:
    #save_new_username_vulnerable(args.a, args.p)
    save_new_username_correct(args.a, args.p)
elif args.c and args.p:
    #check_for_username_vulnerable(args.c, args.p)
    check_for_username_correct(args.c, args.p)
conn.close() 
<<<<<<< HEAD

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------"""
=======
"""

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""
filename= "Data_file.csv"
def get_names(filename):
    rows = []

    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in enumerate(reader):
            rows += [ [x for x in row.values()] ]
    return rows

names = get_names(filename)
print ('Welcome to the birthday dataset. We know the birthdays of these people:')
print ("names:", [names[n][0] for n in range(5)])

parser = argparse.ArgumentParser()
parser.add_argument("-n", "name", help = "Insert name in quotation marks to get birthday")
parser.add_argument ("-v", "--verbose", help = "increase verbosity", default= False, action = "store_true")
args = parser.parse_args()

with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    count=0
    for i,row in enumerate(reader):
        if i==10:break
        for k,v in row.items():
            if v == args.name:
                print('the birthday of '+ args.name+ " is: " +row['date_birth'])
            else:
                count+=1
        if count>= 5: 
            print: ("Sadly we don't have "+ args.name+ "'s birthdays")
"""
>>>>>>> matteo
