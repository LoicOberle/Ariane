from .input import Input
import random 
class StaticInput(Input):
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return f"Static input with the {type(self.data).__name__} value {self.data}"
    def trigger(self):
        if(hasattr(self,"output") and self.output is not None):
            self.output.trigger(self.data)
        else:
            print("Can't trigger node: no output connected")

#####################################################################################################################################


class RandomIntInput(Input):
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.data=random.randint(min,max)
    def regenerate(self):
        self.data=random.randint(self.min,self.max)
    def __str__(self):
        return f"Random input with the {type(self.data).__name__} value {self.data}"
    def trigger(self):
        if(hasattr(self,"output") and self.output is not None):
            self.output.trigger(self.data)
        else:
            print("Can't trigger node: no output connected")

    