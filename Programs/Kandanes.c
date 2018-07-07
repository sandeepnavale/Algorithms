#include <stdio.h>
#define min(a,b) a<b?
int kandanes(int *a,int n);

int kandanes(int *a,int n)
{
  int sum_so_far=0,total_sum=0,min_so_far=-100;
  for(int i =0;i<n;i++)
    {
      sum_so_far += a[i];
      if (sum_so_far > total_sum)
	total_sum = sum_so_far;
      if (total_sum == 0)
	total_sum = total_sum<a[i]? 0:a[i];
    }
  return total_sum;
}
int main() {
  int t=0,n=0,a[100]={0};
  scanf("%d",&t);
  for(int i = 0; i<t && t>=1 && t<=200;i++)
    {
      printf("TC %d",i);
      scanf("%d",&n);
      for(int j = n; j<=n && n>=1 && n<=1000;j++)
      for(int k = 0;k<n;k++)
	        scanf("%d",&a[k]);

    printf("\n %d",kandanes(a,n));
    }  
  return 0;
}

