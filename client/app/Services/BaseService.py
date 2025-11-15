from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def get_service_name(self) -> str:
        pass