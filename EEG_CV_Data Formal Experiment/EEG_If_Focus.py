import numpy as np
import matplotlib.pyplot as plt
from pylab import *


def EEG_if_Focus(att_med_data, ST_CV, ST_EEG, thres):

    #从Data_S开始计算
    Data_S = int(ST_CV) - int(ST_EEG) + 28800;
    
    att_med_data[att_med_data>100] = 100;
    att_med_data = np.column_stack((att_med_data,np.ones((len(att_med_data),1))))
    att_med_data = np.column_stack((att_med_data,np.ones((len(att_med_data),1))))
    att_med_data = np.column_stack((att_med_data,np.ones((len(att_med_data),1))))

    width = 5;
    for i in range(1,len(att_med_data)-width+1):
        att_med_data[width -2 +i,2] = average(att_med_data[(i-1):(width -2 +i),0]);
        att_med_data[width -2 +i,3] = average(att_med_data[(i-1):(width -2 +i),1]);

    #计算专注指数
    att_med_data[:,4] = att_med_data[:,2]/att_med_data[:,3]

    #判断每秒是否分心，专注为1，分心为0
    att_med_data = np.column_stack((att_med_data,np.ones((len(att_med_data),1))))
    for j in range(Data_S,len(att_med_data)-1):
        if att_med_data[j,4] >= thres:
            att_med_data[j,5] = 1;
        else:
            att_med_data[j,5] = 0;
            
    #连续五次分心，则给出警告，警告为 0
    att_med_data = np.column_stack((att_med_data,np.ones((len(att_med_data),1))))

    for k in range(Data_S,len(att_med_data)-width+1):
        if (att_med_data[k,5] ==0) & (att_med_data[k+1,5] ==0) &(att_med_data[k+2,5] ==0) & (att_med_data[k+3,5] ==0) & (att_med_data[k+4,5] ==0):
            att_med_data[k+4,6] = 0
        else:
            att_med_data[k+4,6] = 1

    return att_med_data[:,6]         



#测试数据 subject
# 1   CSH
# 2   CXY 
# 3   LBJ
# 4   ZFF
# 5   CBS
# 6   BL
# 7   LWM
# 8   ZJH


Sub_Threshold = np.loadtxt('E:\\大创\\终期报告\\Sub_Threshold.txt')
path ='E:\\大创\\11月\\ls_EEG_datadelete\\';
file = [path+'CSH_exp_1.txt',path+'CSH_exp_2.txt',path+'CXY_exp_1.txt',path+'CXY_exp_2.txt',\
        path+'LBJ_exp_1.txt',path+'LBJ_exp_2.txt',path+'ZFF_exp_1.txt',path+'ZFF_exp_2.txt',\
        path+'CBS_exp_1.txt',path+'CBS_exp_2.txt',path+'BL_exp_1.txt',path+'BL_exp_2.txt',\
        path+'LWM_exp.txt',path+'ZJH_exp.txt'];
ST_CV = ['1511510407','1511512121','1511530727','1511532463',\
         '1511609276','1511609512','1511680816','1511681055',\
         '1511510313','1511511979','1511618898','1511620480',\
         '1511161265','1511190536'];
ST_EEG = ['1511539207','1511540924','1511559526','1511561263',\
          '1511638664','1511640573','1511710143','1511711714',\
          '1511539108','1511540775','1511647700','1511649283',\
          '1511190067','1511219339'];
'''
for i in [0,2,4,6,8,10]:
    data_0 = np.loadtxt(file[i]);
    np.savetxt('E:\\大创\\终期报告\\EEG_If_Focus'+ str(i) +'.txt',\
                EEG_if_Focus(data_0,ST_CV[i],ST_EEG[i],Sub_Threshold[2,int(i/2)]))


#EEG开始时间稍微晚于视频开始时间

i = 12
data_0 = np.loadtxt(file[i]);
np.savetxt('E:\\大创\\终期报告\\EEG_If_Focus'+ str(i) +'.txt',\
            EEG_if_Focus(data_0,ST_CV[i],ST_CV[i],Sub_Threshold[2,int(i/2)]))


for i in [1,3,7,9,11]:
    data_0 = np.loadtxt(file[i]);
    np.savetxt('E:\\大创\\终期报告\\EEG_If_Focus'+ str(i) +'.txt',\
                EEG_if_Focus(data_0,ST_CV[i],ST_EEG[i],Sub_Threshold[2,int((i-1)/2)]))

#LBJ第二段视频从5分30s开始,因此EEG直接开始，全都可以用
i = 5
data_0 = np.loadtxt(file[i]);
np.savetxt('E:\\大创\\终期报告\\EEG_If_Focus'+ str(i) +'.txt',\
            EEG_if_Focus(data_0,ST_CV[i],str(int(ST_CV[i])+28800),Sub_Threshold[2,int((i-1)/2)]))
#
'''
data_0 = np.loadtxt(file[13]);
np.savetxt('E:\\大创\\终期报告\\EEG_If_Focus13.txt',\
            EEG_if_Focus(data_0,ST_CV[13],ST_EEG[13],Sub_Threshold[2,7]))



