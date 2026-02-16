class calculator:
    def __init__(self,x1,x2):
        self.x1=x1
        self.x2=x2
    def add(self):
        print(self.x1+self.x2)
    def sub(self):
        print(self.x1-self.x2)
    def mul(self):
        print(self.x1*self.x2)
    def div(self):
        print(self.x1/self.x2)
obj=calculator(1,2)
obj.add()