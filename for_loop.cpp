#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
#include <bits/stdc++.h> 

int main() {
    int a;
    int b;

    // Initialize array of pointer 
    const char *numbers[9] = { "one","two","three","four","five","six","seven","eight","nine" }; 

    cin >> a;
    cin >> b;

    for (int i=a;i<=b;i++){
        if (i>=1 && i<=9){
        cout << numbers[i-1]<< endl;

    }
    }

    for (int i=a;i<=b;i++){

        if (i>9){
            if (i%2==0){
                cout<<"even\n";
            }

            else {
                cout<<"odd\n";
            }
        }

    }
    
    return 0;
} 






