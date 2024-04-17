myint = 8
myfloat = 8.0
num1 = 18
num2 = 7
num3 = 2
mystring = "It's John Birthday!"
print("Integer: %d" % myint)
print("Float: %f" % myfloat)
print("String: %s" % mystring)
mylist = ["Alex", "David", "Peter", "David"]
mytuple = ("Alex", "David", "Peter", "David")
mylist[3] = "John"
print(mylist)
mylist = list(mytuple)
mylist[3] = "Jackson"
mytuple = tuple(mylist)
print(mytuple)
result = (num1 % num2) * num3
output = "Result" + " " + "="
print("%s %d" % (output, result))
num1 = 6
num2 = 2
result = 0

operator = "multiply"
if operator in ["multiply", "divide"]:
    if num1 == 6 and num2 == 2:
        result = num1 * num2
        print("The result is %d" % result)
    else:
        result = num1 / num2
        print("The result is %d" % result)

def MyFirstFunction():
    print("Hello From My First Function!")

def MyFirstFunctionWithInputs(Name, Greeting):
    print("Hi %s!,  %s" % (Name, Greeting))

def Sum(a, b):
    return a + b

MyFirstFunction()

MyFirstFunctionWithInputs("Johnson", "Happy New Year!")

x = Sum(8,9)
print("8 + 9 = %d" % x)
