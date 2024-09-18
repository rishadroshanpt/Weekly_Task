bikes=[]
print('********************************************************************')
print('---------------------SECOND HAND BIKE DEALERSHIP--------------------')
print('********************************************************************')
while True:
    print(
        '''
1.Add bike details.
2.Display bike details.
3.Update bike details.
4.Delete bike.
5.Search bike.
6.Exit'''
    )
    ch=int(input('Enter your choice : '))
    if ch==1:
        id=int(input('Enter id of the bike :'))
        brand=input('Enter brand name of the bike : ')
        name=input('Enter name of the bike : ')
        engine=int(input('Enter engine cc of the bike :'))
        mlg=int(input('Enter average mileage : '))
        model=int(input('Enter model of the bike : '))
        price=int(input('Enter the price of the bike : '))
        qty=int(input('Enter stock quantity :'))
        bikes.append({'id':id,'brand':brand,'name':name,'engine':engine,'mlg':mlg,'model':model,'price':price,'qty':qty})
    elif ch==2:
        print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID','BRAND','NAME','ENGINE','AVG MILEAGE','MODEL','PRICE','QUANTITY'))
        print('-'*75)
        for i in bikes:
            print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['brand'],i['name'],i['engine'],i['mlg'],i['model'],i['price'],i['qty']))
    elif ch==3:
        id=int(input('Enter ID of the bike that you want to update : '))
        f=0
        for i in bikes:
            if id==i['id']:
                f=1
                while True:
                    print(
                    '''
1.Update Id
2.Update brand name
3.Update name
4.Update engine cc
5.Update mileage
6.Update model
7.Update price
8.Update quantity
9.Exit'''
                    )
                    ch=int(input('Enter your choice : '))
                    if ch==1:
                        new_id=int(input('Enter new  ID : '))
                        i['id']=new_id
                    elif ch==2:
                        new_brand=input('Enter new brand name : ')
                        i['brand']=new_brand
                    elif ch==3:
                        new_name=input('Enter new name : ')
                        i['name']=new_name
                    elif ch==4:
                        new_engine=int(input('Enter new engine cc : '))
                        i['engine']=new_engine
                    elif ch==5:
                        new_mlg=int(input('Enter new mileage : '))
                        i['mlg']=new_mlg
                    elif ch==6:
                        new_model=int(input('Enter updated year of the bike : '))
                        i['model']=new_model
                    elif ch==7:
                        new_price=int(input('Enter new price : '))
                        i['price']=new_price
                    elif ch==8:
                        new_qty=int(input('Enter new quantity : '))
                        i['qty']=new_qty
                    elif ch==9:
                        break
                    else:
                        print('Invalid choice !')
        if f==0:
            print('Bike not found in list')
    elif ch==4:
        id=int(input('Enter ID of the Bike that you want to delete : '))
        f=0
        for i in bikes:
            if id==i['id']:
                f=1
                bikes.remove(i)
        if f==0:
            print(' Bike not found in list')
    elif ch==5:
        id=int(input('Enter ID of the Bike that you want to search : '))
        f=0
        for i in bikes:
            if id==i['id']:
                f=1
                print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID','BRAND','NAME','ENGINE','AVG MILEAGE','MODEL','PRICE','QUANTITY'))
                print('-'*75)
                print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['brand'],i['name'],i['engine'],i['mlg'],i['model'],i['price'],i['qty']))
        if f==0:
            print('Bike not found in list')
    elif ch==6:
        break
    else:
        print('Invalid Choice !')