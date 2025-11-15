import json

class ResponseTemplate:
    response: dict

    @classmethod
    def __init__(cls, service_name: str, data: str):
        cls.response = {
            "service": service_name,
            "data": data
        }

    
    @classmethod
    def __str__(cls) -> str:
        return json.dumps(cls.response)
        