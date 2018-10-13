#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int change(char x,char y);
    int change1(char t);
    ifstream infile;
    ofstream outfile;
    outfile.open("1023E_result.txt",ios::out);
    infile.open("1023E_delete.txt",ios::in);
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
    char d1[17];
    char d2[57];
    int count=0,att,med;
    char a1,a2,b1,b2;
    while(!infile.eof())
    {
	    infile.get(d1,17);
        if(d1[4]=='2')
            {
                infile.get(d2,57);  
                att=0,med=0;
                a1=d2[48],a2=d2[49],b1=d2[52],b2=d2[53];
                att=change(a1,a2);
                med=change(b1,b2);
                cout<<"attention:"<<att<<" "<<"meditation:"<<med<<endl;
                //outfile<<d1<<d2<<"\n"<<"attention:"<<att<<"   "<<"meditation:"<<med<<endl;
                outfile<<att<<"   "<<med<<endl;
			}
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
