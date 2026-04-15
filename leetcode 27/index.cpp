#include<iostream>
using namespace std;


int lessval(int x, int y){
    if(x < y){
        return x;
    }else{
        return y;
    }
}
class animal{
 public:
    string name = "fucking dog";
};
class blackdog : public animal{
    public:
    string legs = "black";
};
int main(){
    cout << "hello world" << endl;
    int val = lessval(3,65);
    cout << val;
    blackdog x;
    cout << x.name;
}