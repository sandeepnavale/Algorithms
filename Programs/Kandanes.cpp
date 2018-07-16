#include<iostream>
using namespace std;


int kadane(int* arr,int n){
    int curr=0,tot=0;
    int m=-100;
    for(int i=0;i<n;i++){
	if(curr<0) curr=0;
	curr+=arr[i];
	tot=std::max(tot,curr);
	m=std::max(m,arr[i]);
    }
    if(tot==0) tot=m;
    return tot;
}

int main() {
    ios_base::sync_with_stdio(false);
    int n,t;
    std::cin>>t;
    while(t--){
	std::cin>>n;
	int*arr=new int[n];
	for(int i=0;i<n;i++){
	    std::cin>>arr[i];
	}
	std::cout<<kadane(arr,n);
	delete arr;
    }
}
