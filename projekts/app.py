from flask import Flask, request, render_template 
import hashlib

app = Flask(__name__)

USERNAME = "arturix@arturix.lv"
HASH = "9e03f8af086ffe78a5fcd5e4027af673" #Parole: Tests123!

@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("pwd")
        print(username)
        print(password)

        hashed = hashlib.md5(password.encode("utf-8")).hexdigest()
        print(hashed)

        if username == USERNAME and hashed == HASH:
            return render_template("dashboard.html", username=username)
        else:
            error = "Nepareizs lietotājvārds vai parole"

    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run()