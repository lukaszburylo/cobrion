import Services
import requests
import json
from typing import Optional, Dict, List, Any
from pydantic import BaseModel, field_validator, ValidationError

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


if __name__ == "__main__":
    url = "http://127.0.0.1:8080/get-tasks"  # your Flask server address

    payload = {
        "host_id": "foo",
        "api_key": "bar"
    }
    response = requests.get(url, json=payload)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
    _data = Config(**response.json())
    _return = []

    for service in _data.Services:
        service_name = service.service_name
        service_parameters = service.parameters

        svc_cls = Services.SERVICES.get(service_name)
        if svc_cls:
            _return.append(svc_cls.get_data(service_parameters).get_response())
        else:
            print(f"Service '{service_name}' not found")

    url = "http://127.0.0.1:8080/results"  # your Flask server address


    payload = {
        "host_id": "foo",
        "api_key": "bar",
        "data": _return
    }

    response = requests.post(url, json=payload)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
