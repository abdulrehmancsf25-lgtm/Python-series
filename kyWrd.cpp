// #include <iostream>
// #include<vector>
// using namespace std;

// class Animals{
//               public:
//                 virtual  void speak(){
//                  cout << "he is speaking loudly "<< endl ;
//               }
// };     
// class s_Animal:public Animals{
//             public:
//              void speak  (){
//                  cout << "he is meowing like cats " << endl ;
//              }
// };
// class t_Animal :public Animals{
//                               public:
//                               void speak(){
//                                 cout << "he is roaring like a lion " << endl ;
//                               }
// };
// void call_speak( Animals &animal){
//                      animal.speak();
// }
// int main() {
//             Animals H1;
            
            
//             s_Animal H2;
            
//             t_Animal H3 ;
                
//             call_speak(H1);
//             call_speak(H2);
//             call_speak(H3);
//         vector <Animals*> category = {new s_Animal(),new t_Animal} ;
//          for(auto*i :category)
//            i->speak();

//     return 0;
