import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import * 
   
#PPT预实验部分

import os  
path = 'C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\PPT_CV\\'; #文件夹目录  
files= os.listdir(path) #得到文件夹下的所有文件名称
face_filename = [];
eye_filename = [];
time_filename = [];
other_filename = [];
for i in range(0,len(files)):
    if files[i].find('face') >= 0:
        face_filename.append(files[i])
    elif files[i].find('eye') >= 0:
        eye_filename.append(files[i])
    elif files[i].find('time') >=0:
        time_filename.append(files[i])
    else:
        other_filename.append(files[i])
        

#读取faces数据
def read_face_data(path, face_filename):
    
    f =open(path+face_filename);
    data = f.read()
    data0 = data.split(']]\n')
    flag = np.zeros(len(data0))

    for i in range(0,len(data0)):
        data0[i] = data0[i].replace('[[','')
        data0[i] = data0[i].replace(']\n [',' ')
        data0[i] = data0[i].split( )
        flag[i] = len(data0[i])

    data1 = np.zeros([len(data0),int(max(flag))]);
    for i in range(0,len(data0)):
        for j in range(0,int(flag[i])):
            data1[i,j] = data0[i][j];

    np.savetxt('E:\\大创\\终期报告\\PPT_CV_Result\\face\\'+\
               're_'+face_filename,data1)

#读取眼部数据    
def read_eye_data(path, eye_filename):
    f =open(path+eye_filename);
    data0 = f.readlines()
    
    flag = np.zeros(len(data0))

    for i in range(0,len(data0)):
        data0[i] = data0[i].replace('], dtype=int32), array([',',')
        data0[i] = data0[i].replace('[array([','')
        data0[i] = data0[i].replace('], dtype=int32)]\n','')
        data0[i] = data0[i].replace('[]\n','')
        data0[i] = data0[i].split(',')
        flag[i] = len(data0[i])

    data1 = np.zeros([len(data0),int(max(flag))]);
    for i in range(0,len(data0)):
        for j in range(0,int(flag[i])):
            if data0[i][j] == '':
                data1[i,j] = float(0);
            else:
                data1[i,j] = float(data0[i][j]);
    
    np.savetxt('E:\\大创\\终期报告\\PPT_CV_Result\\eye\\'+\
               're_'+eye_filename,data1)


#读取并清洗时间数据
def read_time_data(path, time_filename):
    f =open(path+time_filename);
    data0 = f.readlines()
    data1 = data0[1:]
    for i in range(0,len(data1)):
        data1[i] = int(float(data1[i]));
    np.savetxt('E:\\大创\\终期报告\\PPT_CV_Result\\time\\'+\
               're_'+time_filename,data1)


#读取处理subject的眼部、脸、时间数据
for i in range(0,len(face_filename)):
    read_face_data(path, face_filename[i]);
    read_eye_data(path,eye_filename[i]);
    read_time_data(path,time_filename[i]);


   

#判断眼部数据是否为眼睛,即判断是否分心
#1为专注；0为分心

#(x,y,w,h)     
def judge_if_eye(eye_filename,face_filename,time_filename):
    
    filepath = 'E:\\TrainingPlan_Undergraduate\\FinalReport\\PPT_CV_Result\\';
    eye_data = pd.read_table(filepath+'eye\\re_'+eye_filename, sep =' ',header = None)
    face_data = pd.read_table(filepath+'face\\re_'+face_filename,sep = ' ',header = None)
    time_data = pd.read_table(filepath+'time\\re_'+time_filename,sep = ' ',header = None)
    
    time_data.insert(1,'If_face',1)
    time_data.insert(2,'If_eye',0)
    
    #眼睛的坐标要在脸部的上1/2处
    for i in range(0,len(time_data)):
        flag = 0;
        for j in range(0,int(eye_data.shape[1]/4)):
            if (int(eye_data.iat[i,4*j+1]) < int(face_data.iat[i,3]/2)) & (int(eye_data.iat[i,4*j+1]) > 0):
                flag = flag +1;
            else:
                flag = flag +0
        if flag >=1:
            time_data.iat[i,2]  = 1

    time_data.to_csv(filepath+'If_eye'+time_filename.replace('.txt','')+'.csv')


#去重并添加行，校正时间
def time_Correction(time_filename):
    filepath = 'E:\\TrainingPlan_Undergraduate\\FinalReport\\PPT_CV_Result\\';
    time_data = pd.read_table(filepath+'If_eye'+time_filename.replace('.txt','.csv'),sep = ',')
    #flag = np.ones(len(time_data))
    time_min = int(time_data.iat[0,1])
    time_max = int(time_data.iat[len(time_data)-1,1])
    time_data_Correct = np.zeros([time_max - time_min+1,time_data.shape[1]])
    time_data_Correct[:,1] = range(time_min,time_max+1)
    #time_count = (time_data.iloc[:,1]).value_counts()
    
    time_exist = list(set(time_data.iloc[:,1]))
    time_data = np.array(time_data)
    for i in range(0,len(time_data_Correct)):
        if(time_min+i) in time_exist:
            time_data_Correct[i] = time_data[np.where(time_data[:,1]== i+time_min)][0]
        
    np.savetxt(filepath+'TCorrect'+time_filename,time_data_Correct)

            #j = time_count[time_min+i]
                
            #time_data_Correct[i] = time_data.iloc[j]
        
        
            #time_data.drop(i+1,axis = 0,inplace = True)
            #flag[i+1] = 0;
            #time_data = np.delete(time_data, i+1, 0)
            


#连续五次分心，则给出警告，警告为0
def CV_if_Focus(time_filename):
    filepath = 'E:\\TrainingPlan_Undergraduate\\FinalReport\\PPT_CV_Result\\';
    time_data = np.loadtxt(filepath+'TCorrect'+time_filename)
    time_data = np.column_stack((time_data,np.ones((len(time_data),1))))

    for k in range(0,len(time_data)-4):
        if(time_data[k,3] == 0)& (time_data[k+1,3] == 0)&(time_data[k+2,3] == 0)&(time_data[k+3,3] == 0)&(time_data[k+4,3] == 0):
            time_data[k+4,4] = 0;  
    return time_data
   
            
for i in range(0,len(time_filename)):
 
    #judge_if_eye(eye_filename[i],face_filename[i],time_filename[i])
    #time_Correction(time_filename[i])
    np.savetxt('E:\\TrainingPlan_Undergraduate\\FinalReport\\PPT_CV_Result\\'+'PPT_CV_alarm'+str(i)+'.txt',CV_if_Focus(time_filename[i]))
    

#（不含右边）
#12s - 22s  专注
#24s - 34s  专注
#36s - 46s  专注
#52s - 62s  分心
#64s - 74s  分心
#76s - 86s  分心
#104s - 114s专注
#116s - 126s专注
#128s - 138s专注
#144s - 154s分心
#156s - 166s分心
#168s - 178s分心

#CV数据分析
def CorrectRate(i):
    data = np.loadtxt('E:\\TrainingPlan_Undergraduate\\FinalReport\\PPT_CV_Result\\'+'PPT_CV_alarm'+str(i)+'.txt')
   
    data = np.column_stack((data,2*np.ones((len(data),1))))
    from itertools import chain
    
    if len(data)>=178:
        data[12 : 22,5] = 1;
        data[24 : 34,5] = 1;
        data[36 : 46,5] = 1;
        data[52 : 62,5] = 0;     
        data[64 : 74,5] = 0;
        data[76 : 86,5] = 0;
        data[104 : 114,5] = 1;
        data[116 : 126,5] = 1;
        data[128 : 138,5] = 1; 
        data[144 : 154,5] = 0;     
        data[156 : 166,5] = 0;
        data[168 : 178,5] = 0;
    

        
        correct = data[[range(12,22),range(24,34),range(36,46),range(52,62),range(64,74),range(76,86),range(104,114),range(116,126),range(128,138),range(144,154),range(156,166),range(168,178)],4] == data[[range(12,22),range(24,34),range(36,46),range(52,62),range(64,74),range(76,86),range(104,114),range(116,126),range(128,138),range(144,154),range(156,166),range(168,178)],5]
        Correct = list(chain(*correct)).count(True)
        #print(str(i)+' '+str(len(data))+' '+ str(Correct/120)) 
        return Correct,120, Correct/120
    else:
        data[12 : 22,5] = 1;
        data[24 : 34,5] = 1;
        data[36 : 46,5] = 1;
        data[52 : 62,5] = 0;     
        data[64 : 74,5] = 0;
        data[76 : 86,5] = 0;
        correct = data[[range(12,22),range(24,34),range(36,46),range(52,62),range(64,74),range(76,86)],4] == \
                  data[[range(12,22),range(24,34),range(36,46),range(52,62),range(64,74),range(76,86)],5]
        Correct = list(chain(*correct)).count(True)
        #print(str(i)+' '+str(len(data))+' '+ str(Correct/60)) 
        return Correct,60,Correct/60

CR = np.zeros([41,3]);

for i in range(0,41):
    CR[i] = CorrectRate(i);
    
CR_H = CR[CR[:,2]>0.5]    
plt.plot(CR_H[:,2])
plt.plot(np.ones(24)*sum(CR_50[:,0])/sum(CR_50[:,1]))
plt.ylim(0,1)
plt.xlabel('subject')
plt.ylabel('CorrectRate')
plt.show()



#测试数据 subject
# 1   CSH     0.5166666666666667     
# 2   CXY     0.825
# 3   LBJ
# 4   ZFF
# 5   CBS
# 6   BL      0.6416666666666667
# 7   LWM
# 8   ZJH
    

'''
0 205 0.975
1 191 0.8833333333333333
2 190 0.9916666666666667
3 196 0.4083333333333333
4 197 0.5583333333333333
5 198 0.9666666666666667
6 192 0.5416666666666666
7 200 0.5166666666666667
8 200 0.5
9 199 0.6416666666666667
10 189 0.625
11 189 0.7333333333333333
#BL:
#12 233 0.55
#13 195 0.6416666666666667
#14 191 0.6
#
15 203 0.6333333333333333
16 193 0.3416666666666667
17 105 0.8333333333333334
#CSH
#18 160 0.5166666666666667
#19 190 0.43333333333333335
#CXY
20 198 0.825
21 185 0.4
22 194 0.6666666666666666
#
23 195 0.5666666666666667
24 193 0.5666666666666667
25 184 0.7166666666666667
26 206 0.325
27 197 0.475
28 192 0.38333333333333336
29 186 0.625
#LBJ
#30 190 0.5
#31 192 0.5
#32 189 0.4083333333333333
#LWM
#33 178 0.425
#ZFF
#34 193 0.5
#35 184 0.5
#36 190 0.5
#37 200 0.5
#38 211 0.5083333333333333
#39 200 0.5
#ZJH
40 186 0.6166666666666667
'''








