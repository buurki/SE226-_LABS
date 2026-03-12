#include <iostream>
using namespace std;
void swapValues(int *p1, int *p2) {
    int temp = *p1;
    *p1= *p2;
    *p2= temp;
}


void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i);
        if (i < size - 1) {
            cout << " ";
        }
    }
}
int findSum(int *arr, int size){
    int sum = 0; 
    for(int i = 0; i < size; i++){
        sum += *(arr + i);
    }
    return sum;
}
void shiftRight(int* arr, int size) {
    if (size <= 1) {
        return;
    }

    int last = *(arr + size - 1);
    for (int i = size - 1; i > 0; i--) {
        *(arr + i) = *(arr + i - 1);
    }
    *arr = last;
}

int* createArray(int size){
    int* arr = new int[size];
    for (int i = 0; i < size; i++) {
        cin >> *(arr + i);
    }
    return arr;
}
void deleteArray(int* arr){
    delete arr;

}

int main() {
    int size;

    cout << "Enter array size: ";
    cin >> size;

    cout << "Enter " << size << " numbers: ";
    int* arr = createArray(size);

    cout << "Array: ";
    printArray(arr, size);
    cout << endl;

    cout << "Sum: " << findSum(arr, size) << endl;

    shiftRight(arr, size);
    cout << "After shiftRight: ";
    printArray(arr, size);
    cout << endl;

    swapValues(&arr[0], &arr[1]);
    cout << "After swap first two: ";
    printArray(arr, size);
    cout << endl;

    deleteArray(arr);

    return 0;
}
