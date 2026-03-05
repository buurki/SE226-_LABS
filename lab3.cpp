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

TASK2:


TASK3:
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a number between 3 and 9: ";
    cin >> n;

    if (n < 3 || n > 9) {
        cout << "Invalid input";
        return 0;
    }

    for (int k = 1; k <= n; k++) {
        cout << string(k, '*') << endl;
    }

    for (int k = n - 1; k >= 1; k--) {
        cout << string(k, '*') << endl;
    }

    return 0;
}
