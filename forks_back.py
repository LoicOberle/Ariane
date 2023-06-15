class EmptyFork:
    def __init__(self) -> None:
        pass

    def attach1(self,output):
        if(hasattr(self,"output1") and self.output1 is not None):
            print("can't attach output, an output is already attached. Please detach it before trying to attach another one")
        else:
            self.output1=output
    def detach1(self):
        if(hasattr(self,"output1")):
            self.output1=None
    
    def attach2(self,output):
        if(hasattr(self,"output2") and self.output2 is not None):
            print("can't attach output, an output is already attached. Please detach it before trying to attach another one")
        else:
            self.output2=output
    def detach2(self):
        if(hasattr(self,"output2")):
            self.output2=None
    def trigger(self,data):
        if(not hasattr(self,"output1") and not hasattr(self,"output2")):
            print("can't trigger fork node: No output attached")
        else:
            if(hasattr(self,"output1") and self.output1 is not None):
                self.output1.trigger(data)
            if(hasattr(self,"output2") and self.output2 is not None):
                self.output2.trigger(data)