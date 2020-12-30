#include <stdio.h>

int main(){
	int N;
	scanf("%d", &N);              	

	int X,Y;
	scanf("%d", &X); 

	for(int i=0;i<N;i++)
	{
		scanf("%d", &Y);

		if(Y<X)
		{
			printf("NO\n");
		}           	
		else
		{
			printf("YES\n");
		}
	
	}             	
	
	    
}

