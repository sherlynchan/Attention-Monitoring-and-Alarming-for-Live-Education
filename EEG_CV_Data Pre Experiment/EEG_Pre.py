#0s(含左边，不包含右边)
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

import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def EEG_threshold (data_0, ST_CV, ST_EEG):
    
    data_0[data_0>100] = 100
    data_1 = np.column_stack((data_0,2*np.ones((len(data_0),1))))
    Data_S = int(ST_CV) - int(ST_EEG) + 28800;

    #第2列为label，1代表专注，0代表分心
    data_1[Data_S +12 : Data_S+22,2] = 1;
    data_1[Data_S +24 : Data_S+34,2] = 1;
    data_1[Data_S +36 : Data_S+46,2] = 1; 
    data_1[Data_S +52 : Data_S+62,2] = 0;     
    data_1[Data_S +64 : Data_S+74,2] = 0;
    data_1[Data_S +76 : Data_S+86,2] = 0;

    data_1[Data_S +104 : Data_S+114,2] = 1;
    data_1[Data_S +116 : Data_S+126,2] = 1;
    data_1[Data_S +128 : Data_S+138,2] = 1; 
    data_1[Data_S +144 : Data_S+154,2] = 0;     
    data_1[Data_S +156 : Data_S+166,2] = 0;
    data_1[Data_S +168 : Data_S+178,2] = 0;  

    data_2 = np.column_stack((data_1,np.ones((len(data_1),1))))
    data_2[:,3] = data_2[:,0]/data_2[:,1]
    
    data_3 = np.column_stack((data_2,np.ones((len(data_2),1))))
    data_3 = np.column_stack((data_3,np.ones((len(data_3),1))))
    data_3 = np.column_stack((data_3,np.ones((len(data_3),1))))

    width = 5;
    for i in range(1,len(data_3)-width+1):
        data_3[width -2 +i,4] = average(data_3[(i-1):(width -2 +i),0]);
        data_3[width -2 +i,5] = average(data_3[(i-1):(width -2 +i),1]);

    data_3[:,6] = data_3[:,4]/data_3[:,5]
    
    threshold=np.hstack((data_3[Data_S +12 +4 : Data_S+22,6],\
                         data_3[Data_S +24 +4 : Data_S+34,6],\
                         data_3[Data_S +36 +4 : Data_S+46,6],\
                         data_3[Data_S +52 +4 : Data_S+62,6],\
                         data_3[Data_S +64 +4 : Data_S+74,6],\
                         data_3[Data_S +76 +4 : Data_S+86,6],\
                         data_3[Data_S +104 +4 : Data_S+114,6],\
                         data_3[Data_S +116 +4 : Data_S+126,6],\
                         data_3[Data_S +128 +4 : Data_S+138,6],\
                         data_3[Data_S +144 +4 : Data_S+154,6],\
                         data_3[Data_S +156 +4 : Data_S+166,6],\
                         data_3[Data_S +168 +4 : Data_S+178,6]));
    Threshold = threshold.reshape((12,6));
    return Threshold

'''
    att_ave = average(data_3[where(data_3[:,2] == 1),4])
    natt_ave = average(data_3[where(data_3[:,2] == 0),4])
    med_ave = average(data_3[where(data_3[:,2] == 1),5])
    nmed_ave = average(data_3[where(data_3[:,2] == 0),5])
    ratio_ave = average(data_3[where(data_3[:,2] == 1),6])
    nratio_ave = average(data_3[where(data_3[:,2] == 0),6])


    att_ave_1 = average(data_3[Data_S +12 : Data_S+22,0]);
    att_ave_2 = average(data_3[Data_S +24 : Data_S+34,0]);
    att_ave_3 = average(data_3[Data_S +36 : Data_S+46,0]); 
    natt_ave_1 = average(data_3[Data_S +52 : Data_S+62,0]);     
    natt_ave_2 = average(data_3[Data_S +64 : Data_S+74,0]);
    natt_ave_3 = average(data_3[Data_S +76 : Data_S+86,0]);

    att_ave_4 = average(data_3[Data_S +104 : Data_S+114,0]);
    att_ave_5 = average(data_3[Data_S +116 : Data_S+126,0]);
    att_ave_6 = average(data_3[Data_S +128 : Data_S+138,0]); 
    natt_ave_4 = average(data_3[Data_S +144 : Data_S+154,0]);     
    natt_ave_5 = average(data_3[Data_S +156 : Data_S+166,0]);
    natt_ave_6 = average(data_3[Data_S +168 : Data_S+178,0]);  

    med_ave_1 = average(data_3[Data_S +12 : Data_S+22,1]);
    med_ave_2 = average(data_3[Data_S +24 : Data_S+34,1]);
    med_ave_3 = average(data_3[Data_S +36 : Data_S+46,1]); 
    nmed_ave_1 = average(data_3[Data_S +52 : Data_S+62,1]);     
    nmed_ave_2 = average(data_3[Data_S +64 : Data_S+74,1]);
    nmed_ave_3 = average(data_3[Data_S +76 : Data_S+86,1]);

    med_ave_4 = average(data_3[Data_S +104 : Data_S+114,1]);
    med_ave_5 = average(data_3[Data_S +116 : Data_S+126,1]);
    med_ave_6 = average(data_3[Data_S +128 : Data_S+138,1]); 
    nmed_ave_4 = average(data_3[Data_S +144 : Data_S+154,1]);     
    nmed_ave_5 = average(data_3[Data_S +156 : Data_S+166,1]);
    nmed_ave_6 = average(data_3[Data_S +168 : Data_S+178,1]); 



    
    
    return att_ave, natt_ave, med_ave, nmed_ave,ratio_ave, nratio_ave,\
           att_ave_1,att_ave_2,att_ave_3,att_ave_4,att_ave_5,att_ave_6,\
           natt_ave_1,natt_ave_2,natt_ave_3,natt_ave_4,natt_ave_5,natt_ave_6,\
           med_ave_1,med_ave_2,med_ave_3,med_ave_4,med_ave_5,med_ave_6,\
           nmed_ave_1,nmed_ave_2,nmed_ave_3,nmed_ave_4,nmed_ave_5,nmed_ave_6

'''
 
'''        
plt.plot(range(Data_S +10,Data_S+20),data_1[Data_S +10 : Data_S+20,0],'r-')
plt.plot(range(Data_S +22,Data_S+32),data_1[Data_S +22 : Data_S+32,0],'r-')
plt.plot(range(Data_S +34,Data_S+44),data_1[Data_S +34 : Data_S+44,0],'r-')

plt.plot(range(Data_S +50,Data_S+60),data_1[Data_S +50 : Data_S+60,0],'g-')
plt.plot(range(Data_S +62,Data_S+72),data_1[Data_S +62 : Data_S+72,0],'g-')
plt.plot(range(Data_S +74,Data_S+84),data_1[Data_S +74 : Data_S+84,0],'g-')

plt.plot(range(Data_S +100,Data_S+110),data_1[Data_S +100 : Data_S+110,0],'r-')
plt.plot(range(Data_S +112,Data_S+122),data_1[Data_S +112 : Data_S+122,0],'r-')
plt.plot(range(Data_S +124,Data_S+134),data_1[Data_S +124 : Data_S+134,0],'r-')

plt.plot(range(Data_S +140,Data_S+150),data_1[Data_S +140 : Data_S+150,0],'g-')
plt.plot(range(Data_S +152,Data_S+162),data_1[Data_S +152 : Data_S+162,0],'g-')
plt.plot(range(Data_S +164,Data_S+174),data_1[Data_S +164 : Data_S+174,0],'g-')

att_ave = average(data_1[where(data_1[:,2] == 1),0])
dis_ave = average(data_1[where(data_1[:,2] == 0),0])
 
    
#plt.plot(data_2[:,3])


plt.plot(range(Data_S +10,Data_S+20),data_2[Data_S +10 : Data_S+20,3],'r-')
plt.plot(range(Data_S +22,Data_S+32),data_2[Data_S +22 : Data_S+32,3],'r-')
plt.plot(range(Data_S +34,Data_S+44),data_2[Data_S +34 : Data_S+44,3],'r-')

plt.plot(range(Data_S +50,Data_S+60),data_2[Data_S +50 : Data_S+60,3],'g-')
plt.plot(range(Data_S +62,Data_S+72),data_2[Data_S +62 : Data_S+72,3],'g-')
plt.plot(range(Data_S +74,Data_S+84),data_2[Data_S +74 : Data_S+84,3],'g-')

plt.plot(range(Data_S +100,Data_S+110),data_2[Data_S +100 : Data_S+110,3],'r-')
plt.plot(range(Data_S +112,Data_S+122),data_2[Data_S +112 : Data_S+122,3],'r-')
plt.plot(range(Data_S +124,Data_S+134),data_2[Data_S +124 : Data_S+134,3],'r-')

plt.plot(range(Data_S +140,Data_S+150),data_2[Data_S +140 : Data_S+150,3],'g-')
plt.plot(range(Data_S +152,Data_S+162),data_2[Data_S +152 : Data_S+162,3],'g-')
plt.plot(range(Data_S +164,Data_S+174),data_2[Data_S +164 : Data_S+174,3],'g-')


    

#plt.plot(data_3[:,3])
plt.plot(data_3[:,6])
plt.plot(range(Data_S +10,Data_S+20),data_3[Data_S +10 : Data_S+20,6],'r-')
plt.plot(range(Data_S +22,Data_S+32),data_3[Data_S +22 : Data_S+32,6],'r-')
plt.plot(range(Data_S +34,Data_S+44),data_3[Data_S +34 : Data_S+44,6],'r-')

plt.plot(range(Data_S +50,Data_S+60),data_3[Data_S +50 : Data_S+60,6],'g-')
plt.plot(range(Data_S +62,Data_S+72),data_3[Data_S +62 : Data_S+72,6],'g-')
plt.plot(range(Data_S +74,Data_S+84),data_3[Data_S +74 : Data_S+84,6],'g-')

plt.plot(range(Data_S +100,Data_S+110),data_3[Data_S +100 : Data_S+110,6],'r-')
plt.plot(range(Data_S +112,Data_S+122),data_3[Data_S +112 : Data_S+122,6],'r-')
plt.plot(range(Data_S +124,Data_S+134),data_3[Data_S +124 : Data_S+134,6],'r-')

plt.plot(range(Data_S +140,Data_S+150),data_3[Data_S +140 : Data_S+150,6],'g-')
plt.plot(range(Data_S +152,Data_S+162),data_3[Data_S +152 : Data_S+162,6],'g-')
plt.plot(range(Data_S +164,Data_S+174),data_3[Data_S +164 : Data_S+174,6],'g-')

plt.show()
#plt.close()

#np.savetxt('C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\DataAnalysis\\label_EEG_zjh.txt',data_1)




def EEG_pre(data):
    data = np.column_stack((data,np.ones((len(data),1))))
    data = np.column_stack((data,np.ones((len(data),1))))
    width = 5;
    
    for i in range(1,len(data)):
        data[width -2 +i,2] = average(data[(i-1):(width -2 +i),0]);
        data[width -2 +i,3] = average(data[(i-1):(width -2 +i),1]);

     
'''
#测试数据 subject
# 1   CSH
# 2   CXY 
# 3   LBJ
# 4   ZFF
# 5   CBS
# 6   BL
# 7   LWM
# 8   ZJH

path ='E:\\大创\\11月\\ls_EEG_datadelete\\';
file = [
         #path +'ggq1.txt',path +'ggq2.txt',path +'ggq3.txt',\
         #path +'wyt1.txt',path +'wyt2.txt',path +'wyt3.txt',\
         #path +'zrl1.txt',path +'zrl2.txt',path +'zrl3.txt',\
         #path +'hhl1.txt',path +'hhl2.txt',path +'hhl3.txt',\
         path +'csh1.txt',path +'csh2.txt',path +'csh3.txt',\
         path +'cxy1.txt',path +'cxy2.txt',path +'cxy3.txt',\
         path +'lbj1.txt',path +'lbj2.txt',path +'lbj3.txt',\
         path +'zff1.txt',path +'zff2.txt',path +'zff3.txt',\
         
         
         path +'cbs1.txt',path +'cbs2.txt',path +'cbs3.txt',\
         #path +'ljy1.txt',path +'ljy2.txt',path +'ljy3.txt',\
         #path +'lzt1.txt',path +'lzt2.txt',path +'lzt3.txt',\
         path +'bl1.txt',
         #path +'bl2.txt',
         path +'bl3.txt',\
         
         
         #path +'dls1.txt',path +'dls2.txt',path +'dls3.txt',\
         #path +'yc1.txt',path +'yc2.txt',path +'yc3.txt',\
         #path +'csl1.txt',path +'csl2.txt',path +'csl3.txt',\
         path +'lwm1.txt',\
         #path +'lwm2.txt',path +'lwm3.txt',\
         path +'zjh1.txt'
         #path +'zjh2.txt',path +'zjh3.txt',\
         #path +'zbz1.txt',path +'zbz2.txt',path +'zbz3.txt',\
         #path +'zsj1.txt',path +'zsj2.txt',path +'zsj3.txt',\
         #path +'jn1.txt',path +'jn2.txt',path +'jn3.txt'
         ];

ST_CV = [
    #'1511424346','1511424642','1511424922',
        # '1511425488','1511425768','1511426012',\
         #'1511426012','1511426416','1511426897','1511625474','1511625717','1511625952',\
         '1511509793','1511510037','1511514127','1511530123','1511530405','1511534512',\
         '1511609276','1511609512','1511613371','1511680816','1511681055','1511684884',\
         '1511509505','1511509825','1511514033',\
        #'1511616025','1511616274','1511620321',\
        #'1511432132','1511432389','1511436398',\
         '1511618323',
         #'1511618640',
         '1511622797',\
         '1511160770',\
         '1511190113'
        # '','','',
         ];
ST_EEG =[
    #'1511453139','1511453437','1511453760',
        # '1511454283','1511454561','1511454805',\
         #'1511455209','1511455438','1511455692','1511654263','1511654509','1511654743',\
         '1511538592','1511538837','1511542923','1511558923','1511559207','1511563313',\
         '1511638077','1511638313','1511642172','1511709615','1511709856','1511713682',\
         '1511538298','1511538619','1511542827',\
         #'1511644821','1511645070','1511649083',\
         #'','','',\
         '1511647125',\
         #'1511647442',
         '1511651599',\
         '1511189566',\
         '1511218916'
         ];

#EEG_ave = np.zeros([len(file),30])
#EEG_ave_apart = np.zeros([len(file),24])
#threshold = np.zeros([12,len(file)])

for i in range(1,len(file)+1):
#i = 1;
    data_0 = np.loadtxt(file[i-1]);
    np.savetxt('E:\\大创\\终期报告\\Threshold_'+ str(i-1) +'.txt',EEG_threshold(data_0,ST_CV[i-1],ST_EEG[i-1]))
   # [EEG_ave[i-1,0], EEG_ave[i-1,1], EEG_ave[i-1,2], EEG_ave[i-1,3],EEG_ave[i-1,4], EEG_ave[i-1,5]\
    #EEG_ave[i-1,:] = EEG_threshold(data_0,ST_CV[i-1],ST_EEG[i-1])
 
      #EEG_ave[i-1,6], EEG_ave[i-1,7], EEG_ave[i-1,8], EEG_ave[i-1,9],EEG_ave[i-1,10], EEG_ave[i-1,11],\
    # EEG_ave[i-1,12], EEG_ave[i-1,13], EEG_ave[i-1,14], EEG_ave[i-1,15],EEG_ave[i-1,16], EEG_ave[i-1,17],\
     #EEG_ave[i-1,18], EEG_ave[i-1,19], EEG_ave[i-1,20], EEG_ave[i-1,21],EEG_ave[i-1,22], EEG_ave[i-1,23],\
     #EEG_ave[i-1,24], EEG_ave[i-1,25], EEG_ave[i-1,26], EEG_ave[i-1,27],EEG_ave[i-1,28], EEG_ave[i-1,29] 

'''
#画出滑动窗口图
    
data_0 = np.loadtxt(file[22]);
data_1 = np.column_stack((data_0,2*np.ones((len(data_0),1))))
Data_S = int(ST_CV[22]) - int(ST_EEG[22]) + 28800;

    #第2列为label，1代表专注，0代表分心
data_1[Data_S +12 : Data_S+22,2] = 1;
data_1[Data_S +24 : Data_S+34,2] = 1;
data_1[Data_S +36 : Data_S+46,2] = 1; 
data_1[Data_S +52 : Data_S+62,2] = 0;     
data_1[Data_S +64 : Data_S+74,2] = 0;
data_1[Data_S +76 : Data_S+86,2] = 0;

data_1[Data_S +104 : Data_S+114,2] = 1;
data_1[Data_S +116 : Data_S+126,2] = 1;
data_1[Data_S +128 : Data_S+138,2] = 1; 
data_1[Data_S +144 : Data_S+154,2] = 0;     
data_1[Data_S +156 : Data_S+166,2] = 0;
data_1[Data_S +168 : Data_S+178,2] = 0;  

data_2 = np.column_stack((data_1,np.ones((len(data_1),1))))
data_2[:,3] = data_2[:,0]/data_2[:,1]

data_3 = np.column_stack((data_2,np.ones((len(data_2),1))))
data_3 = np.column_stack((data_3,np.ones((len(data_3),1))))
data_3 = np.column_stack((data_3,np.ones((len(data_3),1))))

width = 5;
for i in range(1,len(data_3)-width+1):
        data_3[width -2 +i,4] = average(data_3[(i-1):(width -2 +i),0]);
        data_3[width -2 +i,5] = average(data_3[(i-1):(width -2 +i),1]);
        
plt.plot(data_3[:,0])
plt.plot(data_3[:,4])
labels = ['','']
plt.legend(labels,loc = 'upper left')
#plt.plot(data_3[:,1])
#plt.plot(data_3[:,5])
plt.show()



'''
   
'''
plt.plot(range(Data_S +10,Data_S+20),data_1[Data_S +10 : Data_S+20,0],'r-')
plt.plot(range(Data_S +22,Data_S+32),data_1[Data_S +22 : Data_S+32,0],'r-')
plt.plot(range(Data_S +34,Data_S+44),data_1[Data_S +34 : Data_S+44,0],'r-')

plt.plot(range(Data_S +50,Data_S+60),data_1[Data_S +50 : Data_S+60,0],'g-')
plt.plot(range(Data_S +62,Data_S+72),data_1[Data_S +62 : Data_S+72,0],'g-')
plt.plot(range(Data_S +74,Data_S+84),data_1[Data_S +74 : Data_S+84,0],'g-')

plt.plot(range(Data_S +100,Data_S+110),data_1[Data_S +100 : Data_S+110,0],'r-')
plt.plot(range(Data_S +112,Data_S+122),data_1[Data_S +112 : Data_S+122,0],'r-')
plt.plot(range(Data_S +124,Data_S+134),data_1[Data_S +124 : Data_S+134,0],'r-')

plt.plot(range(Data_S +140,Data_S+150),data_1[Data_S +140 : Data_S+150,0],'g-')
plt.plot(range(Data_S +152,Data_S+162),data_1[Data_S +152 : Data_S+162,0],'g-')
plt.plot(range(Data_S +164,Data_S+174),data_1[Data_S +164 : Data_S+174,0],'g-')

att_ave = average(data_1[where(data_1[:,2] == 1),0])
dis_ave = average(data_1[where(data_1[:,2] == 0),0])
''' 
    
#plt.plot(data_2[:,3])
'''

plt.plot(range(Data_S +10,Data_S+20),data_2[Data_S +10 : Data_S+20,3],'r-')
plt.plot(range(Data_S +22,Data_S+32),data_2[Data_S +22 : Data_S+32,3],'r-')
plt.plot(range(Data_S +34,Data_S+44),data_2[Data_S +34 : Data_S+44,3],'r-')

plt.plot(range(Data_S +50,Data_S+60),data_2[Data_S +50 : Data_S+60,3],'g-')
plt.plot(range(Data_S +62,Data_S+72),data_2[Data_S +62 : Data_S+72,3],'g-')
plt.plot(range(Data_S +74,Data_S+84),data_2[Data_S +74 : Data_S+84,3],'g-')

plt.plot(range(Data_S +100,Data_S+110),data_2[Data_S +100 : Data_S+110,3],'r-')
plt.plot(range(Data_S +112,Data_S+122),data_2[Data_S +112 : Data_S+122,3],'r-')
plt.plot(range(Data_S +124,Data_S+134),data_2[Data_S +124 : Data_S+134,3],'r-')

plt.plot(range(Data_S +140,Data_S+150),data_2[Data_S +140 : Data_S+150,3],'g-')
plt.plot(range(Data_S +152,Data_S+162),data_2[Data_S +152 : Data_S+162,3],'g-')
plt.plot(range(Data_S +164,Data_S+174),data_2[Data_S +164 : Data_S+174,3],'g-')

'''

    

'''
#plt.plot(data_3[:,3])
plt.plot(data_3[:,6])
plt.plot(range(Data_S +10,Data_S+20),data_3[Data_S +10 : Data_S+20,6],'r-')
plt.plot(range(Data_S +22,Data_S+32),data_3[Data_S +22 : Data_S+32,6],'r-')
plt.plot(range(Data_S +34,Data_S+44),data_3[Data_S +34 : Data_S+44,6],'r-')

plt.plot(range(Data_S +50,Data_S+60),data_3[Data_S +50 : Data_S+60,6],'g-')
plt.plot(range(Data_S +62,Data_S+72),data_3[Data_S +62 : Data_S+72,6],'g-')
plt.plot(range(Data_S +74,Data_S+84),data_3[Data_S +74 : Data_S+84,6],'g-')

plt.plot(range(Data_S +100,Data_S+110),data_3[Data_S +100 : Data_S+110,6],'r-')
plt.plot(range(Data_S +112,Data_S+122),data_3[Data_S +112 : Data_S+122,6],'r-')
plt.plot(range(Data_S +124,Data_S+134),data_3[Data_S +124 : Data_S+134,6],'r-')

plt.plot(range(Data_S +140,Data_S+150),data_3[Data_S +140 : Data_S+150,6],'g-')
plt.plot(range(Data_S +152,Data_S+162),data_3[Data_S +152 : Data_S+162,6],'g-')
plt.plot(range(Data_S +164,Data_S+174),data_3[Data_S +164 : Data_S+174,6],'g-')

plt.show()
#plt.close()
'''        
    
     
  
    
'''    
#t检验
def t_test(attention_data,distraction_data):
        from scipy.stats import ttest_ind
        t,p = ttest_ind(attention,distraction)
        return t,p


data = np.loadtxt('E:\\大创\\终期报告\\数据处理和分析\\threshold_0.txt')

  



t,p = ttest_ind((data_re[[0,1,2,6,7,8],:]).reshape((1,36)),(data_re[[3,4,5,9,10,11],:]).reshape((1,36)))

'''


 '''       
        
ST_EEG = ['1511905252','1511905486','1511905713']
ST_CV = ['1511876452','1511876684','1511876913']
path ='E:\\大创\\11月\\ls_EEG_datadelete\\';
file = [path + 'zffn1.txt', path+'zffn2.txt', path+'zffn3.txt']
for i in range(1,len(file)+1):
#i = 1;
    data_0 = np.loadtxt(file[i-1]);
    np.savetxt('E:\\大创\\终期报告\\Threshold_'+ str(i+18) +'.txt',EEG_threshold(data_0,ST_CV[i-1],ST_EEG[i-1]))

'''
