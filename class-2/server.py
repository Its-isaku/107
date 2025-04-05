from flask import Flask, render_template

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

#? @app.post
#? @app.put
#? @app.delete
#? @app.patch

app.run(debug=True, port=8000)       