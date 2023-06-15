from .merge import Merge

class AddMerge(Merge):
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