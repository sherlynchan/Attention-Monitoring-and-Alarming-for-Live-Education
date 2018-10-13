#测试数据 subject
# 1   CSH
# 2   CXY 
# 3   LBJ
# 4   ZFF
# 5   CBS
# 6   BL
# 7   LWM
# 8   ZJH
import numpy as np
import pandas as pd

#实验数据部分

path = 'C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\';
face_filename = ['CSH_test1_face_data.txt','CSH_test2_face_data.txt',\
                 'CXY_test1_face_data.txt','CXY_test2_face_data.txt',\
                 'LBJ_test1_face_data.txt','LBJ_test2_face_data.txt',\
                 'ZFF_test1_face_data.txt','ZFF_test2_face_data.txt',\
                 'CBS_test1_face_data.txt','CBS_test2_face_data.txt',\
                 'BL_test1_face_data.txt','BL_test2_face_data.txt',\
                 'LWM.test_eye_data_eye_data_face_data.txt','ZJH_test_face_data.txt'
                 ]
eye_filename = ['CSH_test1_eye_data.txt','CSH_test2_eye_data.txt',\
                 'CXY_test1_eye_data.txt','CXY_test2_eye_data.txt',\
                 'LBJ_test1_eye_data.txt','LBJ_test2_eye_data.txt',\
                 'ZFF_test1_eye_data.txt','ZFF_test2_eye_data.txt',\
                 'CBS_test1_eye_data.txt','CBS_test2_eye_data.txt',\
                 'BL_test1_eye_data.txt','BL_test2_eye_data.txt',\
                 'LWM.test_eye_data_eye_data.txt','ZJH_test_eye_data.txt'
                 ]
time_filename = ['CSH_test1_time_data.txt','CSH_test2_time_data.txt',\
                 'CXY_test1_time_data.txt','CXY_test2_time_data.txt',\
                 'LBJ_test1_time_data.txt','LBJ_test2_time_data.txt',\
                 'ZFF_test1_time_data.txt','ZFF_test2_time_data.txt',\
                 'CBS_test1_time_data.txt','CBS_test2_time_data.txt',\
                 'BL_test1_time_data.txt','BL_test2_time_data.txt',\
                 'LWM.test_eye_data_eye_data_time_data.txt','ZJH_test_time_data.txt'
                 ]
'''
#with open(path+filename,'r') as f:
#   lines = f.readlines()
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

    np.savetxt('C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\'+\
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
    
    np.savetxt('C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\'+\
               're_'+eye_filename,data1)

'''
'''
#读取并清洗时间数据
def read_time_data(path, time_filename):
    f =open(path+time_filename);
    data0 = f.readlines()
    data1 = data0[1:]
    for i in range(0,len(data1)):
        data1[i] = int(float(data1[i]));
    np.savetxt('C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\'+\
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
    
    filepath = 'C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\';
    eye_data = pd.read_table(filepath+'re_'+eye_filename, sep =' ',header = None)
    face_data = pd.read_table(filepath+'re_'+face_filename,sep = ' ',header = None)
    time_data = pd.read_table(filepath+'re_'+time_filename,sep = ' ',header = None)
    
    time_data.insert(1,'If_face',1)
    time_data.insert(2,'If_eye',0)
    
    #眼睛的坐标要在脸部的上1/2处
#错了    
   
#    for i in range(0,len(time_data)):
 #       flag = 0;
  #      for j in range(0,int(eye_data.shape[1]/4)): 
   #         if (eye_data.iat[i,4*j+1] >= face_data.iat[i,3]/2) | (eye_data.iat[i,4*j+1] == 0.0):
    #            flag = flag +1;
     #   if flag == int(eye_data.shape[1]/4):
      #      time_data.iat[i,2]  = 0;
       # else:
        #    time_data.iat[i,2]  = 1;
    #time_data.to_csv('If_eye'+filepath+time_filename+'.csv')
   

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
'''




def time_Correction(time_filename):
    filepath = 'C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\';
    time_data = pd.read_csv(filepath+'If_eye'+time_filename.replace('.txt','')+'.csv')
   
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
         


#连续五次分心，则给出警告，警告为0
def CV_if_Focus(time_filename):
    filepath = 'C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\';
    time_data = np.loadtxt(filepath+'TCorrect'+time_filename)
    time_data = np.column_stack((time_data,np.ones((len(time_data),1))))

    for k in range(0,len(time_data)-4):
        if(time_data[k,3] == 0)& (time_data[k+1,3] == 0)&(time_data[k+2,3] == 0)&(time_data[k+3,3] == 0)&(time_data[k+4,3] == 0):
            time_data[k+4,4] = 0;  
    return time_data
   
            
for i in range(0,len(time_filename)):
 
    #judge_if_eye(eye_filename[i],face_filename[i],time_filename[i])
    time_Correction(time_filename[i])
    np.savetxt('C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\Data_CSL\\Used Subject\\CV\\'+'CV_alarm'+str(i)+'.txt',CV_if_Focus(time_filename[i]))
       







            
           
        
               
        
        
    
    
    

    

    
    
    
