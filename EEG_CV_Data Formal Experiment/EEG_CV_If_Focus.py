import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *


#测试数据 subject
# 1   CSH   
# 2   CXY 
# 3   LBJ
# 4   ZFF
# 5   CBS
# 6   BL
# 7   LWM
# 8   ZJH

'''
path = 'E:\\大创\\终期报告\\';
for i in range(0,14):
    f = open(path+'CV_If_focus'+str(i)+'.csv')
    CV_alarm = pd.read_csv(f)
    CV_ALARM = CV_alarm[['CV_alarm']]
    EEG_alarm = np.loadtxt(path+'EEG_if_focus'+str(i)+'.txt')
   
    
    
    if len(CV_alarm) <= len(EEG_alarm):
        EEG_CV_ALARM = np.ones(len(CV_alarm))
        for j in range(0,len(CV_alarm)):
            if (CV_ALARM.iat[j,0] == 0) & (EEG_alarm[j] == 0):
                EEG_CV_ALARM[j] = 0
        print(len(CV_ALARM) - CV_ALARM.sum())
         
        print(len(CV_ALARM) - EEG_alarm[0:len(CV_alarm)].sum())
                
    else:
        EEG_CV_ALARM = np.ones(len(EEG_alarm))
        for j in range(0,len(EEG_alarm)):
            if (CV_ALARM.iat[j,0] == 0) & (EEG_alarm[j] == 0):
                EEG_CV_ALARM[j] = 0
        print(len(EEG_alarm) - CV_ALARM[0:len(EEG_alarm)].sum())
        print(len(EEG_alarm) - EEG_alarm.sum())
            
   
   print(str(i))
   print(EEG_CV_ALARM.sum())
   print(len(EEG_CV_ALARM))
   np.savetxt(path+'EEG_CV_IF_FOCUS'+str(i)+'.txt', EEG_CV_ALARM)
'''   
path1 = 'C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\';
path2 = 'E:\\TrainingPlan_Undergraduate\\FinalReport\\';
path3 = 'E:\\TrainingPlan_Undergraduate\\FinalReport\\Test_CV_result\\';
for i in range(0,14):
    CV_alarm = np.loadtxt(path1+'CV_alarm'+str(i)+'.txt')
    CV_ALARM = CV_alarm[:,4];
    EEG_alarm = np.loadtxt(path2+'EEG_if_focus'+str(i)+'.txt')
   
    
    
    if len(CV_alarm) <= len(EEG_alarm):
        EEG_CV_ALARM = np.ones(len(CV_alarm))
        for j in range(0,len(CV_alarm)):
            if (CV_ALARM[j] == 0) & (EEG_alarm[j] == 0):
                EEG_CV_ALARM[j] = 0
        #print(len(CV_ALARM) - sum(CV_ALARM))         
        #print(len(CV_ALARM) - EEG_alarm[0:len(CV_alarm)].sum())
                
    else:
        EEG_CV_ALARM = np.ones(len(EEG_alarm))
        for j in range(0,len(EEG_alarm)):
            if (CV_ALARM[j] == 0) & (EEG_alarm[j] == 0):
                EEG_CV_ALARM[j] = 0
        #print(len(EEG_alarm) - CV_ALARM[0:len(EEG_alarm)].sum())
        #print(len(EEG_alarm) - EEG_alarm.sum())
            
    print(str(i))
    print(len(EEG_CV_ALARM) - EEG_CV_ALARM.sum())
    print(len(EEG_CV_ALARM))
    #np.savetxt(path3+'EEG_CV_IF_FOCUS'+str(i)+'.txt', EEG_CV_ALARM)
    
                
        
    


