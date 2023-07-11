import matplotlib.pyplot as plt
import numpy as np

class LogicModel:
    def __init__(self,str,hi,lo):
        self.str=str.replace('^','**')
        self.hi=hi
        self.lo=lo
        self.compiled_str=compile(self.str,'name','eval')

    
    # def __init__(self):
    #     self.str=''
    #     self.hi=0
    #     self.lo=0
    #     self.compiled_str=None


    def set_hi(self,hi):
        self.hi=hi

    def set_lo(self,lo):
        self.lo=lo

    def set_str(self,str):
        self.str=str.replace('^','**')

    def set_compiledStr(self):
        self.compiled_str=compile(self.str,'name','eval')

    def f(self):
       return np.array(range(self.lo,self.hi+1))

    def get_compiled_str(self):
        return self.compiled_str
    
    def generate_plot(self):
        plt.plot(self.f(),eval(self.compiled_str,{},{'x':self.f()}),color='red')
        plt.show()

    def get_str(self):
        return self.str






if __name__=='__main__':
    com=LogicModel('x^2',10,-10)
    s=LogicModel()
    print(com.get_str())
    com.generate_plot()
    

