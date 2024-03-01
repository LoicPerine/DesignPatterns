from Dependency.interface import ILogger
from Dependency.singleton_logger import Logger
from Dependency.duplicatable_logger import DuplicatableLogger
from Dependency.not_instantiable import IncompleteLogger
from enums import LogLevel

def injectable_function(logger: ILogger) -> None:
    logger.log("This is a message", "INFO")

def main() -> None:
    logger = Logger()
    injectable_function(logger)
    logger = DuplicatableLogger()
    injectable_function(logger)

main()