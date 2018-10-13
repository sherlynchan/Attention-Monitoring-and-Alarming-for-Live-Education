#include <iostream>
#include <fstream>
#include "Queue.cpp"

using namespace std;
int main()
{
    int change(char x,char y);
    int change1(char t);
    ifstream infile;
    ofstream outfile;
    outfile.open("1023E_delete.txt",ios::out);
    infile.open("1023E.txt",ios::in);
    if(!infile)
    {
        cout<<"open infile fail"<<endl;
	    exit(1);
	}
    if(!outfile)
	{
        cout<<"open outfile fail"<<endl;
	    exit(1);
    }
    
    char time[11];
    char a;
    Queue<char>timetest;
    
    if(!infile.eof()) infile.get(time,12); //最开始如果有时间就要加，没有则不能加 
    //outfile<<time<<endl;
    for(int i=0;i<10;i++)
    cout<<time[i];
    cout<<endl;
    
	while(!infile.eof())
    {
	    a=infile.get();
	    //cout<<a<<endl;
	    
		if(timetest.Full()) outfile<<timetest.Out();
		
		if(a==',') timetest.Delete_all();
		else timetest.In(a);
	}
	
    infile.close();
    outfile.close();
    return 0;
}


int s2t(char t)
{
    int t1;
    if(t>='A'&&t<='Z')
        t1=int(t-'A')+10;
    else 
	    t1=int(t-'0');
    return t1;
}
int change(char x,char y)
{
    int z;
    z=s2t(x)*16+s2t(y);
    return z;
}
