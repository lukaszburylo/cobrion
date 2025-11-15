import Services


if __name__ == "__main__":
    _r = dict()
    _r["Services"] = []

    service = dict()
    service["Name"] = "ip_address"

    _r["Services"].append(service)

    # przykładowe użycie rejestru: znajdź po nazwie i wywołaj get_data()
    svc_name = "process"
    svc_cls = Services.SERVICES.get(svc_name)
    if svc_cls:
        print(svc_cls.get_data('{"process_name": "python.exe"}'))
    else:
        print(f"Service '{svc_name}' not found")
