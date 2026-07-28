#include <iostream>
using namespace std;
 int a = 2 ;
 void temp(){ 
                int a ;
                
                ::a += 1 ;    // able to change global variables also 
                // but we have to use :: for global variable changes 
                // if we have declared same name local variable
                cout << ::a  << endl ;
             }
int main() {
             temp() ;
             cout << a << endl ;
            
    return 0;
}