class One2One:
    def __init__(self,data) -> None:
        self.data=data

    def attach(self,output):
        if(hasattr(self,"output") and self.output is not None):
            print("can't attach output, an output is already attached. Please detach it before trying to attach another one")
        else:
            self.output=output
    def detach(self):
        if(hasattr(self,"output")):
            self.output=None
    def trigger(self,data):
        if(hasattr(self,"output") and self.output is not None):
            self.output.trigger(data+self.data)
        else:
            print("Can't trigger node: no output connected")