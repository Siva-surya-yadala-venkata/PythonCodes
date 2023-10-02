a=int(input("Enter the value of  "))
print(type(a))

a=10
print(type(a))

a="surya"
print(type(a))
a=input("Enter the String ")
print(type(a))

a=complex(input("Enter the Complex Number "))
print(type(a))

a=3+4j
print(type(a))

a=input("Enter the None /Null")#None
print(type(a))
a=None
print(type(a))

a=bool(input("Enter the Boolean value"))
print(type(a))

a=True
print(type(a))

#Let's Disccus about Lists and Tuples and Sets and Dictionary and string
#Lists means it's an type of array we can able to add and replace in the Numbers reprsented in [square bracket]=list
#Tuples are type of array but here we can't able to change and replace those are immutalable reprsented in(open brackets)=tuples
# Sets are the distinct objects which can't get again re enter in the set like { 2,2 ,3} 2 is only needed to enter one time and helps in hashing so reprsented in {curly brackets }=sets
# Dictionary are having a key and value (key value pairs) the key contains the Integer type and the value contains the String 

str=input("Enter the String")
print(str)

l=list(input("enter the list"))
print(l,"The Type is ",type(l))

l=[6,5,6]
print(l,type(l),sep="The Type of is ")

t=tuple(input("Enter the Tuple "))
print(t,type(t),sep="The type is ")

t=(3,4,5)
print(t,"The Type is ",type(t))

s=set(input("Enter the set values(won't repeat the values)"))
print(s,type(s),sep="The type is ")

s={2,5,6}
print(s,"The Type is ",type(s))

input_str = input("Enter the key and values of the dictionary (key1 value1 key2 value2 ...): ")
input_list = input_str.split()
d = dict(zip(input_list[0::2], input_list[1::2]))
print(d,"The Type is",type(d))

d={2:"Surya",3:"GFG",4:"Varma"}
print(d,type(d),sep="The Type is ")

#lIKE HERE "IS" IS LIKE IF STATEMENT AND "IS NOT" IS LIKE ELSE STATEMENT AT LAST GIVES THE BOOLEAN VALUE
print(2 is 2)#TRUE
print(2 is not 2)#FALSE

print(type([]) is list)
 
print(type([]) is not list)
 
print(type(()) is tuple)
 
print(type({}) is dict)
 
print(type({}) is not list)







