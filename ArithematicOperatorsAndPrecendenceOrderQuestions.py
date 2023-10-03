#Arithematic Operators
#1) precendence
#->      + -                         left to Right   |
#->      * / //                      left to Right   |
#->  **(Exponential Operator)        Right To left   |  THIS IS THE PRECENDENCE IN PYTHON
#                                                    V

#Arithematic Operator
""" First we are doing Addition """
val1=10
val2=20
sum=val1+val2
print(sum)

#Subtraction
difference=val1-val2
print(difference)

#Multiplication
multiplication=val1*val2
print(multiplication)

#Division
division=val1/val2 #Gives The Float Value

#Modulus Operator (Remainder)
remainder=val1 % val2
print(remainder)

#Floor Division (//) gives the output in the form of Integer
floor_Division= val1 // val2
print(floor_Division)


#Let's Go into The Precendence Order
value=5+2*3 # Here the above the precendence increases from up to down so 2*3=6 and add 5 => 6+5 = 11
print(value)

value=5+3*4**2 # Here the Above the Precendence increases from up to down so 4 ** 2=  4 square 2 is 16 *3=48 and then add 5 to it 48 + 5=53
print(value)

value = 5+4-2  #Here The Above there is precendence Order so + - are from left to right so 5+4=9 so subtract 2 from that is 9-2=7
print(value)

value=2**2**2**-1 #Here The Exponential Form takes from Right To Left so 2 **-1 is 0.5 and  2**0.5 is 1.414 so 2**1.414 = 2.66475
print(value)

value=(2**2)**-1 # so 2 ** 2 is 4 so brackets has more precendence  so 4**-1 = 0.25
print(value)






