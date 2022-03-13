from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route("/")
def main():
    return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/process", methods = ["POST"])
def process():
    session["username"] = request.form["username"]
    session["location"] = request.form["location"]
    session["fav_lang"] = request.form["fav_lang"]
    session["comments"] = request.form["comments"]
    session["hidden_input"] = request.form["hidden_input"]
   
    print(session)
    return render_template("show.html")


@app.route("/clear_session")
def clear_session():
    session.clear()
    return redirect("/dashboard")



if __name__ == "__main__":
    app.run(debug=True)