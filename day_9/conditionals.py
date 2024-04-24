### CONDITIONALS ###


    ### EXERCISES LEVEL 1 ###
#1. 
age = int(input("Please, enter your age: "))
years_wait = 0
if age > 18:
    print("You can drive a car")

else:
    years_wait = 18 - age
    print("You must wait", years_wait, "years")




#2. 

my_age = 29
your_age = int(input("Enter your age"))

if (your_age - my_age) > 0:
    difference_age = your_age - my_age
    print("You are", difference_age, "years older than me")


elif my_age == your_age:
    print("Your age is the same")


else:
    difference_age = your_age - my_age
    print("You are", abs(difference_age), "years younger than me")


#3. 
    
a = int(input("Please enter the first number"))
b = int(input("Please enter the second number"))


if a > b:
    print("Number A is greater than B")


elif a < b:
    print("Number B is greater than A")


else:
    print("Both numbers are iquals")



### EXERCISES LEVEL 2 ###

#1.
    """
    80-100, A
    70-89, B
    60-69, C
    50-59, D
    0-49, F
    """


student_mark = 0

if student_mark > 49:
    if (student_mark > 49) and (student_mark < 60):
            print("D")
    if (student_mark > 59) and (student_mark < 70):
            print("C")
    if (student_mark > 69) and (student_mark < 90):
            print("B")
    if (student_mark > 89) and (student_mark < 100):
            print("A")


else:
    print("F")


#2. 
season = input("Enter the season you are")

spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
autumn = ["September", "October", "November"]
winter = ["January", "February", "December"]   

if season:   
    
    if (season in winter) == True:
        print("You are in Winter!")
    if (season in spring) == True:
        print("You are in Spring!")
    if (season in summer) == True:
        print("You are in Summer!")
    if (season in autumn) == True:
        print("You are in Autumn!")

else:
    print("sad")


#3. 

fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Please enter a fruit")


if not (user_fruit in fruits):
     fruits.append(user_fruit)
     print(fruits)


else:
     print("The fruit is already on the list :)")


    

### EXERCISES LEVEL 3 ###
     
person ={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#1
if ("skills" in person):
     print(person["skills"][2])



#2
if ("skills" in person):
    skills = ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    does_exist = 'Python' in skills
    print(does_exist)

#3
skills = person['skills']

if 'JavaScript' in skills and 'React' in skills:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')


#4. 
if person['country'] == "Finland" and person["is_marred"] == True:
     print(person["first_name"], person["last_name"], "lives in", person["country"],".He is marred")
     

     








