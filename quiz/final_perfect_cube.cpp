# include <iostream>
# include <cassert>


int perfect_cube(int n){
    int count = 0;
    for(int i = 1; i<=n;i++){
        count=count+(i*i*i);
    }
    return count;

}


int main()
{
    std::cout << "Testing...\n";

    assert(perfect_cube(10)==3025);

    std::cout << "Success!";

}