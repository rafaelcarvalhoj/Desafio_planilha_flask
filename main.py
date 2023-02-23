import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request
from flask import jsonify
from flask import Flask

d = [
        {
            "number": "1",
            "name": "Mahesh",
            "age": 25,
            "city": "Bangalore",
            "country": "India"
        },
        {
            "number": "2",
            "name": "Alex",
            "age": 26,
            "city": "London",
            "country": "UK"
        },
        {
            "number": "3",
            "name": "David",
            "age": 27,
            "city": "San Francisco",
            "country": "USA"
        },
        {
            "number": "4",
            "name": "John",
            "age": 28,
            "city": "Toronto",
            "country": "Canada"
        },
        {
            "number": "5",
            "name": "Chris",
            "age": 29,
            "city": "Paris",
            "country": "Franch"
        }
    ]

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/")
def home():
    df = pd.DataFrame(d)
    return df.to_html()

app.run()
