from Dependency.interface import ILogger
from enums import LogLevel

class DuplicatableLogger(ILogger):
    
    def log(self, message: str, loglevel: LogLevel) -> None:
        print(f"duplicatable logger - {message}")