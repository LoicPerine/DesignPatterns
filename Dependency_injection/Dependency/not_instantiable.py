from Dependency.interface import ILogger


class IncompleteLogger(ILogger):
    def __init__(self) -> None:
        print("incomplete logger initialized")
