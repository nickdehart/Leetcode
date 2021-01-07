class Solution
{
public:
    uint32_t reverseBits(uint32_t n)
    {
        unsigned int a = 0;
        for (int i = 0; i < 32; i++)
        {
            a = (a << 1) | ((n << 31 - i) >> 31);
        }
        return a;
    }
};