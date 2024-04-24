### SETS ### No es una estructura ordenada, no admite repetidos

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24] 


# EXERCISES LEVEL 1
print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Nasa", "Nvidia", "The burger shop"])
it_companies.remove("Facebook")
print(it_companies)
#5. What is the difference between remove and discard (Discard never return an error)


# EXERCISES LEVEL 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B


# EXERCISES LEVEL 3
print(len(age))
print(len(set(age))) # El largo del set es mas corto porque no admite repetidos

"""
Explain the difference between the following data types: string, list, tuple and set
STRING: Un string es una cadena de caracteres, siempre se escriben entre comillas.
LIST: La lista es un conjunto de valores ordenado que puede modificarse (PERMITE DUPLICADOS)
TUPLE: La lista es un conjunto de valores ordenado que NO puede modificarse (PERMITE DUPLICADOS)
SET: Un set es un conjunto de valores desordenado que NO puede modificarse, aunque si se pueden añadir valores (NO PERMITE DUPLICADOS)
"""

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? 
#Use the split methods and set to get the unique words.