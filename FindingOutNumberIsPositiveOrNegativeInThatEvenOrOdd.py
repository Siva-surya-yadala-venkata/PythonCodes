#Here We are Going to find Out the whether the Number is Positive Even , Postive Odd , Negative Even , Negative Odd , Or Zero

number=int(input("Enter the Number to Verify In the Conditions Above "))
#POSITIVE EVEN OR ODD

#Method 1:
if(number > 0): #Positive Form
    print("The Number is",number,"Positive")
    if(number % 2==0):
        print("The Number is",number,"is Positive Even")
    else:
        print("The Number is Positive but",number," is Positive odd")
#For Positive Even and Positive Odd
elif(number < 0):#For Negative Form
    print("The Number You entered",number,"is Negative")
    if(number %2 == 0):
        print("The Number You Entered is",number,"Negative Even")
    else:
        print("The Number You Entered is",number,"is Negative Odd")
#For Negative Even and Negative Odd
else:
    print("You Entered Number is",number,"is Zero")

#Method 2:
if number > 0 and number % 2==0:
    print("The Number You Entered is",number,"Positive Even")
elif number > 0 and number % 2==1:
    print("The Number You Entered is",number,"Positive Odd")
elif number < 0 and number % 2==0:
    print("The Number You Entered is",number,"Negative Even")
elif number < 0 and number % 2==1: 
    print("The Number You Entered is",number,"Negative Odd")
else:
    print("The Number You Entered is ",number,"Zero") 