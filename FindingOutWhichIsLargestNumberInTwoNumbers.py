#Take two numbers a and b from the user and sepending upon values of a and b , print one of the following output:
#a) a is greater  b)b is greater c) a and b are same
num1=int(input("Enter the First Number "))
num2=int(input("Enter The Second Number"))

if num1 > num2:
    print("The Number You Entered First",num1,"is greater than the Second Number",num2)
elif num1 < num2:
    print("The Number You Entered Second",num2,"is Greater than First Number",num1)
else:
    print("The Both Numbers First and Second numbers are equal",num1,"=",num2)