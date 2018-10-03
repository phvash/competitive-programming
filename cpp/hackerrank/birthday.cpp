#include <iostream>
#include <fstream>

using namespace std;

ifstream inputFile("birthday.in"); 
ofstream outputFile("birthday.out");

int main(){
    int age, candleHeight, max=0, maxCount=0;
    inputFile >> age;
    for (int i=0; i<age; i++){
        inputFile >> candleHeight;
        if (candleHeight > max){
            max = candleHeight;
            maxCount = 1;
        } else if (candleHeight == max){
            maxCount++;
        }
    }
    outputFile << maxCount;
    return 0;
}