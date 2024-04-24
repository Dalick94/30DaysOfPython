### HIGHER ORDER FUNCTIONS ###

#Exercises Level 1:

#1.
'''
Mapear sería itinerar sobre cada elemento de una lista.
Filtro itira sobre la lista y devuelve un boleano. 
Reduce itira sobre la lista y opera con el restante. (Devuelve un valor único)
'''

#2.
'''
Una función de orden superior en Python es un ciudadano de primera clase, que nos permite realizar diversas operaciones con las funciones.
Un cierre es como una función anidada.
Un decorador es un patrón de diseño que permite añadir a un objeto nuevas funciones.
'''

#3.
def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

print(list(squared_numbers))

#4.
countries = ['Spain', 'Portugal', 'Italy', 'Greece', 'Morocco']
list(map(lambda country: print(country), countries))

#5.
names = ['Guillermo', 'Edu', 'Diego', 'José']
list(map(lambda name: print(name), names))

#6.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
list(map(lambda number: print(number), numbers))


# Exercises Level 2:
#1.
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, countries)
print(list(names_upper_cased))

#2.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def squared_root(num):
    return num**2

squared_root_list = map(squared_root, numbers)
print(list(squared_root_list))

#3.
names = ['Guillermo', 'Edu', 'Diego', 'José']
def change_to_upper_the_names(x):
    return x.upper()
changed_to_upper_the_names = map(change_to_upper_the_names, names)
print(list(changed_to_upper_the_names))

#4.
countries = ['Spain', 'Portugal', 'Iceland', 'Switzerland', 'Italy', 'Greece', 'Morocco']

def filter_countries(country):
    if 'land' in country:
        return True     
    return False

filtered_countries_by_land = filter(filter_countries, countries)
print(list(filtered_countries_by_land))


#5.
countries = ['Spain', 'Portugal', 'Iceland', 'Switzerland', 'Italy', 'Greece', 'Morocco']
def filter_countries_six(country):
    if len(country) == 6:
        return True     
    return False

filtered_countries_by_land = filter(filter_countries_six, countries)
print(list(filtered_countries_by_land))

#6.
countries = ['Spain', 'Portugal', 'Iceland', 'Switzerland', 'Italy', 'Greece', 'Morocco', 'Estonia']
def filter_countries_six_or_more(country):
    if len(country) >= 6:
        return True     
    return False

filtered_countries_by_land = filter(filter_countries_six_or_more, countries)
print(list(filtered_countries_by_land))

#7.
countries = ['Spain', 'Portugal', 'Iceland', 'Switzerland', 'Italy', 'Greece', 'Morocco', 'Estonia']
def filter_countries_start_by_e(country):
    if country.startswith('E'):
        return True     
    return False

filtered_countries_by_land = filter(filter_countries_start_by_e, countries)
print(list(filtered_countries_by_land))

#8.

from functools import reduce

arr = [1, 2, 3, 4, 5]

def add_one(x):
    return x + 1

def is_odd(x):
    return x % 2 != 0

result = reduce(lambda acc, x: acc + x, filter(is_odd, map(add_one, arr)))

print(result) 

#9.
def get_string_lists(lst):
    string_list = []

    for item in lst:
        if isinstance(item, str):
            string_list.append(item)

    return string_list

#10.
numbers = [1, 2, 3, 4, 5]

sum_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_numbers) 

#11.
countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]

sentence = reduce(lambda acc, country: acc + country + ", ", countries, "")[:-2] + " are north European countries" 
print(sentence)

#12.
categorized_countries = []

for country in countries:
    for pattern in common_patterns:
        if pattern in country.lower():
            categorized_countries.append(country)
            break
            
    return categorized_countries

#13.
def country_starting_letter_count():
    countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi"]

    country_dict = {}
    for country in countries:
        first_letter = country[0].upper()
        if first_letter in country_dict:
            country_dict[first_letter] += 1
        else:
            country_dict[first_letter] = 1

    return country_dict

print(country_starting_letter_count())

#14.

def get_first_ten_countries():
    with open('data/countries.json', 'r') as file:
        countries_data = json.load(file)
    
    first_ten_countries = countries_data[:10]
    
    return first_ten_countries

#15.
def get_last_ten_countries(countries):
    if len(countries) <= 10: 
        return countries 
    else: return countries[-10:]

#16.
