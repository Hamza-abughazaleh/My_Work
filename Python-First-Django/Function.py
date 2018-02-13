def my_func(param1='default'):
    print("my first python function!{}".format(param1))

my_func();

###################
def my_func(param1='default'):
    """
    This is the Docstring
    """
    print("my first python function!{}".format(param1))

my_func();
##################33
def count_evens(nums):
  # CODE GOES HERE
  count=0
  for i in nums:
      if(nums[i]%2==0):
          count=count+1

  print(count)

count_evens5=[2, 1, 2, 3, 4]
count_evens(count_evens5)


def stringBits(str):
  # CODE GOES HERE
  strs=""
  for i in range(len(str)):
      if(i%2==0):
          strs=strs+str[i]
  print(strs)

stringBits2='Hello'
stringBits(stringBits2)

def end_other(a,b):
  # CODE GOES HERE
  a=a.upper()
  b=b.upper()
  if a.endswith(b) or b.endswith(a):
      print(True)
  else:
      print(False)

end_other("Hiabc","abc")

def doubleChar(str):
  # CODE GOES HERE
  result = ''
  for char in str:
      result += char * 2
  return result

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))
