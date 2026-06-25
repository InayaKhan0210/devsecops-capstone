from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["notes_db"]
notes_collection = db["notes"]

@app.route("/")
def index():
    notes = list(notes_collection.find())
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    note = request.form.get("note")
    if note:
        notes_collection.insert_one({"note": note})
    return redirect("/")

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)