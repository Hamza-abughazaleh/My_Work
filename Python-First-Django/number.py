print((2+10) * (10+3))
a = 5
print(a+a)
a = a*5

#comment
print(a) #comment

#another example1
my_income = 100
tax_rate = 0.1
My_taxes = my_income * tax_rate
print(My_taxes)
#end

'hello'
"hello"

mystring="ABCDERG"
print(mystring)

print(mystring[0])

print(mystring[-1])#print final digit

print(mystring[2:])

print(mystring[:3])

print(mystring[2:5])#print digit between 2 and 5

print(mystring[::2])#skipping two digit

print(mystring[::3])

#mystring[0]='x'

x = mystring.lower()#.upper
mystring=  mystring.lower()
mystring.lower()#don't change any thing
print(mystring)
print (x)

#print formatting

x="insert any thing {} " .format("hahahaha")
print(x)

x="item one: {} item tow: {} " .format("dog" , "cat")
print(x)

x="item one: {x} item tow: {y} " .format(x="dog" ,y= "cat")
print(x)

#list

mylist=[1,2,3]
print(len(mylist))
mylist=['sdfasdfsdf',1,2,3,4,20.1,True,'sdfsf',[1,2,3]]
print(len(mylist))
print(mylist)

mylist=['a','b','c','d','e']
print(mylist[-1])

mylist=['a','b','c','d','e']
mylist[0]="NEW ITEM"
print(mylist)

mylist=['a','b','c','d','e']
mylist.append("NEW ITEM")
print(mylist)

mylist=['a','b','c','d','e']
mylist.append(['x','y','z'])
print(mylist)

mylist=['a','b','c','d','e']
mulist2=['x','y','z']
mylist.extend(mulist2)
print(mylist)

mylist=['a','b','c','d','e']
mylist.extend(['x','y','z'])
print(mylist)

mylist=['a','b','c','d','e']
item = mylist.pop()
print(mylist)
print(item)

mylist=['a','b','c','d','e']
item = mylist.pop(0)
print(mylist)
print(item)

mylist=['a','b','c','d','e']
mylist.reverse()
print(mylist)

mylist=[1,2,3,50,74,20,5,8]
mylist.sort()
print(mylist)

mylist=[1,2,['a','b','c','d','e']]
print(mylist[2][1])

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#list COMPREHENSION
first_col= [row[0]for row in matrix]
print(first_col)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#list COMPREHENSION
first_col= [row[1]for row in matrix]
print(first_col)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#list COMPREHENSION
first_col= [row for row in matrix]
print(first_col)
#end list

#DECTIONARIES
my_stuff={"key1":123,"key2":'value2',"key3":{'1230':[1,2,"Grabme"]}}
print(my_stuff)

my_stuff={"key1":123,"key2":'value2',"key3":{'1230':[1,2,"Grabme"]}}
print(my_stuff['key3']['1230'][2].upper())

my_stuff={'lunch':'pizza' , 'bfast':'eggs'}
my_stuff['lunch']='burger'
my_stuff['dinner']='pasta'
print(my_stuff['lunch'])
print(my_stuff)
#end DECTIONARIES


#booleans

True
False

#Tuples
t = (1,2,3)
print(t[0])

t=('a',True,123)
print(t)
#t[0]="NEW"

#Sets

x= set()
x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
x.add(4)
x.add(4)
print(x)

converted = set([1,1,1,1,1,1,1,2,2,2,21,3,3,3,3,])
print(converted)
