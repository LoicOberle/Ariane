class Input():
    def attach(self,output):
        if(hasattr(self,"output") and self.output is not None):
            print("can't attach output, an output is already attached. Please detach it before trying to attach another one")
        else:
            self.output=output
    def detach(self):
        if(hasattr(self,"output")):
            self.output=None