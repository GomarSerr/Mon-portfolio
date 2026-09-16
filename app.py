from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html", name="Margaux", age=33)

@app.route("/projets")
def projets():
    return render_template("projets.html")


@app.route("/apropos")
def apropos():
    return render_template("apropos.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True)
