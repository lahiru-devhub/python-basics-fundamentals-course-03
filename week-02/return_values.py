def add(a, b):
    print(a + b)

add(10, 20)


def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# def function_name(parameter):
#     return value


def is_adult(age):
    return age >= 18

print(is_adult(20))



def login(username, password):
    if username == "admin" and password == "1234":
        return True
    
    return False

status = login("admin", "1234")

print(status)
