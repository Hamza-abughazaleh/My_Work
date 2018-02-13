def func():
    return 1

print(func())

s='Global Variable'
def func2():
    print(locals())
    print('\n')
    print(globals())
    print('\n')
    print(globals().keys())
    print('\n')
    print(globals()['s'])

func2()

def hello(name="hamza"):
    return 'hello '+name
print(hello())

greet = hello

print(greet())


def hello2(name="hamza"):
    print ('The hello2() funcction has been execute')

    def greet2():
        return ('\t This is inside the greet() function')
    def welcome():
        return ("\t This is inside the welcome() function")

hello2()
#welcome()

def hello3(name="hamza"):
    def greet():
        return ("\t this is inside the greet() function")
    def welcome():
        return ("\t This is inside the welcome() function")
    if name=="hamza":
        return greet()
    else:
        return welcome()
x=hello3()
print(x)

def hello4():
    return ("hi hamza")
def other(func):
    print ("other code would go here")
    print(func())

other(hello4)

def new_decorator(func):

    def wrap_func():
        print("code would be here, before executing the func")

        func()
        print("code here will execute after the func()")
    return (wrap_func)
#def func_need_decorator():
    #print("this function is in need of a decorator")

#func_need_decorator()
#func_needs_decorator = new_decorator(func_need_decorator)
#func_needs_decorator()

@new_decorator
def func_needs_decorator():
      print ("This function is in need of a Decorator")

func_needs_decorator()
