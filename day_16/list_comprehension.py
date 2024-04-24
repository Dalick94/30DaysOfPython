### LIST COMPREHENSION ###

#Exercises:

#1.
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero_numbers = [i for i in numbers if i > 0]
print(negative_and_zero_numbers)

#2.
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatted_list = [number for row in list_of_lists for number in row]
more_flatted_list = [number for row in flatted_list for number in row]
print(more_flatted_list)

#3.
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

#4.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [[country.upper() for country in sublist[0]] + [sublist[0][0][:3].upper()] for sublist in countries]
print(output)

#5.
ountries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(output)

#6.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [' '.join(name[0]) for name in names]
print(output)

#7.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda slope, x, y: y - slope * x
