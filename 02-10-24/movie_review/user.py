from login import *
from data import *
def rate_movie(user):
    id=input('Enter id of the movie that you want to rate : ')
    f=0
    for i in movies:
        if id==i['m_id']:
            f=1
            rating=float(input('Enter your rating out of 5 : '))
            if rating<=5:
                i['l'].append(rating)
                rt=0
                for j in i['l']:
                    rt+=j
                rtn=(rt/len(i['l']))
                print(i['l'],rtn,len(i['l']))
                i['m_rating']=rtn
                user['movie'].append(i['m_id'])
            else:
                print('Rating is larger than 5 !')
    if f==0:
        print('Id not found !')
def view_user(user):
    # users=[{'id':1001,'username':'rish','email':'rish','name':'roshan','phone':12345678,'password':'123','movie':[]}]
    print('-'*20,'USER DETAILS','-'*20)
    print('ID     :   ',user['id'])
    print('NAME     :   ',user['name'])
    print('USERNAME     :   ',user['username'])
    print('EMAIL     :   ',user['email'])
    print('PHONE     :   ',user['phone'])
    print('REVIEWED MOVIE     :   ',user['movie'])
def update_user(user):
    while True:
        print(
'''
1.Change name
2.Change username
3.Change email
4.Change phone no
5.Change Password
6.Exit
'''
        )
        ch=int(input('Enter your choice : '))
        if ch==1:
            newName=input('Enter new name : ')
            user['name']=newName
            print('Name changed successfully !')
        elif ch==2:
            newUsername=input('Enter new username : ')
            user['username']=newUsername
            print('Username changed successfully !')
        elif ch==3:
            newMail=input('Enter new email : ')
            user['email']=newMail
            print('Email changed successfully !')
        elif ch==4:
            newPhone=input('Enter new phone number : ')
            user['phone']=newPhone
            print('Phone no changed successfully !')
        elif ch==5:
            passwd=input('Enter your current password : ')
            if passwd==user['password']:
                newPasswd=input('Enter new password : ')
                user['password']=newPasswd
                print('Password changed successfully !')
            else:
                print('Invalid password')
        elif ch==6:
            break
