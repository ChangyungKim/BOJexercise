#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
   int A,B;
   cin>>A>>B;
   if(A==0){
       if(B>=45){
           B=B-45;
       }
       else{
           A=23;
           B=B-45+60;
       }
   }
   else{
       if(B>=45){
           B=B-45;
       }
       else{
           A=A-1;
           B=B-45+60;
       }
   }
   printf("%d %d", A,B);
}
