#include<stdio.h>
#include<math.h>
double f(double x,int n)
{
    double y;
    if(n == 1)
    {
        y = sqrt(n + x);
    }
    else
        y = sqrt(n + f(x,n - 1));
    return y;
}
int main()
{
    double x;
    int n;
    double y;
    scanf("%lf%d",&x,&n);
    y = f(x,n);
    printf("%.2lf\n",y);
    return 0;
}
