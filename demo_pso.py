import numpy as np
import random

class PSO_model:
    def __init__(self,w,c1,c2,r1,r2,N,D,M,func):
        self.w = w # 惯性权值
        self.c1=c1
        self.c2=c2
        self.r1=r1
        self.r2=r2
        self.N=N # 初始化种群数量个数
        self.D=D # 搜索空间维度
        self.M=M # 迭代的最大次数
        self.x=np.zeros((self.N,self.D))  #粒子的初始位置
        self.v=np.zeros((self.N,self.D))  #粒子的初始速度
        self.pbest=np.zeros((self.N,self.D))  #个体最优值初始化
        self.gbest=np.zeros((1,self.D))  #种群最优值
        self.p_fit=np.zeros(self.N)
        self.fit=1e8 #初始化全局最优适应度
        self.func = func   #优化函数

# 目标函数，也是适应度函数（求最小化问题）
    def function(self,x):   #func是传入的函数，x是func所需的参数
        return self.func(x)

     # 初始化种群
    def init_pop(self):
        for i in range(self.N):
            for j in range(self.D):
                self.x[i][j] = random.random()
                self.v[i][j] = random.random()
            self.pbest[i] = self.x[i] # 初始化个体的最优值
            aim=self.function(self.x[i]) # 计算个体的适应度值
            self.p_fit[i]=aim # 初始化个体的最优位置
            if aim < self.fit:  # 对个体适应度进行比较，计算出最优的种群适应度
                self.fit = aim
                self.gbest = self.x[i]

    # 更新粒子的位置与速度
    def update(self):
        for t in range(self.M): # 在迭代次数M内进行循环
            for i in range(self.N): # 对所有种群进行一次循环
                aim=self.function(self.x[i]) # 计算一次目标函数的适应度
                if aim<self.p_fit[i]: # 比较适应度大小，将小的负值给个体最优
                    self.p_fit[i]=aim
                    self.pbest[i]=self.x[i]
                    if self.p_fit[i]<self.fit: # 如果是个体最优再将和全体最优进行对比
                        self.gbest=self.x[i]
                        self.fit = self.p_fit[i]
            for i in range(self.N): # 更新粒子的速度和位置
                self.v[i]=self.w*self.v[i]+self.c1*self.r1*(self.pbest[i]-self.x[i])+ self.c2*self.r2*(self.gbest-self.x[i])
                self.x[i]=self.x[i]+self.v[i]
        print("最优值：",self.fit,"位置为：",self.gbest)


def func_examples(x):   #测试函数
    a1 = x[0]
    a2 = x[1]
    return a1**2 + 10

#  演示
if __name__ == '__main__':
    # w,c1,c2,r1,r2,N,D,M参数初始化
    w=random.random()
    c1=c2=2#一般设置为2
    r1=0.7 
    r2=0.5
    N=30
    D=2
    M=200

    pso_object=PSO_model(w,c1,c2,r1,r2,N,D,M,func_examples)#设置初始权值
    pso_object.init_pop()
    pso_object.update()
