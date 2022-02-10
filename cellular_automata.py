

class CA:
    """ 1D cellular automaton """
    
    def __init__(self,size,length=10):
        self.size = size
        self.length = length
        self.grid = [[0 for i in range(size)] for j in range(length)]
        self.rule = {'[0, 0, 0]':0,
                     '[0, 0, 1]':1,
                     '[0, 1, 0]':1,
                     '[0, 1, 1]':1,
                     '[1, 0, 0]':1,
                     '[1, 0, 1]':1,
                     '[1, 1, 0]':1,
                     '[1, 1, 1]':0}
    
    def updateRule(self,newRule):
        for k,i in zip(self.rule.keys(),range(self.size)):
            self.rule[k] = newRule[i]
    
    def initialCond(self,init=None):
        if init==None:
            self.grid[0][int(self.size/4)] = 1
            self.grid[0][int(3*self.size/4)] = 1
        else:
            self.grid[0] = init
    
    def applyRule(self):
        for row in range(1,self.length):
            for col in range(self.size):
                if col == 0:
                    self.grid[row][col] = self.rule[str([0] + self.grid[row-1][col:col+2])]
                elif col == self.size-1:
                    self.grid[row][col] = self.rule[str(self.grid[row-1][col-1:col+2] +[0])]
                else:
                    self.grid[row][col] = self.rule[str(self.grid[row-1][col-1:col+2])]
    
    def printCA(self):
        for row in range(self.length):
            print(self.grid[row])
    
    def getGridForHeat(self):
        self.gridHeat = self.grid
        for row in range(self.length):
            factor = 1 - (row * 0.5 / self.length)
            self.gridHeat[row] = [factor * i for i in self.gridHeat[row]]

