#include <iostream>
#include <algorithm>

using namespace std;
int main() {
    int N;
    cin>>N;
    double*score=new double[N];
    for(int i=0;i<N;i++){
        cin>>score[i];
    }
    double result=0;
    int mx=*(max_element(score, score+N));
    for(int i=0;i<N;i++){
        score[i]=score[i]/mx*100;
    }
    for(int i=0;i<N;i++){
        result+=score[i];
    }
    cout<<result/N;

}
