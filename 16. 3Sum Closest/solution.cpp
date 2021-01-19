class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        int ans = 2000000000;
        for (int i = 0; i < nums.size() - 2; i++)
        {
            for (int ii = i + 1; ii < nums.size() - 1; ii++)
            {
                for (int iii = ii + 1; iii < nums.size(); iii++)
                {
                    int t = nums[i] + nums[ii] + nums[iii];
                    if (abs(t - target) < (abs(ans - target)))
                    {
                        ans = t;
                    }
                }
            }
        }
        return ans;
    }
};