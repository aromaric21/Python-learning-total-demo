# Simple Signup and Signin System

users = {}

def signup():
    username = input("Create Username: ")
    password = input("Create Password: ")

    if username in users:
        print("Username already exists")
    else:
        users[username] = password
        print("Sign-up successful!!!")
signup()

def signin():
    username = input("Create Username: ")
    password = input("Create Password: ")

    if username in users and users[username] == password:
        print("Login successful!!!")
    else:
        print("Username or password incorrect. Try again!")
signin()
