import sqlite3
import argparse
import hashlib
import csv
conn = None
cursor = None


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

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)", required=False)
    parser.add_argument('-p', help="the username password", required=True)
    parser.add_argument('-c', help="check for a usernamename and password" "(requires -p)", required=False)
    parser.add_argument("-n", help = "Insert name in quotation marks to get birthday", required=False)
    parser.add_argument ("-v", "--verbose", help = "increase verbosity", default= False, action = "store_true", required=False)
    return parser.parse_args()


def save_new_username(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?)",
                   (username, digest))
    cursor.execute("INSERT OR REPLACE INTO wallet VALUES (?,?)",
                   (username, 10))
    print ("Thanks for registering: you can now access the database with your credentials, use -c *username* and -p *password* to login, plus -n *name* to know name's birthday")
    conn.commit()

args = parse_args()
filename= "Data_file.csv"

def check_for_username(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                          (username, digest))
    results = rows.fetchall()
    
    if str(username) in str(results):
        if results:
            conn.commit()
            with open(filename) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row["name"] == args.n:
                        print ("Welcome " +args.c+ ", the birthday of " + args.n+ " is: " +row['date_birth'])
        else:
            print ("Name is not present, or password is invalid")

    else:
        print ("Unrecognised User, please try again")


args = parse_args()
open_and_create()
if args.a and args.p:
    save_new_username(args.a, args.p)
elif args.c and args.p:
    check_for_username(args.c, args.p)
conn.close()