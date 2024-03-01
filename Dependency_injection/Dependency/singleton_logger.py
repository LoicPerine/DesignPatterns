from Dependency.interface import ILogger
from time import time
from typing import Self

from enums import LogLevel

class Logger(ILogger):
    
    log_format = '{asctime}- {level} - {message}'
    instance: Self = None
    
    def __new__(cls) -> Self:
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def log(self, message: str, level: LogLevel) -> None:
        print(self.log_format.format(asctime=time(), level=level, message=message))