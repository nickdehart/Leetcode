class Solution
{
public:
    string convertToTitle(int n)
    {
        char ans[10];
        int i = 0;

        while (n > 0)
        {
            int r = n % 26;
            if (r == 0)
            {
                ans[i++] = 'Z';
                n = (n / 26) - 1;
            }
            else
            {
                ans[i++] = (r - 1) + 65;
                n = n / 26;
            }
        }
        ans[i] = '\0';
        reverse(ans, ans + strlen(ans));
        return ans;
    }
};