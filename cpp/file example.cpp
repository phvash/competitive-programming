#include <iostream>
#include <fstream>

using namespace std;

ifstream inputFile("data.in");
ofstream outputFile("data.out");


int main (void)
{   int firstNum, secondNum, sum;

    inputFile >> firstNum >> secondNum;
    sum = firstNum + secondNum;
    outputFile << sum;
 
    return 0; 
}