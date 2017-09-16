
import turtle
import math

"""1.4 (Print a table) Write a program that displays the following table:
a a^2 a^3
1 1 1
2 4 8
3 9 27
4 16 64"""
print("a", "a^2", "a^3")
print(1, 1**1, 1**3)
print(2, 2**1, 2**3)
print(3, 3**1, 3**3)
print(4, 4**1, 4**3)

""" 1.9 (Area and perimeter of a rectangle) Write a program that displays the area and
perimeter of a rectangle with the width of 4.5 and height of 7.9 using the following
formula:
area = width * height

"""

#1.9
width = 4.5
height = 7.9
area = width * height
perimeter = 2 * (width + height)

print("Area of the rectangle is ", area)
print("Perimeter of the rectangle is ", perimeter)

"""1.10 (Average speed) Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
Write a program that displays the average speed in miles per hour. (Note that
1 mile is 1.6 kilometers.)"""

distance = 14 / 1.6  # changing killometer to miles
time = (45 + 0.5) / 60  # change the seconds, minutes to hour
speed = distance/time  # in miles/hour
print("The average speed of the runner is ", speed, " miles/hour")


"""
*2.5 (Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total. Here is a sample run:"""

subtotal, gratuity = eval(input("Enter the subtotal and a gratuity rate:"))
gratuity = (subtotal * gratuity)/100
total = subtotal + gratuity
print("The gratuity is ", gratuity, " and the total is ", total)

"""**2.7 (Find the number of years and days) Write a program that prompts the user to
enter the minutes (e.g., 1 billion), and displays the number of years and days for
the minutes. For simplicity, assume a year has 365 days. Here is a sample run:"""
minutes = eval(input("Enter the number of minutes:"))

day = 24 * 60
year = day * 365

if minutes > 1440*365:
	years = minutes // year
	remainder = minutes % year
	if remainder > day:
		days = remainder//day
		minute = remainder%day

print(min, "minutes is approximately", years, "years and ", days, "days")

'''*2.13 (Split digits) Write a program that prompts the user to enter a four-digit integer
and displays the number in reverse order. Here is a sample run:
Enter an integer:
3
1
2
5'''

num = input("Enter an ingeger:")
for i in range(len(num)):
	print(num[len(num)-i-1])
	
	
"""|2.15 (Geometry: area of a hexagon) Write a program that prompts the user to enter the
side of a hexagon and displays its area. The formula for computing the area of a
hexagon is where Area = s is the length of a side. Here is a sample run:"""

s = eval(input("Enter the side:"))

area = (3*(3 ** 0.5) * (s ** 2))/2

print("The area of the hexagon is ", format(area, ".2f"))

# """3.1 (Geometry: area of a pentagon) Write a program that prompts the user to enter the
# length from the center of a pentagon to a vertex and computes the area of the pentagon,
# as shown in the following figure.The formula for computing the area of a pentagon is  area = (3*(3 ** 0.5)*(s*s))/2 where s is
# the length of a side. The side can be computed using the formula
# where r is the length from the center of a pentagon to a vertex. Here is a sample
# run:
# s = 2rpi/5 
# """

r = eval(input("Enter the length from the center to a vertex:"))
s = (2 * r * math.sin(math.pi/5))
area = (3*(3 ** 0.5)*(s*s))/2

print("The area of the pentagon is ",format(area,"0.2f"))

"""*3.2 (Geometry: great circle distance) The great circle distance is the distance between
two points on the surface of a sphere. Let (x1, y1) and (x2, y2) be the geographical
latitude and longitude of two points. The great circle distance between the two
points can be computed using the following formula:
d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
Write a program that prompts the user to enter the latitude and longitude of two
points on the earth in degrees and displays its great circle distance. The average
earth radius is 6,371.01 km. Note that you need to convert the degrees into radians
using the math.radians function since the Python trigonometric functions use
radians. The latitude and longitude degrees in the formula are for north and west.
Use negative to indicate south and east degrees. Here is a sample run: """

radius = 6371.01

x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees:"))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees:"))


d = radius * math.acos(math.sin( math.radians(x1)) * math.sin( math.radians(x2)) + math.cos( math.radians(x1))*math.cos( math.radians(x2))*math.cos( math.radians(y1-y2)))
print("The distance between the two points is",d,"km")

"""*3.3 (Geography: estimate areas) Find the GPS locations for Atlanta, ;
Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
www.gps-data-team.com/map/ and compute the estimated area enclosed by these
four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
distance between two cities. Divide the polygon into two triangles and use the formula
in Programming Exercise 2.14 to compute the area of a triangle.)"""


"""
#Atlanta
33.7489954,-84.3879824
#Georgia
-82.90007509999998 , 32.1656221

#Orlando
28.5383355,-81.37923649999999

#Florida

27.6648274,-81.51575350000002

#Savannah
32.0835407,-81.09983419999998

#Charlotte
-80.84312669999997 , 35.2270869

"""
"""*3.5 (Geometry: area of a regular polygon) A regular polygon is an n-sided polygon in
which all sides are of the same length and all angles have the same degree (i.e., the
polygon is both equilateral and equiangular). The formula for computing the area
of a regular polygon is
Here, s is the length of a side. Write a program that prompts the user to enter the
number of sides and their length of a regular polygon and displays its area. Here is
a sample run:
"""



n = int(input("Enter the nunber of sides:"))
s = float(input("Enter the side length:"))

area = (n * s ** 2)/(4 * math.tan(math.pi/n))

print("The area of the polygon is", area)

"""
3.9 (Financial application: payroll) 
Write a program that reads the following information
and prints a payroll statement:
Employee’s name (e.g., Smith)
Number of hours worked in a week (e.g., 10)
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%)
State tax withholding rate (e.g., 9%)
A sample run is shown below:
"""

name = input("Enter employee's name::")
hours = int(input("Enter number of hours worked in a week:"))
payrate = float(input("Enter hourly pay rate:"))
federaltax = float(input("Enter federal tax withholding rate:"))
statetax = float(input("Enter state tax withholding rate:"))

gross = hours * payrate
federaltax = gross * federaltax/100
statetax = gross * statetax/100
totaldeduction = federaltax + statetax
netpayment = gross - totaldeduction

print("Employee Name:", name)
print("Hours Worked:", hours)
print("Pay Rate:",payrate)
print("Gross Pay:",gross)
print("Deductions:")

print(" Federal Withholding(20.0%):","$" + str(federaltax))
print(" State Withholding(9.0%):","$" + str(statetax))
print(" Total Deduction:", "$" + str(totaldeduction))

print("Net Pay:","$" + str(netpayment))

"""
3.11 (Reverse number) Write a program that prompts the user to enter a four-digit integer
and displays the number in reverse order. Here is a sample run:"""
number = input("Enter an integer:")
digits = []
for n in number:
	digits.append(n)
num = ""
for i in range(len(digits)):
    num += digits[len(digits)-i-1]
print(num)





