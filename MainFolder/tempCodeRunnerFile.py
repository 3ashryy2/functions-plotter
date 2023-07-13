import re
import matplotlib.pyplot as plt
import numpy as np

class LogicModel:
    # def __init__(self,str,hi,lo):
    #     self.str=str.replace('^','**')
    #     self.hi=hi
    #     self.lo=lo
    #     self.compiled_str=compile(self.str,'name','eval')

    
    def __init__(self):
        self.str=''
        self.hi=0
        self.lo=0
        self.compiled_str=None


    def set_hi(self,hii):
        self.hi=hii

    def set_lo(self,loo):
        self.lo=loo

    def set_str(self,strr):
        self.str=strr.replace('^','**')
        self.set_compiledStr

    def set_compiledStr(self):
        self.compiled_str=compile(self.str,'name','eval')

    def x(self):
       return np.linspace(self.lo,self.hi)
    
    def y(self):
        return eval(self.str,{},{'x':self.x()})

    def get_compiled_str(self):
        return self.compiled_str
    
    def validate_input(self):
        
        if not re.match(r'^[0-9+\-*/^x()]+$', self.str):
            raise ValueError("Invalid function string")
            
        if (self.lo>self.hi):
            raise ValueError("min must be less than max")
        
        return True
    
    def plot_graph(self):
        #if self.validate_input()==True:
        plt.plot(self.x(),self.y(),color='red')
        plt.show()

       
    def get_str(self):
        return self.str






if __name__=='__main__':
    s=LogicModel()
    s.set_str('x^2')
    s.set_hi(10)
    s.set_lo(-10)
    s.plot_graph
    plt.show