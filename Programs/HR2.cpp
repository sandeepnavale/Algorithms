// https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
// // Array

#include <iostream>
#include <vector>
using namespace std;

#if 0
long arrayManipulation(int n, vector<vector<int>> queries);

long arrayManipulation(int n, vector<vector<int>> q) {

  vector<int> a(n + 1, 0);
  int sum = 0;


  for (int qi = 0; qi < q.size(); qi++) {
    if ((q[qi][0] > q[qi][1]) || (q[qi][1] > n)) return 0;

    cout << "for row " << q[qi][0] << " Col " << q[qi][1] << " Val " << q[qi][2]
         << "\n";

    for (int ri = q[qi][0]; ri <= q[qi][1]; ri++) {
      cout << "adding " << q[qi][2] << " to " << a[ri] << "\n";
      a[ri] += q[qi][2];
      // cout << a[ri] << " ";

      sum = std::max(sum, a[ri]);
    }
  }
  return sum;
}

int main() {
  int n=10;

  std::vector<std::vector<int>> queries{
      {2, 6, 8}, {3, 5, 7}, {1, 8, 1}, {5, 9, 15}};

  cout << arrayManipulation(n, queries);
  return 0;

}

#else


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    long int N,K,p,q,sum,i,j,max=0,x=0;

    cin>>N>>K;
    long int *a=new long int[N+1]();

    for(i=0;i<K;i++)
    {
        cin>>p>>q>>sum;
        a[p]+=sum;
        if((q+1)<=N) a[q+1]-=sum;
    }

    for(i=1;i<=N;i++)
    {
       x=x+a[i];
       if(max<x) max=x;

    }

    cout<<max;
    return 0;
}

#endif
