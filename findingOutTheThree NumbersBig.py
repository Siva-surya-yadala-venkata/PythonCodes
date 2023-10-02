#Finding Out The Numbers in 3 Numbers which are big

num1=int(input("Enter the First Number"))
num2=int(input("Enter The Second Number"))
num3=int(input("Enter The Third Number"))

if num1 > num2 and num1 > num3:
    print("The Number The First Which You Entered",num1,"Is Big Than Both The Numbers",num2,num3)
elif num2 > num1 and num2 > num3:
    print("The Number The Second Which You Entered",num2,"Is Big Than The Both The Numbers",num1,num3)
else:
    print("The Number The Third Which You Entered",num3,"Is Big Than The Both The NUmbers",num1,num2)

print("THANK YOU!!")
