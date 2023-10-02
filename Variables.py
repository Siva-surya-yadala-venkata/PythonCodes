#Variables In Python

a=10
b=20
print(a+b)

c=12.5
print(a*b*c)

a,b,c=10,12.5,'Surya'     # In python we can able to assign many variables in an single line with any type of data Type
print(a,b,c,sep="\n") # We can print Multiple things in Python by using sep="\n" prints the variables in separate lines
print(a,b,c)#Print the variables in a single line


e=f=g=10
print(e,f,g)
#The Commas gives default as space

print(e,f,g ,sep=",") # sepearte in between , by commas -> OUTPUT is 10,10,10

a="Yadala Venkata"
b="Siva Surya"
print(a+b,sep="  ") # Here sep can't able to use because a+b takes an variable so i can't give any space prints Yadala VenkataSiva Surya

a=20
b="Surya"
#print(a+b) This gives an Error Because a=integer and b=string can't able add

#In Python we can access the same variable with any data type


istrueornot=True #Without keeping any data Type we can keep an Boolean Variable
print(istrueornot)

# We can use the same variable name with changing into capital letters in variable but C doesn't support it
varma="Surya"
Varma="Surya"# Here we are changing One letter into capital in Variable we can use of this 
print(varma)
print(Varma)
