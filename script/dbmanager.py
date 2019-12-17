"""This file creates and populates the password database for the project"""

import sqlite3

import argparse

import hashlib

conn = None

cursor = None


def open_and_create():
    """checking for database and creating it if negative"""
    global conn
    global cursor
    conn = sqlite3.connect('script/example-pwd.db')
    conn = sqlite3.connect('script/pwd.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
                     (username TEXT, password TEXT,
                      PRIMARY KEY (username))''')


def parse_args():
    """storing arguments with argparse module"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password", required=True)
    return parser.parse_args()

args = parse_args()


def save_new_username(username, password):
    """saving provided authenticators for a new user"""
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?)",
                   (username, digest))
    print ("""Thanks for registering: you can now access the
    database with your credentials, use -c *username* and -p
    *password* to login, plus -n *name* to know name's birthday""")
    conn.commit()


args = parse_args()
open_and_create()
if args.a and args.p:
    save_new_username(args.a, args.p)
conn.close()
