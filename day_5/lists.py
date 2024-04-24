### LISTS ###

### EXERCISES LEVEL 1 ###
#1. Declare an empty list
my_list = []

#2. Declare a list with more than 5 items
my_list = ["Athletic", "Barca", "Madrid", "Atletico", "Sevilla", "Girona"]

#3. Find the length of your list
print(len(my_list))

#4. Get the first item, the middle item and the last item of the list
a, b, c, d, e, f = my_list
print(a, c, e)

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Guillermo", 29, 1.81, "Single", "Cartagena Street"]

#6. Declare a list variable named it_companies and assign initial values Facebook, Google,
# Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
a, b, c, d, e, f, g = it_companies
print(a, d, g)

#10. Print the list after modifying one of the companies
it_companies [0] = "Telecon"
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append("Galaxy")
print(it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies.insert(5, "Nvidia")
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies [0] = "TELECON"
print(it_companies)

#14. Join the it_companies with a string '#;  '
print(it_companies)

#15. Check if a certain company exists in the it_companies list.
does_exist = 'Google' in it_companies
print(does_exist)

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#18. Slice out the first 3 companies from the list
print(it_companies[0:6])

#19. Slice out the last 3 companies from the list
print(it_companies[3:9])

#20. Slice out the middle IT company or companies from the list
it_companies.remove("IBM")
print(it_companies)

#21. Remove the first IT company from the list
it_companies.remove("TELECON")
print(it_companies)

#22. Remove the middle IT company or companies from the list
it_companies.remove("Google")
print(it_companies)

#23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
del it_companies

#26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

#27. After joining the lists in question 26. Copy the joined list and
# assign it to a variable full_stack. Then insert Python and SQL after Redux.
my_copy = full_stack.copy()
my_copy.insert(5, "Python")
my_copy.insert(6, "SQL")
print(my_copy)


### EXERCISES LEVEL 2 ###
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
a, b, c, d, e, f, g, h, i, j = ages
print(ages)
print("The min age is :", a)
print("The max age is :", j)

#Find the median age (one middle item or two middle items divided by two)
median_age = (d + e) / 2
print(median_age)

#Find the average age (sum of all items divided by their number )
average_age = (a+b+c+d+e+f+g+h+i+j) / 10
print(average_age)

#Find the range of the ages (max minus min)
range_age = j - a
print(range_age)

#Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
average_age = sum(ages) / len(ages)
min_age = min(ages)
max_age = max(ages)

min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print(min_avg_diff)
print(max_avg_diff)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Eirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print(len(countries))
print(countries[95:96])

first_list = countries.copy()
del first_list [96:193]
print(first_list)

second_list =countries.copy()
del second_list [0:96]
print(second_list)

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
#Unpack the first three countries and the rest as scandic countries.

final_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

firsts_powers_worldwide = final_countries.copy()
del firsts_powers_worldwide [3::]
print(firsts_powers_worldwide)

scandic_countries = final_countries.copy()
del scandic_countries [0:3]
print(scandic_countries)














