from signUp import *
from data import *
from login import *
while True:
    print(
'''
1.Sign Up
2.Login
3.Exit
'''
    )
    ch=int(input('Enter your choice : '))
    if ch==1:
        signup()
    elif ch==2:
        login()
    elif ch==3:
        break
    else:
        print('Invalid choice !')