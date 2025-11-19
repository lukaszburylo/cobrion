from flask import Flask, jsonify, request

app = Flask(__name__)

class Service:
    def __init__(self, service_name, parameters: dict = None):
        self.service_name = service_name
        self.parameters = parameters

@app.route("/")
def home():
    return jsonify(message="Welcome to the server application!")


@app.route("/get-tasks", methods=["GET"])
def get_tasks():
    params = request.get_json()
    host_id = params.get("host_id")
    api_key = params.get("api_key")

    _r = dict()
    services = [
        Service("disk_usage"),
        Service("ip_address"),
        Service("process", {"process_name": "python.exe"}),
        Service("docker", {"container_name": "sth"}),
        Service("fake")
    ]
    _r['Services'] = [s.__dict__ for s in services]
    _r["HOST_ID"] = host_id
    _r["API_KEY"] = api_key
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
