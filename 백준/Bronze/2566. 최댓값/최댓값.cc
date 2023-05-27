#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main() {
    int mx=0;
    int row=0;
    int col=0;
    int** arr=new int*[9];
    for(int i=0;i<9;i++){
        arr[i]=new int[9];
    }
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cin>>arr[i][j];
            if(mx<arr[i][j]){
                mx=arr[i][j];
                row=i;
                col=j;
            }
        }
    }
    printf("%d\n", mx);
    printf("%d %d", row+1, col+1);
}
