#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
    int N;
    cin>>N;
    vector<int> vc;
    for(int i=0;i<N;i++){
        int s;
        cin>>s;
        vc.push_back(s);
    }
    int mx=*(max_element(vc.begin(), vc.end()));
    int min=*(min_element(vc.begin(), vc.end()));
    printf("%d %d", min, mx);


}
