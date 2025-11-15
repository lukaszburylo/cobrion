from .BaseService import BaseService
from Helpers.ResponseTemplate import ResponseTemplate
import psutil
import json


class ProcessService(BaseService):
    @staticmethod
    def get_service_name() -> str:
        return "docker"

    @staticmethod
    def get_data(input: str | None) -> str:
        result, data = DockerService.__get_container(input)
        return ResponseTemplate(
            service_name=DockerService.get_service_name(),
            result_status=result,
            input_data=json.loads(input),
            output_data=data,
        )

    @staticmethod
    def __get_container(input) -> str:
        input = json.loads(input)
        container_name = input.get("container_name")
        client = docker.from_env()
        try:
            container = client.containers.get(container_name)
            if container.status == "running":
                print(f"Container '{container_name}' is running.")
                return True, None
            else:
                return False, f"Container '{container_name}' is NOT running. Status: {container.status}"
        except docker.errors.NotFound:
            return False, f"Container '{container_name}' does not exist."
