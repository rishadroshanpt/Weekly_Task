from data import *
from admin import *
from user import *
def login():
    f=0
    uname=input('Enter your usernmae : ')
    passwd=input('Enter your password : ')
    if uname=='admin' and passwd=='admin':
        f=1
    user=''
    for i in users:
        if uname==i['username'] and passwd==i['password']:
            f=2
            user=i
    return f,user