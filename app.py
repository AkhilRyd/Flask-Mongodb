
from flask import Flask, render_template,redirect, url_for,render_template_string,request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')  # Adjust if using a different host or port
db = client['Student']  # Use the 'Student' database
collection = db['Address'] 

@app.route("/")
def home():
    data = collection.find()
    data_list=list(data)
    return render_template("index.html",abc=data_list)

@app.route("/edit/<id>", methods=["GET"])
def edit(id):
    document = collection.find_one({"_id": ObjectId(id)})
    return render_template("editpage.html",abc=document)

@app.route("/update", methods=["POST"])
def update():
    name = request.form.get("name")  # Get value of 'name' field
    id=request.form.get("id")
    age= request.form.get("Age")    # Get value of 'age' field
    document = collection.find_one({"_id": ObjectId(id)})
    collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"Name": name, "Age": age}}
        )
    return redirect(url_for("home"))

@app.route("/delete<id>", methods=["GET"])
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})  # Delete the document by ID
    return redirect(url_for("home"))

   


if __name__ == "__main__":
    app.run(debug=True)
    