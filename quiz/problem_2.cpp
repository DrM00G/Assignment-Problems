# include <iostream>
# include <cassert>

int seqSum(int n){
  int entries[n+1];
  for(int i = 0; i<n+1;i++){
    if(i == 1 || i==0){
      entries[i]=i;
    }
    else{
      entries[i]=entries[i-1]+(2*entries[i-2]);
    };
  };
  int sum=0;
  for(int j = 0; j<=n;j++){
    sum+=entries[j];
  };
  return sum;
}

int extendedSeqSum(int k){
  int entries[10];
  for(int i = 0; i<10;i++){
    if(i == 1 || i==0){
      entries[i]=i;
    }
    else{
      entries[i]=entries[i-1]+(2*entries[i-2]);
    };
  };
  return seqSum(entries[k]);
}

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!";

    return 0;
}