// Given an array of 0’s and 1’s. Need to tell the minimum number of swaps required to take all 1’s to one side.
// Only adjacent swap is allowed.
//
// Example: 10101
// Answer is 3

#include<cstring>
#include<iostream>
using namespace std;

int main(){

 string zerone = "1010101";
 // std::cout << "Enter string: " << '\n';
 // cin>>zerone;

 int length = zerone.length();
 int zerostillnow_left=0,zerotillnow_right=0;
 int ans_left=0,ans_right=0;

for (size_t i = 0; i < length; i++) {

  //If you want to make all the one's to the left side
  if(zerone[i]=='0')
  zerostillnow_left++;
  else
   ans_left+=zerostillnow_left;

  //If you want to make all the one's to the right side
  if(zerone[length-1-i]=='0')
    zerotillnow_right++;
  else
  ans_right+=zerotillnow_right;
 }

 cout<<std::min(ans_right,ans_left)<<std::endl;

 return 0;
}
