from flask import Flask, request, render_template, redirect, url_for, flash
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "alsknq3rAg$GernaeasSEF^woei4r098HRFYUKioq73498"

with open("iowa_cities.json") as json_file:
    cities_dict = json.load(json_file)

# print(cities_dict)


###### Custom Error Pages ######
# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


###### Routes ######


# Home page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", pageTitle="Cities in Iowa", cities=cities_dict)


if __name__ == "__main__":
    app.run(debug=False)
