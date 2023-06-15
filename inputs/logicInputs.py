from .input import Input

class TrueInput(Input):
    def __init__(self):
        self.data=True

class FalseInput(Input):
    def __init__(self):
        self.data=False

class ChoiceInput(Input):
    def __init__(self,data):
        self.data=data
    def getState(self):
        return self.data
    def invert(self):
        self.data=not self.data