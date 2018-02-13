#genarat the random
import random

digits = list(range(10))
random.shuffle(digits)
print(digits[:3])
shuffle_value=digits[:3]
#End Genarate

#enter numbers
guess =int( input("What is your guess?"))
#End

#check if the numbers are integers
def check(guess2):
        if type(guess2)==type(2) and guess2<=999:

            return(guess2)
        else:
            print("enter integer ,or three digits")
#end function

checkinput=check(guess)

#converting
input_String_Array = str(checkinput)
input_convert_sting = []
for i in input_String_Array :
    input_convert_sting .append (int(i))
print (input_convert_sting )
#End converting

def match(input_convert_sting , shuffle_value ):

    matches=sum(i==j for i,j in zip(shuffle_value, input_convert_sting))
    if(matches>0):
        print("{} matches".format(matches) )
    else:
        close(input_convert_sting , shuffle_value)


def close(input_convert_sting , shuffle_value):
    close=0

    for item1 in input_convert_sting:
        for item2 in shuffle_value:
            if item1==item2:
                close=close+1
    if close > 0:
        print("{} close".format(close))
    else:
        print("none")












match(input_convert_sting , shuffle_value )
