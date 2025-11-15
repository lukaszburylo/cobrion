from abc import abstractmethod
import Services


if __name__ == "__main__":
    _r = dict()
    _r['Services'] = []
    

    service = dict()
    service['Name'] = 'ip_address'
    service['Error_if'] = 'ip_address.value == None'

    _r['Services'].append(service)
    
    # przykładowe użycie rejestru: znajdź po nazwie i wywołaj get_data()
    svc_name = "memory_usage"
    svc_cls = Services.SERVICES.get(svc_name)
    if svc_cls:
        print(svc_cls.get_data())
    else:
        print(f"Service '{svc_name}' not found")

