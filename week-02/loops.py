# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

for number in range(1,6):
    print(number)
    
    
# Type of Loop

# For Loop
# While Loop


# for variable in sequence:
#     statements

for i in range(5):
    print(i)
    
    
fruits = ["Apple", "Orange", "Mango"]

for fruit in fruits:
    print(fruit)
    

word = "Python"

for letter in word:
    print(letter)
    
    
# While Loop

# while condition:
#     statements


count = 1

while count <= 5:
    print(count)
    count += 1
    

# while True:
#     print("Hello")
    

# break Statement
for i in range(10):
    if i == 5:
        break
    
    print(i)
    
# Continue Statement

for i in range(6):
    
    if i == 3:
        continue
    
    print(i)
    
# Pass statement

for i  in range(5):
    if i == 3:
        pass
    
    print(i)