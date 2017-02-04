#include <iostream>
using namespace std;

struct abc{
  int x;
  abc(int x, int z){
    this->x = x;
  }

};

class a{
  virtual void foo(){
  }
};

class b : a{
  void foo(){
    cout << "Bar" << endl; 
  }
};

int main(){
  a *aptr = new b();
  b bobj = *a;

}
