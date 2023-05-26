#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
   int N,X;
   cin>>N>>X;
   int *lst=new int[N];
   for(int i=0;i<N;i++){
       cin>>lst[i];
   }
   for(int i=0;i<N;i++){
       if(lst[i]<X){
           printf("%d ", lst[i]);
       }
   }




}
