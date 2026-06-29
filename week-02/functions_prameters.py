print("Welcome Kamal")
print("Welcome Nimal")
print("Welcome Sunil")

def welcome(name):
    print("Welcome:", name)
    
welcome("Dilan")
welcome("Prabath")
welcome("Nimal")

# def function_name():
#     statements
    
    
def show_message():
    print("Welcome to Python master course")
    
show_message()


def display_course_info():
    print("Course: Python master course")
    print("week: 02")
    print("Topic: Functions")
    
display_course_info()


# abc()
# test1()
# myfunction()

def calculate_total():
    pass

def login_user():
    pass

def send_email():
    pass

def validate_password():
    pass

def create_student():
    pass


# Parameters

# def function_name(parameter):
#     statements

def student(name, age):
    print("Student Name: ", name)
    print("Student Age: ", age)
    

student("Dilan", 22)


# Cal Price

def calculate_total(price, quantity):
    total = price * quantity
    print("Total price:", total)
    
calculate_total(500,5)


# Send Email
def send_email(email):
    print("Sending email to:", email)
    
send_email("student@gamil.com")

# Default Parameters

def create_user(username, role="student"):
    print("Username: ", username)
    print("Role : ", role)
    
create_user("John")
create_user("admin_user", "admin")


def student(name, age):
    print(name)
    print(age)
    

student(age=22, name="Dilan")


# Scope of Variables

def create_admin():
    name = "Dilan"
    
    print(name)
    
    
country = "Sri Lanka"

def show():
    print(country)
    
show()


def welcome():
    print("welcome")
    
def login():
    welcome()
    
    print("login success")
    
login()