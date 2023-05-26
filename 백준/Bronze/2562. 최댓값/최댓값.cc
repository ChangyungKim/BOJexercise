#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
    vector<int> vc;
    for(int i=0;i<9;i++){
        int n;
        cin>>n;
        vc.push_back(n);
    }
    int mx=*(max_element(vc.begin(), vc.end()));
    for(int i=0;i<9;i++){
        if(mx==vc[i]){
            printf("%d\n", mx);
            printf("%d\n",i+1);
        }
    }


}
