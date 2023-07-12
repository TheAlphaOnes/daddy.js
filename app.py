from flask import Flask, render_template ,send_file,request,jsonify
from flask_cors import CORS
import plugs

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/cdn/daddy.js')
def daddy_file():
    return send_file("static/modules/daddy.js")

@app.route('/api/daddy.js',methods=["POST"])
def daddy_api():
    if request.method == "POST":
        try:
            resp = request.json
            url = resp.get("url")
            data = resp.get("data")
            reply = plugs.daddy_api(url,data)
            if reply == 300:
                reply = {"status":300}
            else:
                reply = {"status":200,"data":reply}

        except: reply = {"status":300}

        return jsonify(reply)
    else: return "<h1>This is a POST request endpoint </h1>"

@app.route("/api/sumarise")
def sumarise():
    return "ram ram"

@app.route("/testpage1")
def testpage1():
    return render_template("test1.html")

@app.route("/testpage2")
def testpage2():
    return render_template("test2.html")



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
