import re
import matplotlib.pyplot as plt
import numpy as np

class LogicModel:
    
    def __init__(self):
        self.str=''
        self.hi=0
        self.lo=0

    def set_hi(self,hi):
        self.hi=hi

    def set_lo(self,lo):
        self.lo=lo

    def set_str(self,str):
        self.str=str.replace('^','**')
       
    def x(self):
       return np.linspace(self.lo,self.hi)
    
    def y(self):
        return eval(self.str,{},{'x':self.x()})
    
    def validate_input(self):
        
        if not re.match(r'^[0-9+\-*/^x()]+$', self.str):
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

       
    def get_str(self):
        return self.str



if __name__=='__main__':
    s=LogicModel()
    s.set_str('x^2')
    s.set_hi(10)
    s.set_lo(-10)
    s.plot_graph()

