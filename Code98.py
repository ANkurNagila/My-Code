#include <stdio.h>

int main(){
	int N;
	scanf("%d",&N);

	int T;

	while(N>0)
	{
		scanf("%d",&T);

		for(int i=1;i<=T;i++)
		{
			for(int j=1;j<=2*T;j++)
			{
				if(j<=i||j>2*T-i)
				{
					printf("*");
				}
				else
				{
					printf("#");
				}
			}
			printf("\n");
		}
		printf("\n");

		N--;

	}    
}


