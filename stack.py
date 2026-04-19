class Stack:
    def __init__(self,n):
        self.stack=[]
        self.maxSize=n #maximum number of elements in the stack
        
    def push(self,val):
        if len(self.stack)<self.maxSize:
            self.stack.append(val)
        else:
            print("STACK FULL")
            
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            print("NO VALUES AVAILIBLE")
            
    def top(self):
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1]
        else:
            print("NO VALUES AVAILIBLE")
            
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        return False
    
    def display(self):
        print(self.stack)
        
        
stack=Stack(16)
stack.push(10)
stack.isEmpty()
stack.display()
stack.size()
stack.push(37)
stack.top()