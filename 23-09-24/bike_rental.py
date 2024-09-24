def register_user():
    if len(users)==0:
        id=1001
    else:
        id=users[-1]['id']+1
    email=input('Enter your email : ')
    f=0
    for i in users:
        if email==i['email']:
            f=1
            print('User already exists !')
            register_user()
    if f==0:
        username=email
        name=input('Enter your name : ')
        phone=int(input('Enter your mobile number : '))
        password=input('Set password : ')
        bike=[]
        users.append({'id':id,'name':name,'username':username,'email':email,'phone':phone,'password':password,'bike':bike})
def login():
    username=input('Enter your username : ')
    passwd=input('Enter your password : ')
    f=0
    if username=='admin' and passwd=='admin':
        f=1
    user=''
    for i in users:
        if username==i['username'] and passwd==i['password']:
            f=2
            user=i
    return f,user
def add_bike():
    if len(bikes)==0:
        b_id=501
    else:
        b_id=bikes[-1]['b_id']
        b_name=input('Enter the name of the bike : ')
        f=0
        for i in bikes:
            if b_name==i['b_name']:
                f=1
                print('Bike already exists .')
        if f==0:
            b_brand=input('Enter the brand name of the bike : ')
            b_model=int(input('Enter the bike model : '))
            b_rent=int(input('Enter the rental rate for 1 day : '))
            bikes.append({'b_id':b_id,'b_brand':b_brand,'b_name':b_name,'b_model':b_model,'b_rent':b_rent})
def view_bikes():
    print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID','BRAND','NAME','MODEL','RENT'))
    print('-'*50)
    for i in bikes:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['b_id'],i['b_brand'],i['b_name'],i['b_model'],i['b_rent']))

bikes=[{'b_id':501,'b_brand':'ducati','b_name':'ducati','b_model':2018,'b_rent':1800}]
users=[{'id':1001,'name':'roshan','username':'rish','email':'rish','phone':124,'password':'123'}]
while True:
    print('''
1.Register
2.Login
3.Exit
          ''')
    ch=int(input('Enter your choice : '))
    if ch==1:
        register_user()
    elif ch==2:
        f,user=login()
        if f==0:
            print('Invalid username or password !')
        elif f==1:
            print('Admin Login .')
            while True:
                print('''
1.Add bike
2.View bikes
3.Update bikes
4.View Users
5.Delete bike
6.Logout
''')
                ch=int(input('Enter your choice : '))
                if ch==1:
                    add_bike()
                elif ch==2:
                    view_bikes()
                elif ch==6:
                    break
        elif f==2:
            print('User login .')

    elif ch==3:
        break
