import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

path = 'C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\';
smile_filename = ['CSH_test1_smile_data.txt','CSH_test2_smile_data.txt',\
                 'CXY_test1_smile_data.txt','CXY_test2_smile_data.txt',\
                 'LBJ_test1_smile_data.txt','LBJ_test2_smile_data.txt',\
                 'ZFF_test1_smile_data.txt','ZFF_test2_smile_data.txt',\
                 'CBS_test1_smile_data.txt','CBS_test2_smile_data.txt',\
                 'BL_test1_smile_data.txt','BL_test2_smile_data.txt',\
                 'LWM_test_smile_data.txt','ZJH_test_smile_data.txt'
                 ]



#读取smile数据
#数据格式(time,array([]))

def read_smile_data(path, smile_filename):
    
    f =open(path+smile_filename);
    data = f.read()
    data0 = data.split('))\n')
    flag = np.zeros(len(data0))

    for i in range(0,len(data0)):
        data0[i] = data0[i].replace('(','')
        data0[i] = data0[i].replace(']], dtype=int32','')
        data0[i] = data0[i].replace(' array[[','')
        
        data0[i] = data0[i].replace('],\n       [',',')
        data0[i] = data0[i].split(',')
        flag[i] = len(data0[i])

    data1 = np.zeros([len(data0),int(max(flag))]);
    for i in range(0,len(data0)):
        if int(flag[i])!= 1:
            for j in range(0,int(flag[i])):
                if data0[i][j] == ' ':
                    data1[i,j] = float(0);
                else:
                    data1[i,j] = float(data0[i][j]);
    print(len(data1))
    np.savetxt('C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\'+\
               're_'+smile_filename,data1)



#判断是否有笑脸
def If_smile(smile_filename):
    smile = np.loadtxt('C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\re_'+smile_filename)
    smile_data = np.ones([len(smile),2])
    for k in range(0,len(smile)):
        smile_data[k,0] = int(smile[k,0])
    
    for i in range(0,len(smile)):
        if smile[i,1] == 0:
            smile_data[i,1] = 0;
    print(smile_filename)
    print(sum(smile_data[:,1]))        
    return smile_data

#时间去重
def time_Correction(smile_data):

    time_min = int(smile_data[0,0])
    smile_data = np.delete(smile_data,len(smile_data)-1,0)
    time_max = int(smile_data[len(smile_data)-1,0])
    
    smile_data_Correct = np.zeros([time_max - time_min+1,2])
    smile_data_Correct[:,0] = range(time_min,time_max+1)
    
    time_exist = list(set(smile_data[:,0]))
    
    for i in range(0,len(smile_data_Correct)):
        if (time_min+i) in time_exist:
            if sum(smile_data[np.where(smile_data[:,0]== i+time_min)][:,1]) > 0:
                smile_data_Correct[i,1] = 1; 
    print(sum(smile_data_Correct[:,1]))
    return smile_data_Correct

    

path0 = 'C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\If_Smile\\';
#for i in range(0,len(smile_filename)):
#for i in range(10,11):

    #read_smile_data(path,smile_filename[i])
 #   np.savetxt(path0+'If_smile_'+str(i)+'.txt',time_Correction(If_smile(smile_filename[i])))
#
#数据分析部分
'''
for i in range(0,14):
    data = np.loadtxt(path0+'If_smile_'+str(i)+'.txt')
    print(len(data))
    
'''

Video_length = 5208;


Sub_If_smile = np.zeros([Video_length,8])

for i in [0,2,4,6,8,10]:
    If_smile_1 = np.loadtxt(path0+'If_smile_'+str(i)+'.txt')[:,1]
    If_smile_2 = np.loadtxt(path0+'If_smile_'+str(i+1)+'.txt')[:,1]
    If_smile = np.append(If_smile_1,If_smile_2);
    Sub_If_smile[0:len(If_smile),int(i/2)] = If_smile;
    

If_smile = np.loadtxt(path0+'If_smile_12.txt')
Sub_If_smile[0:len(If_smile),6] = If_smile[:,1];

If_smile = np.loadtxt(path0+'If_smile_13.txt')
Sub_If_smile[0:len(If_smile),7] = If_smile[:,1];




plt.plot(Sub_If_smile.sum(axis = 1))
plt.xlabel('time:s')
plt.ylabel('Num of Subjects(smile)')
plt.xlim((0,Video_length))
plt.ylim((0,9))
plt.show()




  
