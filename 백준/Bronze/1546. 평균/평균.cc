#include <iostream>

using namespace std;

int main()
{
    int N;
    cin>>N;
    int A[N];
    double sum=0;
    for(int i=0;i<N;i++){
        cin>>A[i];
    }
    int max=0;
    for(int i=0;i<N;i++){
        if(max<A[i]){
            max=A[i];
        }
        sum+=A[i];
    }
    double avg=sum*100/max/N;
    cout<<avg;
}