from login import *
from data import *
def rate_movie(user):
    id=input('Enter id of the movie that you want to rate : ')
    f=0
    for i in movies:
        f=1
        if id==i['m_id']:
            rating=float(input('Enter your rating out of 5 : '))
            if rating<=5:
                i['m_rating']=rating
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