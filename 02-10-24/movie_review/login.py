from data import *
def login():
    uname=input('Enter your usernmae : ')
    passwd=input('Enter your password : ')
    if uname=='admin' and passwd=='admin':
        print(users)
    