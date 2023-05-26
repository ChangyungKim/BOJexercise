#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main() {
   int A,B;
   cin>>A>>B;
   int C;
   cin>>C;
   if(B+C>=60){
       A=A+(B+C)/60;
       B=(B+C)%60;
       if(A>=24){
           A=A-24;
       }

   }
   else{
       B=B+C;
   }
   printf("%d %d", A, B);
}
