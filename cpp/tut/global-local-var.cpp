#include <iostream>

using namespace std;

int Aglobal[3];

int main(){
    int Alocal[3];

    cout<<Aglobal[0]<<" "<<Aglobal[1]<<" "<<Aglobal[2]<<"\n";
    cout<<Alocal[0]<<" "<<Alocal[1]<<" "<<Alocal[2]<<"\n";
    return 0;
}