
#? functions  
def hello():
    print("Hello from python")
    
def test_1():
    name = 'Isai'
    last = 'Almeraz'
    
    print(f"Hello {name} {last}")
    
def test_if(age):
    if age < 21:
        print("You are not old enough to drink")
    else:
        print("You are old enough to drink")
        
def test_for():
    nums = [2,4,167,34,73,74,13,67,8]
    sum = 0
    
    for num in nums:
        print(num)
        sum += num
    print(f"Sum of nums is {sum}")
    
def test_dict():
    dog = {
        'name': 'chick',
        'age': 1,
    }
    print(dog)
    print(dog['name'])
    print(dog['age'])
    
#? funtion calls
hello()
test_1()
test_if(18)
test_if(30)
test_for()
test_dict()

#! <---------------Exercise 1---------------> 

"""

    ? Create a for loop an print the title pf each product in the list below.

"""

def test_list():
    products = [
        {"title": "Wireless Mouse", "price": 25.99, "category": "Electronics"},
        {"title": "Yoga Mat", "price": 19.99, "category": "Fitness"},
        {"title": "Coffee Maker", "price": 49.99, "category": "Home Appliances"},
        {"title": "Bluetooth Headphones", "price": 79.99, "category": "Electronics"},
        {"title": "Running Shoes", "price": 59.99, "category": "Footwear"},
        {"title": "Desk Lamp", "price": 22.50, "category": "Office Supplies"}
    ]

    sum = 0
    
    for product in products:
        sum += product['price']
        print(product['title'])
        
    print(f"Sum of products is {sum}")

test_list()