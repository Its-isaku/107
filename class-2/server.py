
#? Flask API Example
from flask import Flask, render_template, request
import json
from config import db

#? initialize Flask app
app = Flask(__name__)

#! <------------- test flask -------------> 

#? Display a simple welcome message
@app.route("/")
def hello_world():
    return "<p>Hello, World CH56!</p>"

#? Test endpoint to verify API is working
@app.get("/test")
def test():
    return "This is a test endpoint"

#? Serve the home page content
@app.get("/home")
def home():
    return "Welcome to the home page!"

#? Return a list of users in JSON format
@app.get("/users")
def get_users():    
    return {"users": ["Alice", "Bob", "Charlie"]}

#? Return information about the API developer
@app.get("/api/about")
def about():
    print("About endpoint accessed")
    name = {"name": "Isai Almeraz"}
    return name

#? Return a list of student names
@app.get("/api/students")
def students():
    print("Students endpoint accessed")
    student_names = ["Isai", "Jeffrey", "George", "nar", "Erick", "Rafael"]
    return student_names

#? Personalized greeting using URL parameter
@app.get("/greet/<name>")
def greet(name):
    print(f"Greet endpoint accessed from {name}")
    return f"Hello, {name}!"

#? Render a contact page HTML template with dynamic data
@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    user_name = "Isai Almeraz"
    age = 21
    return render_template("contact.html", name=user_name, age=age)


#! <------------- real server -------------> 

#? Initialize a list to store products
products = []

#? Retrieve and return all products from MongoDB collection 
@app.get("/api/products")
def get_products():
    cursor = db.products.find({})
    for product in cursor:
        products.append(fix_id(product))
        
    return json.dumps(products)

def fix_id(obj):
    obj["_id"] = str(obj["_id"]) #? Convert ObjectId to string for JSON serialization
    return obj

#? Receive a new product from client and add it to MongoDB collection
@app.post("/api/products")
def post_product():
    item = request.get_json()
    print(item)
    
    #* insert into MongoDB
    db.products.insert_one(item)
    print(item)
    return json.dumps(fix_id(item))

#? Fetch all products from MongoDB collection by index
@app.put("/api/products/<int:index>")
def put_products(index):
    updated_item = request.get_json()
    print(updated_item)
    
    #* mock update
    if len(products) > index >= 0:
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "index deoes not exist", 404

#? Delete a product from MongoDB collection by index
@app.delete("/api/products/<int:index>")
def delete_products(index):
    deleted_item = request.get_json()
    print(f"delete index: {index}")
    
    #* mock delete
    if len(products) > index >= 0:
        deleted_item = products.pop(index)
        return json.dumps(deleted_item)
    else:
        return "index deoes not exist", 404

#? Update a product in MongoDB collection by index
@app.patch("/api/products/<int:index>")
def patch_products(index):
    patch_item = request.get_json()
    print(patch_item)
    
    #* mock update
    if len(products) > index >= 0:
        products[index].update(patch_item)
        return json.dumps(patch_item)
    else:
        return "index deoes not exist", 404

#? Run the Flask app
app.run(debug=True, port=8000)       