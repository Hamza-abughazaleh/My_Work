x = 25
def my_func():
    x=50
    return x


print(x)
print(my_func())
my_func()
print(x)

#####################
#LOCAL
name ="this is a global name"

def greet():
    name="summy"

    def hello():
        print("hello "+name)

    hello()

greet()
print(name)

########################
x = 50

def func(x):
    print('x is:',x)
    x=1000
    print('local x changed to:',x)

func(x)
print(x)

y = 50

def func():
    global y
    y=1000


print(y)
func()
print(y)
