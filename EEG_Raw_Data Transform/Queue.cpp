#include "Queue.h"
#include<iostream>

using namespace std;
template<class DataType>
Queue<DataType>::Queue()
{
      first=0;
	  end=0;                        
}

template<class DataType>
void Queue<DataType>::In(DataType x)
{
      if(first==(end+1)%QueueSize) throw"…œ“Á";
      data[end]=x; 
	  end=(end+1)%QueueSize;
}
       
template<class DataType>       
DataType Queue<DataType>::Out()
{
      DataType x;
      if(first==end) throw"œ¬“Á";
      x=data[first];
      first=(first+1)%QueueSize;
      return x;
}    
                  
       
template<class DataType>       
int Queue<DataType>::Empty()
{
    if(first==end) return 1;
    else return 0;
}

template<class DataType>       
int Queue<DataType>::Full()
{
    if(first==(end+1)%QueueSize) return 1;
    else return 0;
}

template<class DataType>       
void Queue<DataType>::display()
{
    cout<<first<<"   "<<end<<endl;
    int i=first+1;
    cout<<data[first]<<"  ";
	while(1)
	{
		if(i==end%QueueSize) break;
		else cout<<i<<":"<<data[i]<<"  ";
		i=(i+1)%QueueSize;
	}
	
}

template<class DataType>       
void Queue<DataType>::Delete_all()
{
    first=end=0;
}
