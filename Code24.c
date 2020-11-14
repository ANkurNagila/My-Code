#include <stdio.h>

int main(){
	int num;
	scanf("%d", &num);  

	int a,b;            	
	
	
	while(num>0)
	{
		scanf("%d%d",&a,&b);

		if(b%a==0)
		{
			printf("Yes\n");
		}
		else
		{
			printf("No\n");
		}
		num--;
	}
}


