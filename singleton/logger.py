from enum import StrEnum
from typing import Self
from time import time

class LogLevel(StrEnum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"

class Logger:
    
    log_format = '{asctime}- {level} - {message}'
    instance: Self = None
    
    def __new__(cls) -> Self:
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            print("logger already initialized, let's not duplicate it")
        return cls.instance
    
    def __init__(self) -> None:
        print("logger initialized")
    
    def log(self, message: str, level: LogLevel) -> None:
        print(self.log_format.format(asctime=time(), level=level, message=message))
