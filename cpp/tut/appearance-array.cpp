# include <iostream>
# include <fstream>

using namespace std;

ifstream inputFile("appearance-array.in");
ofstream outputFile("appearance-array.out");

int numCountArray[11];

// a
// int updateNumberCount(int num){

// }


// a program that
int main(){
    int lengthOfInput, num;
    inputFile >> lengthOfInput;
    
    for (int count=0; count <lengthOfInput; count++){
        inputFile >> num;
        numCountArray[num] += 1;
    }

    for (int i=0; i<=11; i++){
        outputFile << i << ": " << numCountArray[i] <<"\n";
    }
    
    return 0;
}