from .one2one import One2One
class StaticAddOne2One(One2One):
    def __init__(self,data) -> None:
        self.data=data

    def trigger(self,data):
        if(hasattr(self,"output") and self.output is not None):
            self.output.trigger(data+self.data)
        else:
            print("Can't trigger node: no output connected")