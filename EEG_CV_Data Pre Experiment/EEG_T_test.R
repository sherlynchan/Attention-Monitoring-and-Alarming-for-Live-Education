library('data.table');


 
N = 19
  
datalist = vector('list',N)

for(i in 1:N){  
  datalist[[i]] = fread(paste('E://大创//终期报告//Threshold_',i-1,'.txt',sep = '')); 
  datalist[[i]] = as.data.frame(datalist[[i]]);
  
}

#记录
for(i in 1:N){ 
  datalist[[i]][,7]<-0
  
  for(j in 1:3){
    pvalue = (t.test(datalist[[i]][j,1:6],datalist[[i]][j+3,1:6],'less'))$p.value;
    if(pvalue > 0.1){
      datalist[[i]][j,7] = 1;
      datalist[[i]][j+3,7] = 2;
    }
      
  }
  for(j in 7:9){
    pvalue = (t.test(datalist[[i]][j,1:6],datalist[[i]][j+3,1:6],'less'))$p.value;
    if(pvalue > 0.1){
      datalist[[i]][j,7] = 1;
      datalist[[i]][j+3,7] = 2;
    }
    
  }
}
# datalist[[13]] datalist[[19]] 含有NA的行

att_mean<-0
dis_mean<-0
for(i in 1:N){
  att_mean[i] = mean(as.matrix((datalist[[i]])[which(datalist[[i]]$V7==1),1:6]))
  dis_mean[i]= mean(as.matrix((datalist[[i]])[which(datalist[[i]]$V7==2),1:6]))
}

Threshold = (att_mean+dis_mean)/2
Mean = rbind(att_mean,dis_mean,Threshold)
write.table(Mean,"E://大创//终期报告//Sub_Threshold.txt")




