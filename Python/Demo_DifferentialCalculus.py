import random
import copy
import numpy as np
import math

def func_examples(x):   #测试函数
    a1 = x[0]
    a2 = x[1]
    return a1**2 + 10

class Differential_calculus:
    def __init__(self,N,d,F,left,right,CR,maxCycle,func):
        self.N = N #群体数量
        self.d = d  #个体维度
        self.F = F
        self.left = left
        self.right = right
        self.CR = CR
        self.maxCycle = maxCycle
        self.func = func

    def init_pop(self):
        self.pop=np.random.uniform(2,size=(self.N,self.d))

    # 目标函数，也是适应度函数（求最小化问题）
    def function(self,x):   #func是传入的函数，x是func所需的参数
        return self.func(x)

    def update(self):
        group2 = self.pop.tolist()
        U_temp = [0 for k in range(d)]
        U = [copy.deepcopy(U_temp) for k in range(N)]
        for _ in range(self.maxCycle):
            for i in range(N):
                r1,r2,r3 = random.sample(range(N),3)
                Jrand = random.randint(0,d)
                for j in range(d):
                    rand = random.uniform(0, 1)
                    if rand < CR or j == Jrand:
                        U[i][j] = group2[r1][j] + F * (group2[r2][j]-group2[r3][j])
                    else:
                        U[i][j] = group2[i][j]
            for i in range(N):
                if self.function(np.array(U[i])) < self.function(np.array(group2[i])):
                    group2[i] = copy.deepcopy(U[i])
            print(group2[0])
            print(self.function(group2[0]))

def func_examples(x):   #测试函数
    a1 = x[0]
    a2 = x[1]
    return a1**2 + 10 


if __name__ == "__main__":

    N = 100 #群体数量
    d = 2 #个体维度
    F=1
    left=-100
    right=100
    CR = 0.1
    maxCycle = 1000 #迭代次数
    
    project = Differential_calculus(N,d,F,left,right,CR,maxCycle,func_examples)
    project.init_pop()
    project.update()
