mobiles=[]
while True:
    print(
        '''
1.Add mobile phone details.
2.Display mobile phone details.
3.Update mobile phone details.
4.Delete mobile phone.
5.Search mobile phone.
6.Exit'''
    )
    ch=int(input('Enter your choice : '))
    if ch==1:
        id=int(input('Enter id of the phone :'))
        brand=input('Enter brand name of the phone : ')
        name=input('Enter name of the phone : ')
        memory=int(input('Enter memory capacity of the phone :'))
        camera=int(input('Enter camera resolution : '))
        price=int(input('Enter price of the phone : '))
        qty=int(input('Enter stock quantity :'))
        mobiles.append([id,brand,name,memory,camera,price,qty])
    elif ch==2:
        print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID','BRAND','NAME','STORAGE','CAMERA','PRICE','QUANTITY'))
        print('-'*65)
        for i in mobiles:
            print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    elif ch==3:
        id=int(input('Enter ID of the phone that you want to update : '))
        f=0
        for i in mobiles:
            if id==i[0]:
                f=1
                while True:
                    print(
                    '''
1.Update Id
2.Update brand name
3.Update name
4.Update storage
5.Update camera resolution
6.Update price
7.Update quantity
8.Exit'''
                    )
                    ch=int(input('Enter your choice : '))
                    if ch==1:
                        new_id=int(input('Enter new  ID : '))
                        i[0]=new_id
                    elif ch==2:
                        new_brand=input('Enter new brand name : ')
                        i[1]=new_brand
                    elif ch==3:
                        new_name=input('Enter new name : ')
                        i[2]=new_name
                    elif ch==4:
                        new_memory=int(input('Enter new memory storage : '))
                        i[3]=new_memory
                    elif ch==5:
                        new_camera=int(input('Enter new camera resolution : '))
                        i[4]=new_camera
                    elif ch==6:
                        new_price=int(input('Enter new price : '))
                        i[5]=new_price
                    elif ch==7:
                        new_qty=int(input('Enter new quantity : '))
                        i[6]=new_qty
                    elif ch==8:
                        break
                    else:
                        print('Invalid choice !')
        if f==0:
            print('Mobile phone not found in list')
    elif ch==4:
        id=int(input('Enter ID of the phone that you want to delete : '))
        f=0
        for i in mobiles:
            if id==i[0]:
                f=1
                mobiles.remove(i)
        if f==0:
            print('Mobile phone not found in list')
    elif ch==5:
        id=int(input('Enter ID of the phone that you want to search : '))
        f=0
        for i in mobiles:
            if id==i[0]:
                f=1
                print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID','BRAND','NAME','STORAGE','CAMERA','PRICE','QUANTITY'))
                print('-'*65)
                print('{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        if f==0:
            print('Mobile phone not found in list')
    elif ch==6:
        break
    else:
        print('Invalid Choice !')