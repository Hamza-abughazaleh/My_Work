
####fanction to take the list and send it to function quicksorthlp and send 3 attributes list/0/len-1
def quicksort(data_list):
    quicksorthlp(data_list,0,len(data_list)-1)


def quicksorthlp(data_list,first,last):
    if first<last:
        splitpoint = partition(data_list,first,last)

        quicksorthlp(data_list,first,splitpoint-1)
        quicksorthlp(data_list,splitpoint+1,last)

def partition(data_list,first,last):
    pivotvalue = data_list[first]
    leftmark = first+1
    rightmake = last

    done = False

    while not done:

        while leftmark <= rightmake and data_list[leftmark] <=pivotvalue:
            leftmark = leftmark+1

        while data_list[rightmake] >= pivotvalue and rightmake >= leftmark:
            rightmake = rightmake-1

        if rightmake < leftmark:
            done = True
        else:
            temp = data_list[first]
            data_list[first] = data_list[rightmake]
            data_list[rightmake] = temp

    temp = data_list[first]
    data_list[first] = data_list[rightmake]
    data_list[rightmake] = temp

    return rightmake

#######QUICKSORT FUNCTIONS########
####define list#######
data_list=[5,30,40,50,25,80,100,87]
######send list to functon######
quicksort(data_list)
#####print list after sort#######

print(data_list)

def func(data_list):
    less=[]
    equal=[]
    great=[]
    data_list=data_list
    print(data_list)
    pivotvalue = data_list[0]
    print(pivotvalue)
    for i in range(len(data_list)):
        print(data_list[i])
        if data_list[i] < pivotvalue:
            less.append(data_list[i])
        elif data_list[i] == pivotvalue:
            equal.append(data_list[i])
        elif data_list[i] > pivotvalue:
            great.append(data_list[i])
    print (less+equal+great)



data_list2 = [2,8,5,1,4,9,10]
func(data_list2)
