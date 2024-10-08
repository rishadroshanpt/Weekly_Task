from data import users
def signup():
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
            signup()
    if f==0:
        username=email
        name=input('Enter your name : ')
        phone=int(input('Enter your mobile number : '))
        password=input('Set password : ')
        movie=[]
        users.append({'id':id,'name':name,'username':username,'email':email,'phone':phone,'password':password,'movie':movie})
        print('Successfully Sign Up.')
