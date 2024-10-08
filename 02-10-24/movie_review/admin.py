# movies=[{'m_id':'m501','m_name':'solo','m_year':2017,'m_dir':'Bijoy Nambiar','m_rating':3.4}]
from login import *
from data import *
def add_movie():
    if len(movies)==0:
        m_id='m501'
    else:
        a=int(movies[-1]['m_id'][1:])   
        b=movies[-1]['m_id'][:1]
        m_id=b+str(a+1)
        mName=input('Movie name : ')
        f=0
        for i in movies:
            if i['m_name']==mName:
                print('Movie Already exists !')
                f=1
        if f==0:
            mYear=int(input('Release year : '))
            mDir=input('Director name : ')
            mRating=float()
            movies.append({'m_id':m_id,'m_name':mName,'m_year':mYear,'m_dir':mDir,'m_rating':mRating})
def view_movies():
    print(('{:<10}{:<20}{:<10}{:<20}{:<10}').format('ID','NAME','YEAR','DIRECTOR','RATING'))
    print('-'*70)
    for i in movies:
        print(('{:<10}{:<20}{:<10}{:<20}{:<10}').format(i['m_id'],i['m_name'],i['m_year'],i['m_dir'],i['m_rating']))
def view_users():
    # users=[{'id':1001,'username':'rish','email':'rish','name':'roshan','phone':12345678,'password':'123'}]
    print(('{:<10}{:<20}{:<20}{:<20}{:<10}').format('ID','USERNAME','EMAIL','NAME','PHONE'))
    print('_'*80)
    for i in users:
        print(('{:<10}{:<20}{:<20}{:<20}{:<10}').format(i['id'],i['username'],i['email'],i['name'],i['phone']))
def delete_movie():
    id=input('Enter id of the movie that you want to delete : ')
    f=0
    for i in movies:
        if id==i['m_id']:
            f=1
            movies.remove(i)
            print('Movie removed successfully !')
    if f==0:
        print('Id not found !')