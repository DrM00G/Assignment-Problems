# include <iostream>
# include <cassert>



int calcIndex(int n){
  int first_num=0;
  int second_num=1;
  int placeholder = 0;
  int index = 0;
  while (first_num <= n){
    placeholder = second_num;
    second_num = second_num+first_num;
    first_num=placeholder;
    index++;
  }
  return index;
}

int main()
{
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}