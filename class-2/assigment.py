from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.get("/")
def welcome_page():
    print("Welcome endpoint accessed")
    return render_template("welcome.html")

@app.get("/about")
def about_page():
    print("about endpoint accessed")
    return render_template("about.html")

#? Product data storage
products = []

#? The requested endpoints
@app.get("/api/products")
def get_product_list():
    return json.dumps(products)

@app.get("/api/product/count")
def get_product_count():
    return {"count": len(products)}

#? Required product management endpoints
@app.post("/api/products")
def post_product():
    item = request.get_json()
    print(item)
    products.append(item)
    return json.dumps(products)

@app.put("/api/products/<int:index>")
def put_products(index):
    updated_item = request.get_json()
    print(updated_item)
    
    if len(products) > index >= 0:
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "index does not exist", 404
    
@app.delete("/api/products/<int:index>")
def delete_products(index):
    print(f"delete index: {index}")
    
    if len(products) > index >= 0:
        deleted_item = products.pop(index)
        return json.dumps(deleted_item)
    else:
        return "index does not exist", 404

app.run(debug=True, port=8000)