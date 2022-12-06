# Initiate Flask Project

from flask import Flask, render_template ,request

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
    if request.method == 'POST':
        dict = request.get_json()
        return render_template("main.html", val = dict)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)