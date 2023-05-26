#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
    int *lst=new int[31]{0};
    lst[0]=1;
    for(int i=0;i<28;i++){
        int s;
        cin>>s;
        lst[s]=1;
    }
    for(int i=1;i<31;i++){
        if(lst[i]!=1){
            printf("%d\n", i);
        }
    }


}
