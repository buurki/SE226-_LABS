QUESTION 4:

#include <iostream>
using namespace std;

double Quest3(int n) {
    if (n == 1)
        return 1;

    if (n % 2 == 0)
        return Quest3(n - 1) - 1.0 / n;
    else
        return Quest3(n - 1) + 1.0 / n;
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    cout << "Result: " << Quest3(n) << endl;

    return 0;
}
