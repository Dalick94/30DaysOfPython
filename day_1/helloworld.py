#EXERCISES LEVEL 1 AND 2
#1. Check the python version you are using
print("I am using 3.12 version of Python")

#2. Open the python interactive shell and do the following operations. The operands are 3 and 4
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3%2)
print(3//2)
print(3**2)

#3. Write strings on the python interactive shell. The strings are the following
print("Guillermo")
print("Vivancos")
print("Spain")
print("I am enjoying 30 Days of Python")

#4. Check the data types of the following data
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Guillermo"))
print(type("Vivancos"))
print(type("Spain"))



#EXERCISES LEVEL 2

#1. Write an example for different Python data types such as Number(Integer, Float, Complex), 
#String, Boolean, List, Tuple, Set and Dictionary.
3
3.5
3 + 3j
"Guillermo"
True
[1, 2, 3, 4]
(1, 2, 3, 4)
{2, 4, 1, 4}
{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}

#2. Find an Euclidian distance between (2, 3) and (10, 8)
#print(math.dist(2, 3))
#print(math.dist(10, 8))

#Inicializiting
x1 = 2
x2 = 3
y1 = 10
y2 = 8

#Calculating Euclidian distance
distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

# printing Euclidean distance
print("The Euclidiean distance between (2, 3) and (10, 8) is: ", distance)