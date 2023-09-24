class Person:
    def __init__(self, name):
        self.name = name

    def __call__(self, base):
        print("Call")
        return "PACO"

    def __repr__(self) -> str:
        return "REPR called"

    def __str__(self) -> str:
        return "STR called"
