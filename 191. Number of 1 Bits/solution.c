int hammingWeight(uint32_t n)
{
    int a = 0;
    for (int i = 0; i < 32; i++)
    {
        if ((n >> i) % 2 == 1)
            a++;
        else if (n >> i < 1)
            break;
    }
    return a;
}