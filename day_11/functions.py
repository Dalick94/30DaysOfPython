#1.
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(4, 9))

#2.
def area_of_circle(r):
    area = 3.14 * r * r
    return area

#3.
def sum_all_nums(*nums):
    if int(num) == True:
        total = 0
        for num in nums:
            total += num     
        return total
    else:
        print("Datatype is not an integer")

#4.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

#5.
def check_season(month):
    if month == "January" or "February" or "December":
        x = print("Winter")
        return x
    if month == "March" or "April" or "May":
        x = print("Spring")
        return x
    if month == "June" or "July" or "August":
        x = print("Summer")
        return x
    if month == "September" or "October" or "November":
        x = print("Autumn")
        return x
    
#6.
def slope(x1, y1, x2, y2):
  s = (y2-y1)/(x2-x1)
  return s

#7.
def solve_quadratic_eqn():
    import cmath
    a = 1
    b = 5
    c = 6   
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))

#8.
def print_list(i):
    list = []
    for i in range(1):
        list.append(i)
    return list

#9. 
def reverse_list():
    arr = []
    for i in range(1, 6): 
        arr.append(i)
    return arr[::-1]  

#10.
def capitalize_list_items():
    list = []
    for i in range(1):
        list.append(i)
    return list.upper()


#11. 








    
