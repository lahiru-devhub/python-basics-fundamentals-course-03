# Integer 

age = 25
year = 2026
student_marks = 75

print(type(age))
print(type(year))

print(age)


# Float 

height = 5.8
weight = 65.5
price = 99.99

print(type(price))
print(height)

# String

name = "Kasun"
name1 = 'Kasun'

city = "Galle"
country = "Sri Lanka"
email = "kasun@gmail.com"

print(type(country))
print(email)


message = "Welcome to python class"

first_name = "Kasun"
last_name = "Perera"

#full_name = first_name + last_name
full_name = first_name + " " + last_name

print(full_name)

# String length

user_name = "Dilan"
print(len(user_name))


# Access first character
#  D  i  l  a  n
#  0  1  2  3  4

print(user_name[4])


#  D  i  l  a  n
# -5 -4 -3 -2 -1 

print(user_name[-4])


# String Methods


# upper()

class_name = "Epic Learn Python"
print(class_name.upper()) # EPIC LEARN PYTHON

# lower

product_name = "Test Product 01"
print(product_name.lower()) # test product 01

# title 

city = "kandy city"
print(city.title()) # Kandy City

# Replace

course_name = "DevOps Master Course"
print(course_name.replace("DevOps", "Python"))

# Strip

student_email = " test@gmail.com "
print(student_email)
print(student_email.strip()) # test@gmail.com


# Type conversion

# Integer to String

student_age = 25

print(str(student_age))
print(type(str(student_age)))

# String to Integer
student_age1 = "25"
print(int(student_age1))
print(type(int(student_age1)))


# F string

name = "Kasun"
age = 20

print("My name is " + name  + " and I'm " + str(age) + " years old")

print(f"My name is {name}  and I'm {age} years old.")



