#include<iostream>

using namespace std;

int n;


void f(int x){
	if(n != 0){
		int a=1,k=0;   //k为记录 2的几次方 
		cout<<"2";
		while(a <= x){		//这里要 <= 
			a *= 2;
			k++;
		}
		a /= 2;
		k--;			//符合时 取的是最后一个不符合的k  所以k--
		
		if(k == 2 || k == 0){						//因为题目要求 1次方不需要输出（1）。
			cout<<"("<<k<<")";		
		}
		if(k >= 3){										//题目要求 求到2的 2次方往下，所以每次求出来的次方大于2
															//那就需要再细分。
			cout<<"(";
			f(k);
			cout<<")";
		}
		
		x -= a;					//同k一样，符合时 取的是最后一个不符合的  所以要减掉
		if(x){												//如果是最后一个那就结束了，不是最后一个那就 + 再递归
			cout<<"+";
			f(x);
		}
	}
}


int main(){
	cin>>n;
	f(n);
	return 0;
}
