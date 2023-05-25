#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
   int a,b,c;
   cin>>a>>b>>c;
   vector<int> v;
   v.push_back(a);
   v.push_back(b);
   v.push_back(c);
   if(a==b && b==c){
       cout<<10000+(a)*1000;
   }
   else if(a!=b && b!=c &&c!=a){
       int mx=*(max_element(v.begin(), v.end()));
       cout<<mx*100;
   }
   else{
       for(int i=0;i<2;i++){
           for(int j=1;j<3;j++){
               if(v[i]==v[j]){
                   cout<<1000+v[i]*100;
                   return 0;
               }
           }

       }

   }
}
