class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> ans;
        int a = 0;
        for (auto &i : nums)
        {
            int b = 0;
            // i know, would be more efficient if we start ii at i+1
            // my C++ is too rusty to figure out how to do that with iterators
            for (auto &ii : nums)
            {
                if (i + ii == target && b != a)
                {
                    ans.push_back(a);
                    ans.push_back(b);
                    return ans;
                }
                b++;
            }
            a++;
        }
        return ans;
    }
};