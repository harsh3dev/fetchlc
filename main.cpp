#include <iostream>
#include <vector>
using namespace std;

int trap(vector<int>& height) {
    // Start your code here
}

// Do not change the driver code
int main() {
    int n;
    cin >> n;
    vector<int> height(n);
    for (int i = 0; i < n; i++) {
        cin >> height[i];
    }
    cout << trap(height) << endl;
    return 0;
}
