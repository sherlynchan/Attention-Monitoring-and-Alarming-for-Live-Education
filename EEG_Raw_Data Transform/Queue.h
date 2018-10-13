#ifndef Queue_H
#define Queue_H

const int QueueSize=12;  //����һ��λ�����ж϶����Ƿ������� 

template<class DataType>
class Queue
{
public:
       Queue();
       ~Queue(){}
       void In(DataType x);
       DataType Out();
       int Empty();
       int Full();
       void display() ;
       void Delete_all();
private:
        DataType data[QueueSize];
        int first,end;
};

# endif
