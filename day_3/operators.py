#OPERATORS
#EXERCISES
#1. Declare your age as integer variable
age = 29

#2. Declare your height as a float variable
height = 1.81

#3. Declare a variable that store a complex number
cielo = 1j

#4. Calculating the area of a triangle
base = (input("Enter the base of the triangle"))
height = (input("Enter the height of the triangle"))

area = float(base) * float(height) * 0.5
print("The area of this triangle is :", area)

#5. Calculating the perimeter of a tringle
side_a = input("Enter the side a of the triangle")
side_b = input("Enter the side b of the triangle")
side_c = input("Enter the side c of the triangle")

perimeter = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle is: ", perimeter)

#6. RECTANGLE: area (area = length x width) and perimeter (perimeter = 2 x (length + width)
lenght = input("Enter the lenght of the rectangle")
width = input("Enter the width of the rectangle")

area = int(lenght) * int(width)
perimeter = 2 * (int(lenght) + int(width))


print("The area of the rectangle is: ", area, "" "and the perimeter is: ", perimeter)

#7. Circle area
radius = input("Enter the radius of the circle")
area = 2 * 3.14 * int(radius)
print("The area of the circle is: ", area)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2


#9.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
#9.1 Slope
slope = (10-2) / (6-2)
print(slope)
#9.2 Euclidean distance
from math import dist
punto_1 = (2, 2)
punto_2 = (6, 10)
distancia = dist(punto_1, punto_2)
print(distancia)

#10.Compare the slopes in tasks 8 and 9.
#They are iqual


#11. 
x = -3

y = x**2 + 6*x + 9
print(y)

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python"))
print(len("dragon"))
print(len("python") != len("dragon"))

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
print("jargon" in "I hope this course is not full of jargon")

#15. There is no 'on' in both dragon and python
#False

#16. Find the length of the text python and convert the value to float and convert it to string
print(float(len("python")))
print(str(len("python")))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# x % 2 = 0

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# print(7//3). Yes

#19. check if type of '10' is equal to type of 10: No
print(type(10))
print(type("10"))

#20. Check if int('9.8') is equal to 10: No, is 9.
print(int(9.8))

#21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input ("Enter your hours")
rate = input ("Enter the rate per hour")
pay = int(hours) * int(rate)
print("The weekly pay is : ", pay)

#22. Write a script that prompts the user to enter number of years. 
#Calculate the number of seconds a person can live. Assume a person can live hundred years

years_lived = input("Enter numbers of years you have lived")

hope_live = (100 - int(years_lived))

print("You will live :", hope_live * 31,536,000, "seconds more")

#23. Write a Python script that displays the following table
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 44)
print(4, 1, 5, 25, 125)





