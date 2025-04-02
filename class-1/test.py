
#? variable creation
#? JS - var, let, const | Python - int, str, bool, float, list, dict, tuple, set
num = 1
str = "Hello"
bool = True
float = 1.1
list = [1, 2, 3]
dict = {"name": "John", "age": 20}
tuple = (1, 2, 3)
set = {1, 2, 3}

#? <----------------------------------variable usage---------------------------------->
print("\n<--------------------------------------->")
print(num)
print(str)
print(bool)
print(float)
print(list)
print(dict)
print(tuple)
print(set)

#? <----------------------------------List usage---------------------------------->
print("\n<--------------------------------------->")
print(list)
list.append(4)
print(list)
list.pop()
print(list)
list.insert(0, 0)
print(list)
list.remove(0)
print(list)
list.sort()
print(list)
list.reverse()
print(list)

#? <----------------------------------Tuple usage---------------------------------->
print("\n<--------------------------------------->")
print(tuple)
#* tuple is immutable

#? <----------------------------------Set usage---------------------------------->
print("\n<--------------------------------------->")
print(set)
set.add(4)
print(set)
set.remove(4)
print(set)

#? <----------------------------------Dictionary usage---------------------------------->
print("\n<--------------------------------------->")
print(dict)
dict["name"] = "John"
print(dict)

#? <----------------------------------function creation---------------------------------->
print("\n<--------------------------------------->")
def add(a, b):
    return a + b
print(add(1, 2))

#? <----------------------------------class creation---------------------------------->
print("\n<--------------------------------------->")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

#? <----------------------------------class usage---------------------------------->
person = Person("John", 20)
person.say_hello()

#? <----------------------------------if statement---------------------------------->
print("\n<--------------------------------------->")
if num > 0:
    print("num is positive")
else:
    print("num is negative")
    
#? <----------------------------------elif statement---------------------------------->
print("\n<--------------------------------------->")
if num > 0:
    print("num is positive")
elif num < 0:
    print("num is negative")
else:
    print("num is zero")

#? <----------------------------------ternary operator---------------------------------->   
print("\n<--------------------------------------->")
print("num is positive") if num > 0 else print("num is negative")

#? <----------------------------------for loop---------------------------------->   
print("\n<--------------------------------------->")
for i in range(10):
    print(i)
    
#? <----------------------------------while loop---------------------------------->
print("\n<--------------------------------------->")
while num > 0:
    print(num)
    num -= 1