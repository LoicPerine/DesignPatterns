from logger import Logger, LogLevel

def main():
    logger = Logger()
    logger.log("This is an info message", LogLevel.INFO)
    logger.log("This is a debug message", LogLevel.DEBUG)
    logger.log("This is a warning message", LogLevel.WARNING)
    logger.log("This is an error message", LogLevel.ERROR)
    other_function()

def other_function():
    logger = Logger()
    logger.log("This is an info from another function", LogLevel.INFO)
    logger.log("This is a debug from another function", LogLevel.DEBUG)
    logger.log("This is a warning from another function", LogLevel.WARNING)
    logger.log("This is an error from another function", LogLevel.ERROR)
main()