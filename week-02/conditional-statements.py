# if <condition>:
#     statement


age = 10

if age >= 18:
    print("You are an adult");
    print("You can vote");
    
balance = 5000
payment = 3000

if balance >= payment:
    print("Payment Successful") 

marks = 80

if marks >= 75:
    print("Pass with A Grade")
else:
    print("Fail")
    
    
username = "admin"
password = "12345"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid username or password")
    

role = "teacher"

if role == "admin":
    print("Admin Dashboard")
elif role == "teacher":
    print("Teacher Dashboard")
elif role == "student":
    print("Student Dashboard")
else:
    print("Guest Dashboard")
    

# =================

amount = 2500

if amount >= 5000:
    print("20% Discount")
elif amount >= 2000:
    print("10% Discount")
elif amount >= 1000:
    print("5% Discount")
else:
    print("No Discount")