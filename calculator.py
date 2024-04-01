class Calculator:
    name = "Genius Calculator"

    def __init__(self, name):
        self.name = name

    def add(self, x, y):
        print(self.name)
        res = x + y
        print(res)

    def minus(self, x, y):
        res = x - y
        print(res)
