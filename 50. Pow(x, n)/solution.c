
double Pow(double x, int n)
{
    if (n == 0)
        return 1;

    double t = Pow(x, n / 2);
    if (n % 2)
        return x * t * t;
    else
        return t * t;
}

double myPow(double x, int n)
{

    if (n == 0)
        return 1;
    return n < 0 ? 1.0 / Pow(x, n) : Pow(x, n);
}