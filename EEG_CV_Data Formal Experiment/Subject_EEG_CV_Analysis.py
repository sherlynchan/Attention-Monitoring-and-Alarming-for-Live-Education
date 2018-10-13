import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

path = 'E:\\TrainingPlan_Undergraduate\\FinalReport\\Test_CV_result\\';
Video_length = 5208;
Sub_If_Focus = np.zeros([Video_length,8])

for i in [0,2,4,6,8,10]:
    If_Focus_1 = np.loadtxt(path+'EEG_CV_IF_FOCUS'+str(i)+'.txt')
    If_Focus_2 = np.loadtxt(path+'EEG_CV_IF_FOCUS'+str(i+1)+'.txt')
    If_Focus = np.append(If_Focus_1,If_Focus_2);
    Sub_If_Focus[0:len(If_Focus),int(i/2)] = If_Focus;
    

If_Focus = np.loadtxt(path+'EEG_CV_IF_FOCUS12.txt')
Sub_If_Focus[0:len(If_Focus),6] = If_Focus;

If_Focus = np.loadtxt(path+'EEG_CV_IF_FOCUS13.txt')
Sub_If_Focus[0:len(If_Focus),7] = If_Focus;


'''
def itv2time(sUp_h):         
    m=int(sUp_h/60)  
    sUp_m=sUp_h-60*m  
    s=int(sUp_m)  
    return ':'.join(map(str,(m,s)))

time = np.zeros(Video_length)
for i in range(0,Video_length):
    time[i] = i;
    time[i] = itv2time(time[i])
'''

plt.plot(Sub_If_Focus.sum(axis = 1))
plt.xlabel('time:s')
plt.ylabel('Num of Subjects(focus)')
plt.xlim((0,Video_length))
plt.ylim((0,9))
plt.show()

    

    
