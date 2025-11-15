from typing import Optional
import json

class ResponseTemplate:
    response: dict

    @classmethod
    def __init__(cls, service_name: str, result_status: bool, input_data: Optional[str] = None, output_data: Optional[str] = None):
        cls.response = {
            "service": service_name,
            "result_status": result_status,
            "input_data": input_data,
            "output_data": output_data
        }

    
    @classmethod
    def __str__(cls) -> str:
        return json.dumps(cls.response)
        