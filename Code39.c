#include <stdio.h>
#include<math.h>

int main(){
	int N;
	scanf("%d", &N);              	

	int a[N];
	for(int i=0;i<N;i++)
	{
		scanf("%d",&a[i]);
	}
	long int res=1;
	int t;
	t=pow(10,9)+7;
//	printf("%d\n",t);
	for(int i=0;i<N;i++)
	{
		res=(res*a[i])%(t);
	//	printf("%ld\t",res);
	}

	printf("%ld",res);
}


