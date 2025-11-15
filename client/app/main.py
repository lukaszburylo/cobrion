from abc import abstractmethod
import socket

#!/usr/bin/env python3

class ResponseTemplate:
    response = dict()
    def create_response(self, service_name: str, data: str):
        self.response["service"] = service_name
        self.response["data"] = data
        json_response = str(self.response).replace("'", '"')
        return json_response      

class Service:
    @abstractmethod
    def get_service_name(self) -> str:
        pass


class IpAddressService(Service):
    @staticmethod
    def get_service_name() -> str:
        return "ip_address"
    
    @staticmethod
    def get_data() -> str:
        return ResponseTemplate().create_response(IpAddressService().get_service_name(), IpAddressService().__get_ip())
    
    @staticmethod
    def __get_ip() -> str:
        try:
        # Use a UDP socket to obtain the outbound IP without sending data.
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                # The address doesn't need to be reachable; no packets are sent.
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
        except Exception:
            try:
                hostname = socket.gethostname()
                for ip in socket.gethostbyname_ex(hostname)[2]:
                    if not ip.startswith("127."):
                        return ip
            except Exception:
                pass
        return "127.0.0.1"



if __name__ == "__main__":
    print(IpAddressService.get_data())

