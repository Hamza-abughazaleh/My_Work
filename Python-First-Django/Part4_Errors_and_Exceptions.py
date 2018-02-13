print('Heloo')

try:
    f=open('testfile','w')
    f.write('test write this')
except IOError:
    print("Error: Colud not find file or read data")
else:
    print("Content Written Successfully")
    f.close()

try:
    f=open('testfile','r')
    f.write('test write this')
except IOError:
    print("Error:Could not find file or read data")
else:
    print("content Written Successfully")
    f.close

try:
    f=oper('testfile','r')
    f.write("Test write this")
except:
    print("Error:Colud not find file or read data")
else:
    print("content Written Successfully")
    f.close

try:
    f=open("testfile","w")
    f.write=("test write statement")
finally:
    print("Always execute finally code blocks")
    
