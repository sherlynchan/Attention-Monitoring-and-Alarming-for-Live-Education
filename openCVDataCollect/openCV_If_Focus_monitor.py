import numpy as np
import cv2
import time
import os

#加载面部识别文件
face_cascade = cv2.CascadeClassifier('C:\\Users\Administrator\Desktop\openCV_eye_tracking\haarcascade_frontalface_default.xml')
#加载眼部识别文件(请按文件实际存储路径进行调整)
eye_cascade = cv2.CascadeClassifier('C:\\Users\Administrator\Desktop\openCV_eye_tracking\haarcascade_eye.xml')
#戴眼镜眼部识别
eyeglasses_cascade = cv2.CascadeClassifier('C:\\Users\Administrator\Desktop\openCV_eye_tracking\haarcascade_eye_tree_eyeglasses.xml')
#笑脸检测
smile_cascade = cv2.CascadeClassifier('C:\\Users\Administrator\Desktop\openCV_eye_tracking\haarcascade_smile.xml')


#打开摄像头获取视频


#size = (640,480)
cap = cv2.VideoCapture(0)
size =(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
       int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#编译并输出保存视频
#OpenCV: FFMPEG: tag 0xffffffff/' ' is not found (format 'avi / AVI (Audio Video Interleaved)')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.cv.CV_FOURCC('D', 'I', 'B', '')
#fourcc = cv2.VideoWriter_fourcc('D','I','V','X')
#fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter('Good_output.avi',fourcc, 25,size)

eye_data = open('1125_hhl_eye_data_3.txt','w')
face_data = open('1125_hhl_face_data_3.txt','w')
time_data = open('1125_hhl_time_data_3.txt','w')
smile_data = open('1125_hhl_smile_data_3.txt','w')
tfe_data = open('1125_hhl_tfe_data_3.txt','w')


os.startfile('C:\\Users\\Administrator\\Desktop\\openCV_eye_tracking\\阈值测定视频.mp4')
print((time.time(),'ppt_start'),file = time_data)


#os.startfile('E:\\大创\\视频\\zsj\\M2U00004.MPG')
#print(time.time(),file = eye_data)

#无限循环
while(True):
    #获取视频及返回状态
    ret, img = cap.read()
    if ret == True:
       out.write(img)
        #将获取的视频转化为灰色
       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #检测视频中的人脸，并用vector保存人脸的坐标、大小（用矩形表示）
        #Rect(x,y,w,h)
       faces = face_cascade.detectMultiScale(gray, 1.3, 5)
       
            
        #脸部检测
       for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]




            smiles = smile_cascade.detectMultiScale(gray[int(y+h/2):y+h, x:x+w],4,5)  


            
            
            
        #检测视频中脸部的眼睛，并用vector保存眼睛的坐标、大小（用矩形表示）

            eyes = eyeglasses_cascade.detectMultiScale(roi_gray,1.3,2)
             #eyes = eyeglasses_cascade.detectMultiScale(roi_gray)
        

            # print((time.time(),eyes,faces),file = eye_data)
            print(time.time(),file = time_data)
            print(faces,file = face_data)
            print(list(eyes),file = eye_data)
             #np.savetxt(eye_data,eyes)
            
            print(smiles,file = smile_data)
            print((time.time(),faces,list(eyes),smiles),file = tfe_data)

            #笑脸检测
            for (sx,sy,sw,sh) in smiles:
                 cv2.rectangle(img[int(y+h/2):y+h, x:x+w],(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
                 
                 
             
            #眼睛检测
            for (ex,ey,ew,eh) in eyes:
                 cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
     
        #显示原图像
       cv2.imshow('img',img)
        #按q键退出while循环
       if cv2.waitKey(30) & 0xFF == ord('q'):
             break
    
         

#释放摄像头
cap.release()
#文件关闭
time_data.close()
face_data.close()
eye_data.close()
#关闭视频输出
out.release()
#关闭所有窗口
cv2.destroyAllWindows()
