from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def Ilan_GateWay():
    data = request.get_json()
    param = data["param"]
    return jsonify({"result" : "Success", "param" : param})

if __name__ == "__main__":
    app.run()