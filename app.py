from flask import Flask, redirect, request, render_template, make_response, url_for, jsonify
from datetime import date, datetime
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return 6
    


if __name__ == "__main__":
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    print(page.text)


app.run(debug=True)