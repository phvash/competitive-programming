/* Count Sort using apperance array
// best used when we have a lot of numbers to sort
// but the numbers are relatively small
// eg. 100,000 numbers from the interval 0 - 20,000.
// this implementaion only sorts positive numbers
// requires you to know, maximum value in input, num of inputs
*/

# include <iostream>
# include <fstream>

using namespace std;

ifstream inputStream("data/count_sorting.in");
ofstream outputStream("data/count_sorting.out");

int main(){
    int maxEntry, inputSize;
    inputStream >> maxEntry;
    inputStream >> inputSize;


    // we need an array (i.e appearance arr) of at least size (maxEntry + 1) to hold the counts
    int apperanceArray[maxEntry + 1];

    // initialize all the entries of appearanceArray to zero
    // this is required since local arrays are randomly initialized
    for (int i=0; i <= maxEntry; i++){
        apperanceArray[i] = 0;
    }

    // read inputs and update count in appearance array

    for (int i=0; i < inputSize; i++){
        int num;
        inputStream >> num;
        apperanceArray[num] += 1;
    }

    // here is where the sorting takes place
    for (int num=0; num <= maxEntry; num++){
        int count;
        count = apperanceArray[num];
        while (count > 0) { 
            outputStream << num << " ";
            count--;
        }
    }

    return 0;

}