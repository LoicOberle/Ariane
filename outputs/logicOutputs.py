from .output import Output

class PrintOutput(Output):
    def trigger(self,data):
        print(data)