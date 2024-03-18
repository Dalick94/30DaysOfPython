### TUPLES ### Es inmutable

### EXERCICES LEVEL ###
my_tuple = ()
my_brothers_tuple = ("Francisco", "Pablo", "Sergio")
my_sisters_tuple = ("Ana", "Mamen")
my_siblings_tuple = my_brothers_tuple + my_sisters_tuple
print(my_siblings_tuple)
print(len(my_siblings_tuple))

my_family_list = list (my_siblings_tuple)
my_family_list.insert (1, "Paco")
my_family_list.insert (1, "Josefa")
print(my_family_list)
family_members = tuple(my_family_list)
print(type(family_members))


### EXERCISES LEVEL 2 ###
my_siblings_tuple = list(family_members)
del my_siblings_tuple [0:2]
print(my_siblings_tuple)

my_parents_tuple = list(family_members)
del my_parents_tuple [2:7]
print(my_parents_tuple)



fruits_tuple = ("banana", "orange", "pineaple", "mango")
vegeteable_tuple = ("cucumber", "eggplant", "paprika", "pak choi")
dogs_products = ("ball", "bone", "small house", "brush")
food_stuff_tp = fruits_tuple + vegeteable_tuple + dogs_products
print(food_stuff_tp)


food_stuff_lt = list(food_stuff_tp)
del food_stuff_lt [5:6]
del food_stuff_lt [0:3]
del food_stuff_lt [ 9:12]

print(food_stuff_lt)


del food_stuff_tp


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


