def power(number):
    if(number == 0):
        return False
    else:
         while(number % 2 == 0):
           number = number / 2
         if(number > 1):
             return False
         else:
            return True

number = int(input("enter a integer number must be integer: "))
print(number)
print(power(number))

def palindromic(num):
  #rev = 0
  #while num > 0:
    #rev = (10*rev) + num%10
    #num //= 10
    #print(num)
  #return rev
  b = str(num)
  print(len(b))
  x = len(b)
  i=0;
  while( i<(x-1)/2 ):
    if b[i]==b[x-i-1]:
        print(b[x-i-1])
        i=i+1
    else:
        return False
  return True

number = int(input("enter a integer number must be integer: "))
print(number)
print(palindromic(number))


class Node(object):
    def __init__(self,d,n=None):
        self.data = d
        self.next_node = n
class LinkedList(object):
    def __init__(self, r = None , t = None):
            self.root=r
            self.tail = t
    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        if(self.tail == None):
            self.tail = self.root

    def find(self,d):
        this_node = self.root
        while this_node:
            if this_node.data == d:
                print(this_node.tail)
                return d
            else:
                print(this_node.data)
                this_node = this_node.next_node
        return None



MyList = LinkedList()
MyList.add(5)
MyList.add(8)
MyList.add(10)
MyList.add(12)
print(MyList.find(5))
