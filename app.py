from flask import Flask, redirect, request, render_template, make_response, url_for
from datetime import date, datetime
import csv
from datetime import datetime
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

usa = ["aging","arbor","ardor","armor","balks","check","chili","color","disks","draft","edema","fecal","feces","favor","fiber","filet","fetal","fetid","fetus","jails","gaged","gages","grams","grays","groin","honor","humor","labor","liter","meter","miter","molds","moldy","molts","odors","phony","plows","poufs","rigor","rumor","saber","savor","sheik","story","tumor","tires","valor","vapor","vigor","wagon","wooly"]

def getDate():
    return datetime.today().strftime('%d/%m/%Y')

def getWord(date):
    with open('wordlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['date'] == date:
                return row['word']

def americaCheck(word):
    for i in usa:
        if word == i:
            return True
    return False
                    

@app.route('/', methods=['GET'])
@cache.cached(timeout=50)
def index():
    if request.method == 'GET':
        date = getDate()
        word = getWord(date)
        if americaCheck(word):
            return render_template("true.html")
        else:
            return render_template("false.html")
    


if __name__ == "__main__":
    date = getDate()
    word = getWord(date)
    print(americaCheck(word))
    app.run(debug=True)
    

    