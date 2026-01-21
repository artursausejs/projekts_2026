from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("pwd")
        print(username)
        print(password)
        return render_template("index.html")
    elif request.method == "GET":
        return render_template("login.html")

if __name__ == "__main__":
    app.run()