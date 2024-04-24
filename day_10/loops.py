### LOOPS ###

# EXERCISES LEVEL 1 #

#1.
number = 0

while number < 11:
    print(number)
    number = number + 1
    

for number in range(11):
    print(number)


#2.
number = 10
while number > -1:
    print(number)
    number = number -1 


for number in range(10,0):
    print(number)



#3. 
list = ["#", "##", "###", "####", "#####", "######", "#######"]
for i in list:
    print(i)


for i in range(1, 8):
    print("#" * i)



#4. 
for i in range (0,8):
    print("########")


#5.
resultado = 0  
x = 0
for i in range (0,11):
    int_i = int(i)
    x = int_i * int_i
    print(i, "x", i, "=", x)
    
#6.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for elements in list:
    print(elements)

#7. 
for i in range (0,101,2):
    print(i)


#8.
for i in range (0,101,1):
    if i % 2 == 0:
        continue
    print(i)


# EXERCISES LEVEL 2 #
    
#1. 

sum =  0  
for i in range (0,101):
    sum += i
    i += 1
print ("The sum of all number is :", sum)

#2.

sum_pares = 0
sum_impares = 0

for i in range (0,101,1):
    if i % 2 == 0:
        sum_pares += i
        i += 1
    else:
        sum_impares += i
        i += 1

print("La suma total de los numeros pares es :", sum_pares, "La suma total de los impares es :", sum_impares)



### EXERCISES LEVEL 3 ###

#1.
for i in countries:
    if "land" in i:
        print(i)


#2.
list = ['banana', 'orange', 'mango', 'lemon']
for i in list:
    if i == "lemon":
        list.reverse()
        print(list)


#3.


    




