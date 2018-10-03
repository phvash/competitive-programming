# include <iostream>

using namespace std;

int myMatrix[3][3];


// increases the value of the every element in matrix by specified value
void addMatrix(int value) {
    for (int rowIndex=0; rowIndex<3; rowIndex++){
        for (int columnIndex=0; columnIndex<3; columnIndex++){
            myMatrix[rowIndex][columnIndex] += value;
        }
    }

}

// returns the sum of all the elements in the matrix
int sumMatrix() {
    int sum = 0;
    for (int rowIndex=0; rowIndex<3; rowIndex++){
        for (int columnIndex=0; columnIndex<3; columnIndex++){
            sum += myMatrix[rowIndex][columnIndex];
        }
    }
    return sum;
}

int main() {

    addMatrix(1);
    addMatrix(10);
    addMatrix(100);

    int sum = sumMatrix();    
    cout << sum <<'\n';
    return 0;
}