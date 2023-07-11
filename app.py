from flask import Flask, render_template ,send_file,request,jsonify
import plugs
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/daddy.js', subdomain ='cdn')
def daddy_file():
    return send_file("static/daddy.js")

@app.route('/daddy.js', subdomain ='api',methods=["POST"])
def daddy_api():
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


app.config['SERVER_NAME'] = 'localhost:5000'
app.run(debug=True)