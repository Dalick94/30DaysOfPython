#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
name = "Thirty"
surname = "Days"
age = "Of"
address = "Python"

holamundo = name + surname + age + address
print(holamundo)


#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a = "Coding"
b = "For"
c = "All"

single_string = a + b + c
print(single_string)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4. Print the variable company using print().
print(company)

#5. Pint the length of the company string using len() method and print().
print(len(company))

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9. Cut(slice) out the first word of Coding For All string.
print(company[1:15])

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))

#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

#12. Change Python for Everyone to Python for All using the replace method or other methods.
py= "Python for Everyone"
print(py.replace("Everyone", "All"))

#13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print("Facebook, \t Google, \t Microsoft, \tApple, \tIBM, \t Oracle, \t Amazon")

#15. What is the character at index 0 in the string Coding For All.
#C

#16. What is the last index of the string Coding For All.
#l

#17. What character is at index 10 in "Coding For All" string.
#Space

#18. Create an acronym or an abbreviation for the name 'Python For Everyone
acro = "Python For Everyone"
print(acro[0])
print(acro[7])
print(acro[11])

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
print(company[0], company[7], company [11])

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

#21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
hola = "Coding For All People"
print(hola.rfind("l"))

#23. Use index or find to find the position of the first occurrence of the word 'because' in 
#the following sentence: 'You cannot end a sentence with because because because is a conjunction'
serial = "You cannot end a sentence with because because because is a conjunction"
print(serial.index("because"))

#24. Use rindex to find the position of the last occurrence of the word because in 
#the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(serial.rindex("because"))

#25. Slice out the phrase 'because because because' in
# the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(serial[0:30])
print(serial[54:71])

#26. Find the position of the first occurrence of the word 'because' in
# the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(serial.find("because"))

#27. Slice out the phrase 'because because because' in 
#the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(serial[0:30])
print(serial[54:71])

#28. Does ''Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

#29. Does 'Coding For All' end with a substring coding?
print(company.startswith("coding"))

#30.   Coding For All      '  , remove the left and right trailing spaces in the given string.
re ="    Coding For All      "
print(re[4:20])

#31. Which one of the following variables return True when we use the method isidentifier()
#30DaysOfPython
#thirty_days_of_python (Éste)

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
#Join the list with a hash with space string.
libraries_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries_python)
print(result)

#33. Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print("I am enjoying this challenge. \n I just wonder what is next." )

#34. Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity\nAsabeneh\t25\tFinland\tHelsinki")

#35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

#36. Make the following using string formatting methods:
a = 8
b = 6

print("{}+{}={}".format(a, b, a+b))
print("{}-{}={}".format(a, b, a-b))
print("{}*{}={}".format(a, b, a*b))
print("{}/{}={}".format(a, b, a/b))
print("{}%{}={}".format(a, b, a%b))
print("{}//{}={}".format(a, b, a//b))
print("{}**{}={}".format(a, b, a**b))



