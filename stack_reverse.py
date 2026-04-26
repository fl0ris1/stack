class Stack():
    def __init__(self,n):
        self.stack=[]
        self.maxSize=n
        
    def push(self,value):
        if len(self.stack)<self.maxSize:
            self.stack.append(value)
        else:
            print("STACK FULL")
            
    def pop(self):
        if len(self.stack)>0:
           self.stack.pop()
        else:
            print("NO VALUES AVAILIBLE")
            
    def display(self):
        print(self.stack)
        

inp=input("Input A Word: ")
stack=Stack(len(inp))

for i in range(len(inp)-1,-1,-1):
    stack.push(inp[i])
    
stack.display()