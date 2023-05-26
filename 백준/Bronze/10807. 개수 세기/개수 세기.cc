#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
   int N;
   cin>>N;
   vector<int> vc;
   string str;
   for(int i=0;i<N;i++){
       int s;
       cin>>s;
       vc.push_back(s);
   }
   int v;
   cin>>v;
   int num=0;
   for(int i=0;i<N;i++){
       if(vc[i]==v){
           num++;
       }
   }
   cout<<num;



}
