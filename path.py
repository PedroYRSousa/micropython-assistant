FILE = 0x0
DIR = 0x1

class Path():
    def __init__(self, type, path) -> None:
        self.type = type
        self.path = path