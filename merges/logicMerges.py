from .merge import Merge

class OrMerge(Merge):
    def trigger(self,data):
        if(hasattr(self,"output") and self.output is not None):
            
            if(self.callCounter==0):
                self.callCounter+=1
                self.buffer=data
            else:
                self.output.trigger(self.buffer or data)
                self.callCounter=0

        else:
            print("Can't trigger node: no output connected")

class AndMerge(Merge):
    def trigger(self,data):
        if(hasattr(self,"output") and self.output is not None):
            
            if(self.callCounter==0):
                self.callCounter+=1
                self.buffer=data
            else:
                self.output.trigger(self.buffer and data)
                self.callCounter=0

        else:
            print("Can't trigger node: no output connected")