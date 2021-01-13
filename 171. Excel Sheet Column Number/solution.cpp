class Solution
{
public:
    int titleToNumber(string s)
    {
        int ans = 0;
        for (int i = 0; i < s.size(); i++)
        {
            ans *= 26;
            ans += s[i] - 64;
        }
        return ans;
    }
};