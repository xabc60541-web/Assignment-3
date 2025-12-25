from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# 🔹 MongoDB Atlas Connection
client = MongoClient(
    "mongodb+srv://utkarshrane43_db_user:nauuwN4GxINnmuNz@tram.v455und.mongodb.net/?appName=Tram"
)
db = client["assignment_db"]
collection = db["users"]

# 🔹 Home Page (Form)
@app.route("/")
def index():
    return render_template("index.html")

# 🔹 Form Submission
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        # Insert data into MongoDB
        collection.insert_one({
            "name": name,
            "email": email,
            "age": age
        })

        # Redirect on success
        return redirect("/success")

    except Exception as e:
        # Show error on same page
        return render_template("index.html", error=str(e))

# 🔹 Success Page
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
