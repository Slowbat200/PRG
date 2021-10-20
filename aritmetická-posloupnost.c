#include<stdio.h>
#include<stdlib.h>

int an(int a1, int d, int n)
{
    return a1 + ((n-1)*d)
}

void generuj(int a1, int d, int n)
{
    int a = a1;
    for(i = 0; i < n; i++)
    {
    printf("%d", a);
    a += 4;    
    }
}

int main(){
    generuj(2,4,5);
    return 0;
}