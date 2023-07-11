from flask import Flask, render_template ,send_file,request,jsonify
import plugs

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/cdn/daddy.js')
def daddy_file():
    return send_file("static/daddy.js")

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


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
