#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

	FILE *fp=fopen("output_set5.txt","w");
	if(fp == NULL)
		printf("Error in opening file");
	
	int i=0;
	float zStart=0.019608;
	for(i=1; i<=20; i++)
		fprintf(fp , "%f\n", zStart+(i*((1-zStart)/20)) );
	
	fclose(fp);
	return 0;
}

