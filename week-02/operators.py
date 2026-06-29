# ============================
# Python Operators
# =============================


a = 10
b = 5

print(a+b)

# Arithmetic Operators

# +
# -
# *
# /
# %
# **

number1 = 10
number2 = 20

print(number1+ number2) # 30

print(number2-number1) # 10

print(number1 * number2) #200

print(number2/number1) # 2.0

print(number1 % number2) #10


# Assignment Operators

# = -> Assign value
# += -> Add and Assign
# -= -> Subtract and assign
# *= -> Multiply and assign

x = 10
x += 5

print(x) # 15

y = 20
y -= 8

print(y) # 12


# Comparison Operators

# == Equal
# != Not Equal
# > Greater Than
# < Less Than
# >= Greater or Equal
# <= Less or equal


print(10 == 10)

print(10 != 5)

print(20 > 10)

print(10 < 5)

# Logical Operators

# and
# or
# not

# And

age = 22
country = "Sri Lanka"

if age >= 18 and country == "Sri Lanka":
    print("Eligible")
    

# OR

role = "admin"

if role == "admin" or role == "manager":
    print("Report")
    
# Not

logged_in = False

if not logged_in:
    print("Please login")
    
    
# Membership Operators

# In
# Not in

fruits = ["Apple", "Orange", "Mango"]

print("Mango" in fruits)
print("Banana" not in fruits)

