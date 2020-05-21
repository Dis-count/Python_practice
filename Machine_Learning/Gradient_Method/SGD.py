# SGD（Stochastic gradientdescent）随机梯度下降法：每次迭代使用一组样本

#针对BGD算法训练速度过慢的缺点，提出了SGD算法，普通的BGD算法是每次迭代把所有样本都过一遍，每训练一组样本就把梯度更新一次。而SGD算法是从样本中随机抽出一组，训练后按梯度更新一次，然后再抽取一组，再更新一次，在样本量及其大的情况下，可能不用训练完所有的样本就可以获得一个损失值在可接受范围之内的模型了。

#-*- coding: utf-8 -*-  
import random  
#用y = Θ1*x1 + Θ2*x2来拟合下面的输入和输出  
#input1  1   2   5   4  
#input2  4   5   1   2  
#output  19  26  19  20  
input_x = [[1,4], [2,5], [5,1], [4,2]]  #输入  
y = [19,26,19,20]   #输出  
theta = [1,1]       #θ参数初始化  
loss = 10           #loss先定义一个数，为了进入循环迭代  
step_size = 0.01    #步长  
eps =0.0001         #精度要求  
max_iters = 10000   #最大迭代次数  
error =0            #损失值  
iter_count = 0      #当前迭代次数  
   
while(loss > eps and iter_count < max_iters):    #迭代条件  
    loss = 0  
    i = random.randint(0,3)  #每次迭代在input_x中随机选取一组样本进行权重的更新  
    pred_y = theta[0]*input_x[i][0]+theta[1]*input_x[i][1] #预测值  
    theta[0] = theta[0] - step_size * (pred_y - y[i]) * input_x[i][0]  
    theta[1] = theta[1] - step_size * (pred_y - y[i]) * input_x[i][1]  
    for i in range (4):  
        pred_y = theta[0]*input_x[i][0]+theta[1]*input_x[i][1] #预测值  
        error = 0.5*(pred_y - y[i])**2  
        loss = loss + error  
    iter_count += 1  
    print ('iters_count', iter_count)  
print ('theta: ',theta )  
print ('final loss: ', loss)  
print ('iters: ', iter_count) 
