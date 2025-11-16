import Services
import requests
import json

if __name__ == "__main__":
    url = "http://127.0.0.1:8080/get-tasks"  # your Flask server address

    payload = {
        "host_id": "foo",
        "api_key": "bar"
    }
    response = requests.get(url, json=payload)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
    myjson = response.json()

    _return = []

    for service in myjson.get("Services", []):
        svc_name = service.get("service_name")
        svc_cls = Services.SERVICES.get(svc_name)
        if svc_cls:
            input_data = service.get("input_data", {})
            #print(str(svc_cls.get_data(input_data)))
            _return.append(svc_cls.get_data(input_data).get_response())
        else:
            print(f"Service '{svc_name}' not found")

    url = "http://127.0.0.1:8080/results"  # your Flask server address


    payload = {
        "host_id": "foo",
        "api_key": "bar",
        "data": _return
    }

    response = requests.post(url, json=payload)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
