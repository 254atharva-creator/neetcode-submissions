class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstk=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstk)==0:
            self.minstk.append(val)
        elif val<=self.minstk[-1]:
            self.minstk.append(val)

    def pop(self) -> None:
        if self.stack[-1]==self.minstk[-1]:
            self.minstk.pop()
        self.stack.pop()
        


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstk[-1]

        
