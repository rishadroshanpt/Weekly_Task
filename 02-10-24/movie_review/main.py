from signUp import *
from data import *
from login import *
from admin import *
from user import *
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
        f,user=login()
        if f==0:
            print('Invalid username or password !')
        elif f==1:
            print('Admin Login .')
            while True:
                print(
            '''
1.Add movie
2.View movies
3.View users
4.Delete movie
5.Exit
'''
        )
                ch=int(input('Enter your choice : '))
                if ch==1:
                    add_movie()
                elif ch==2:
                    view_movies()
                elif ch==3:
                    view_users()
                elif ch==4:
                    view_movies()
                    delete_movie()
                elif ch==5:
                    break
                else:
                    print('Invalid choice  !')
        elif f==2:
            print('User Login !')
            while True:
                print(
'''
1.View movies
2.Rate movie
3.View user
4.Update user
5.Exit
'''
                )
                ch=int(input('Enter your choice : '))
                if ch==1:
                    view_movies()
                elif ch==2:
                    view_movies()
                    rate_movie(user)
                elif ch==3:
                    view_user(user)
                elif ch==4:
                    update_user(user)
                elif ch==5:
                    break
                else:
                    print('Invalid choice !')
    elif ch==3:
        break
    else:
        print('Invalid choice  !')