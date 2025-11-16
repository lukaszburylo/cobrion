import Services
import requests

if __name__ == "__main__":
    _r = dict()
    _r["Services"] = []

    _s1, _s2, _s3 = dict(), dict(), dict()
    _s1["service_name"] = "disk_usage"

    _s2["service_name"] = "ip_address"

    _s3["service_name"] = "process"
    _s3["input_data"] = '{"process_name": "python.exe"}'

    _r["Services"].append(_s1)
    _r["Services"].append(_s2)
    _r["Services"].append(_s3)

    response = []

    url = "http://127.0.0.1:8080/get-tasks"  # your Flask server address

    payload = {
        "host_id": "foo",
        "api_key": "bar"
    }

    response = requests.get(url, json=payload)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
    myjson = response.json()
    for service in myjson.get("Services", []):
        svc_name = service.get("service_name")
        svc_cls = Services.SERVICES.get(svc_name)
        if svc_cls:
            input_data = service.get("input_data", {})
            print(str(svc_cls.get_data(input_data)))
        else:
            print(f"Service '{svc_name}' not found")

    print(response)
