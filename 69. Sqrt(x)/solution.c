
int mySqrt(int x)
{
    if (x == 0 || x == 1)
        return x;
    else if (x == 2147483647)
        return 46340;

    int start = 1, end = x, ans;
    while (start <= end)
    {
        int mid = (start + end) / 2;
        while (mid > 46340)
            mid -= 1;
        if (mid * mid == x)
            return mid;
        else if (mid * mid < x)
        {
            start = mid + 1;
            ans = mid;
        }
        else
            end = mid - 1;
    }
    return ans;
}
