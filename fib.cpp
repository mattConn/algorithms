#include <iostream>
#include <iomanip>
#include <ctime>

#define WIDTH 15

using namespace std;

// non-recursive fibonacci
int fib(int n);

// recursive fibonacci
int fibR(int n);

int main()
{
	int fibTime, fibRTime;
	fibTime = fibRTime = 0;

	int val = 0;

	// table header
	cout << "int" << setw(WIDTH) << "fibR" << setw(WIDTH) << "fib" << setw(WIDTH) << "val" << endl;

	for(int i=1; i <= 46; i++)
	{
		// fib time
		time_t now = time(NULL);
		val = fib(i);
		fibTime = time(NULL) - now;

		// fibR time
		now = time(NULL);
		fibR(i);
		fibRTime = time(NULL) - now;


		cout << i << setw(WIDTH) << fibRTime << setw(WIDTH) << fibTime << setw(WIDTH) << val << endl;
	}

	return 0;
}

int fib(int n)
{
	if(n == 0 || n == 1)
		return n;

	if(n == 2)
		return 1;

	int f1, f2;
    f1 = f2 = 1;

    int result = 0;

    for(int i = 3; i <= n; i++)
	{
        result = f1 + f2;
        f1 = f2;
        f2 = result;
	}

    return result;

}

int fibR(int n)
{
	if(n == 0 || n == 1)
		return n;

	if(n == 2)
		return 1;

	return fibR(n-1) + fibR(n-2);
}
