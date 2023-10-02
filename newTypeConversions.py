#Type Conversions are of two types 1)Implicit 2)Explicit Conversions
#1)Implicit Type Conversions are can done without us it is directly done by the python only
#2)Explicit Type Conversion is done By the Us like we need to Convert Tuple into list  or etc ..

#1)Implicit Conversions
a,b=10,20.5
print(a+b,type(a+b))
c,d=True,20
print(c+d,type(c+d))

#2)Explicit Conversions
#Program Converting into List into Tuple ,Set,String
l=[1,2,3]
#Converting List into String
string=str(l)
print(string,type(string))
#Converting List Into Tuple
t=tuple(l)
print(t,type(t))
#Converting List Into Set
s=set(l)
print(s,type(s))

#Converting Tuple into List,String,Set
t=('a','b','c')
#Converting Tuple into String
string=str(t)
print(string,type(string))
#Converting Tuple into List
l=list(t)
print(l,type(l))
#Converting Tuple into Set
s=set(t)
print(s,type(s))

#Converting Set into List,Tuple,String
s={'a','b','c'}
#Converting set into String
string=str(s)
print(string,type(string))
#Converting Set into List
l=list(s)
print(l,type(l))
#Converting Set into Tuple
t=tuple(s)
print(t,type(t))

#Converting String Into List ,Tuple,Set
string="surya"
#Converting String into List
l=list(string)
print(l,type(l))
#Converting String into Tuple
t=tuple(string)
print(t,type(t))
#Converting String into Set
s=set(string)
print(s,type(s))

#Program Converting String into Integer
string="135"
integer=int(string)
print(integer,type(integer))

f=float(string)+10
print(f,type(f))

#Converting String into List
l=['a','b','c']
string=str(l)
print(string,type(string))

str1="10"
str2="20"
print(str1+str2)
#Converting string into integer and then adding both
print(int(str1)+int(str2),type(int(str1)+int(str2)))

#Converting String into float
string="20.5"
f=float(string)
print(f,type(f))

#Converting Integer into Binary,HexaDecimal,Octal
integer=10
print(bin(integer))
print(hex(integer))
print(oct(integer))

#Converting Binary , Hexa Decimal, Octal into Integer
#Converting Binary into Integer
#If They given Number
binary="10001"
integer=int(binary,2)#Here 2 represents the binary to integer conversion
print(integer,type(integer))
#Converting HexaDecimal into Integer
hexaDecimal="A1"
integer=int(hexaDecimal,16)
print(integer,type(integer))
#Converting Octal to Integer
octal="12"
integer=int(octal,8)
print(integer,type(integer))

#Conerting Single Character into the ASCII value by ord()
val1="a"
varma1=ord(val1)
print(varma1,type(varma1))

val2="1"
varma2=ord(val2)
print(varma2,type(varma2))

varma=varma1+varma2
print(varma)

conversionAscii=chr(varma)
print(conversionAscii)

val=98
varma=chr(val)
print(varma)

# Python code to demonstrate Type conversion
# using  dict(), complex(), str()
  
# initializing integers
a = 1
b = 2
  
# initializing tuple
tup = (('a', 1) ,('f', 2), ('g', 3))
  
# printing integer converting to complex number
c = complex(1,2)
print ("After converting integer to complex number : ",end="")
print (c)
  
# printing integer converting to string
c = str(a)
print ("After converting integer to string : ",end="")
print (c)
"""THis is Surya""" 
# printing tuple converting to expression dictionary
c = dict(tup)
print ("After converting tuple to dictionary : ",end="")
print (c)

#Program Converting Set into Dictionary
set_to_dictionary={('a',1),('b',2),('c',3)}
dictionary=dict(set_to_dictionary)
print(dictionary,type(dictionary))

#Program Converting List into Dictionary
list_to_Dictionary=[('a',1),('b',2),('c',3)]
dictionary=dict(list_to_Dictionary)
print(dictionary,type(dictionary))
