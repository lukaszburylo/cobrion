from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Welcome to the server application!")


@app.route("/get-tasks", methods=["GET"])
def get_tasks():
    params = request.get_json()
    host_id = params.get("host_id")
    api_key = params.get("api_key")

    _r = dict()
    _r["Services"] = []

    _s1, _s2, _s3, _s4 = dict(), dict(), dict(), dict()
    _s1["service_name"] = "disk_usage"

    _s2["service_name"] = "ip_address"

    _s3["service_name"] = "process"
    _s3["input_data"] = {"process_name": "python.exe"}

    _s4["service_name"] = "docker"
    _s4["input_data"] = {"container_name": "sth"}

    _r["Services"].append(_s1)
    _r["Services"].append(_s2)
    _r["Services"].append(_s3)
    _r["Services"].append(_s4)
    return jsonify(_r)

@app.route("/results", methods=["POST"])
def results():
    params = request.get_json()
    host_id = params.get("host_id")
    api_key = params.get("api_key")
    data = params.get("data")
    print(data)
    return jsonify({})


if __name__ == "__main__":
    import os

    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
