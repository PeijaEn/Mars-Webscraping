from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# use Flask-PyMongo to set up Mongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# make Flask home page for HTML
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars = mars)

# make Flask route for scraping
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    marsData = scraping.scrapeAll()
    mars.update_one({}, {"$set": marsData}, upsert = True)
    return redirect('/', code = 302)

if __name__ == "__main__":
    app.run()


