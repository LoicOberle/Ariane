class AddMerge:
    def __init__(self) -> None:
        self.callCounter=0
        self.buffer=""
        pass

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
            
            if(self.callCounter==0):
                self.callCounter+=1
                self.buffer=data
            else:
                self.output.trigger(self.buffer+data)
                self.callCounter=0

        else:
            print("Can't trigger node: no output connected")