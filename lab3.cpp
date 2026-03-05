TASK1: Without count
#include <iostream>
using namespace std;

int main() {
    int x;

    cout << "enter positive value: ";
    cin >> x;

    if (x < 1) {
        cout << "enter positive value";
        return 0;
    }

    while (x != 1) {
        cout << x << endl;

        if (x % 2 == 0) {
            x = x / 2;
        } 
        else {
            x = 3 * x + 1;
        }
    }

    cout << 1 << endl;

    return 0;
}


