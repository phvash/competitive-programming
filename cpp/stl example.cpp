#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;


int main(){

    int a=10, b=20;

    cout << max(a, b) <<endl;

    swap(a, b);

    double cubeRoot;
    int num = 2;
    cubeRoot = pow((double)(num), 1.0/3);

    cout << fixed << setprecision(10) << cubeRoot <<endl;

    return 0;
}
