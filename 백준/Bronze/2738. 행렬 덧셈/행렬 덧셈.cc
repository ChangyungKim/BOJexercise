#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main() {
    int N,M;
    cin>>N>>M;
    int**arr1=new int*[N];
    int**arr2=new int*[N];
    int**result=new int*[N];
    for(int i=0;i<N;i++){
        arr1[i]=new int[M];
        arr2[i]=new int[M];
        result[i]=new int[M];
    }
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++){
            cin>>arr1[i][j];
        }
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin>>arr2[i][j];
        }
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            result[i][j]=arr1[i][j]+arr2[i][j];
        }
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

}
