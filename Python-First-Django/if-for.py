if 1<2:
    print('yes!')
########################
if 1<2:
    print('First Block')
    if 20<3:
        print('Second Block')
#########################
if 1 == 1:
    if 1 > 2:
        print('hello')
    elif 3 == 3:
        print('elif ran')
    else:
        print('last')
#########################


#FOR LOOPS
#loop list
seq =[1,2,3,4,5,6]
for item in seq:
    #code here
    print(item)

seq =[1,2,3,4,5,6]
for item in seq:
    #code here
    print('hello')

seq =[1,2,3,4,5,6]
for hamza in seq:
    #code here
    print(hamza)

#end list LOOPS

#loop DECTIONARIES
d={"sam":1,"frank":2}
for k in d:
    print(k)
    print(d[k])


myparis = [(1,2),(3,4),(5,6)]
for x,y in myparis:
    print(x)
    print(y)

myparis = [(1,2),(3,4),(5,6)]
for item in myparis:
    print(item)

i=1
while i<5:
    print("i is:{}".format(i))
    i=i+1

x=[1,2,3,4]
out=[]
for num in x:
    out.append(num**2)

print(out)
##############################

for item in range(10):
    print(item)


a = [[1, 2, 3], [4,5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        if(j == i):
            print(a[i][j], end=' ')
            #print(a[i][j], end=' ')
    if(i != j):
        print(a[i][-1], end=' ')
    else:
        print(a[i][0], end=' ')
    print()
print (a[0][0] , end = '   ')
print (a[0][2])
print (' ',a[1][1])
print (a[2][0], end = '   ')
print (a[2][2])
