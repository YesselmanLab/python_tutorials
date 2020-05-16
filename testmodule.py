# Example .py file for importing functions/classes in lesson9.py locally. 

def helloworld():
    print("Hello World")


class TestClass:
    def __init__(self,value):
        self.value = value
    
    def show(self):
        print("This is a TestClass in the testmodule.py file")
