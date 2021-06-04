# include <iostream>
# include <cassert>


int perfect_cube(int n){
    int count = 0;
    for(int i = 1; i<=n;i++){
        count=count+(i*i*i);
    }
    return count;
//   int entries[10];
//   for(int i = 0; i<10;i++){
//     if(i == 1 || i==0){
//       entries[i]=i;
//     }
//     else{
//       entries[i]=entries[i-1]+(2*entries[i-2]);
//     };
//   };
//   return seqSum(entries[k]);
}


int main()
{
    std::cout << "Testing...\n";

    assert(perfect_cube(10)==3025);
    // assert(seqSum(3)==5);
    // assert(seqSum(8)==170);

    // assert(extendedSeqSum(2)==1);
    // assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

}