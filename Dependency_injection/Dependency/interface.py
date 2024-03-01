from abc import ABC, abstractmethod
from enums import LogLevel

class ILogger(ABC):
    @abstractmethod
    def log(self, message: str,loglevel: LogLevel) -> None:
        pass