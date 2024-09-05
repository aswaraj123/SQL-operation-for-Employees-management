import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

mycr=mydb.cursor()
mycr.execute('use class' )

def display():
    mycr.execute('select * from det')
    r=mycr.fetchall()
    for i in r:
        print(i)
def add():
    id=int(input('Enter ID: '))
    name = input('Enter name: ')
    age = int(input('Enter age:'))
    sal = int(input('Enter salary: '))
    sql='Insert into det(id,name,age,salary) values(%s,%s,%s,%s)'
    val=(id,name,age,sal)
    mycr.execute(sql,val)
    mydb.commit()
    print('Inserted successfully')
def edit():
    id=int(input('Enter ID: '))
    name = input('Enter name: ')
    age = int(input('Enter age:'))
    sal = int(input('Enter salary: '))
    mycr.execute("update det set name=%s,age=%s,salary=%s where id=%s",(name,age,sal,id))
    mydb.commit()
    print('Updated successfully')

def delete():
    id = int(input('enter id of empoyee to be deleted: '))
    mycr.execute('delete from det where id=%s',(id,))
    mydb.commit()

ch=0 
while ch!=5:
    print('Menu')
    print('Please select your input')
    print('''1.List
2.Add
3.Edit
4.Delete
5.Exit''')
    ch = int(input('Select your choice :'))
    if ch==1:
       display()
    elif ch==2:
        add()
    elif ch==3:
        edit()
    elif ch==4:
        delete()
if ch==5:
    exit()
        
    ch = int(input('Select your choice :'))
