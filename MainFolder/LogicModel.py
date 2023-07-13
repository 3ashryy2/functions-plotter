import re
import matplotlib.pyplot as plt
import numpy as np

class Logic:
    
    def __init__(self):
        self.func='x*0'
        self.hi=0
        self.lo=0

    def set_hi(self,hi):
        self.hi=hi

    def set_lo(self,lo):
        self.lo=lo

    def set_func(self,func):
        self.func=func.replace('^','**')
       
    def x(self):
       return np.linspace(self.lo,self.hi)
    
    def y(self):
        return eval(self.func,{},{'x':self.x()})
    
    def validate_input(self):
        
        if not re.match(r'^[0-9+\-*/^x()]+$', self.func):
            raise ValueError("Invalid function input")
            
        if (self.lo>self.hi):
            raise ValueError("Min must be less than Max")
        
        return True
    
    def plot_graph(self):
        if self.validate_input()==True:
           X=self.x()
           Y=self.y()
           plt.plot(X,Y,color='red')
           plt.grid()
           plt.show()
 
    def get_func(self):
        return self.func



