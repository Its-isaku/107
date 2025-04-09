from flask import Flask, render_template, request
import json


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World CH56!</p>"

@app.get("/test")
def test():
    return "This is a test endpoint"

@app.get("/home")
def home():
    return "Welcome to the home page!"

@app.get("/users")
def get_users():    
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.get("/api/about")
def about():
    print("About endpoint accessed")
    name = {"name": "Isai Almeraz"}
    return  name

@app.get("/api/students")
def  students():
    print("Students endpoint accessed")
    student_names = ["Isai", "Jeffrey", "George", "nar", "Erick", "Rafael"]
    return student_names


@app.get("/greet/<name>")
def greet(name):
    print(f"Greet endpoint accessed from {name}")
    return f"Hello, {name}!"

@app.get("/contact")
def contact_api():
    print("Contact API endpoint accessed")
    user_name = "Isai Almeraz"
    age = 21
    return  render_template("contact.html", name=user_name , age=age)

products = []
@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def post_product():
    item = request.get_json()
    print(item)
    
    #* mock save
    products.append(item)
    return json.dumps(products)

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

#? @app.post
#? @app.put
#? @app.delete
#? @app.patch

app.run(debug=True, port=8000)       