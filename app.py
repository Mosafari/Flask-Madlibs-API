# Initiate Flask Project

from flask import Flask, render_template ,request
import json
import csv

app = Flask(__name__)

@app.route("/",methods = ['GET'])
def main():
    # default : Displaying Place Holders
    if request.method == 'GET':
        dict ={
            "person" : r'{{person}}',
            "color" : r'{{color}}',
            "foods" : r'{{foods}}',
            "adjective" : r'{{adjective}}',
            "thing" : r'{{thing}}',
            "place" : r'{{place}}',
            "verb" : r'{{verb}}',
            "adverb" : r'{{adverb}}',
            "food" : r'{{food}}',
            "things": r'{{things}}'
        }
        return render_template("main.html", val = dict)
    
    
@app.route("/api", methods = [ 'POST'])
def apival():
    # recieve json and replace in html
    if request.method == 'POST':
        dict = request.get_json()
        # store each api request in csv file
        print(type(dict))
        # data = json.load(dict)
        headers= ["person" ,"color" ,"foods" ,"adjective" ,"thing" ,"place" ,"verb" ,"adverb" ,"food" ,"things"]
        with open("api-req.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = headers)
            writer.writeheader()
            writer.writerows([dict])
        return render_template("main.html", val = dict)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)