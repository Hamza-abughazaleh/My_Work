#INHERITANCE

class Animal():

    def __init__(self):
        print("sdsdf")

    def whoAmi(self):
        print("dsdcd")

    def eat(self):
        print("dfdsafsa")


class Dog(Animal):

      def __init__(self):
          Animal.__init__(self)
          print("Dog")

mya= Dog()
mya.whoAmi()
mya.eat
