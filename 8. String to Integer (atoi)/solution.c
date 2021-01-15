

int myAtoi(char *s)
{
    int i = 0;
    bool negative = false;

    // ignore whitespace
    while (s[i] == ' ' && i < strlen(s))
        i++;

    // check sign
    if (i >= strlen(s))
        return 0;
    else if (s[i] == '-')
    {
        negative = true;
        i++;
    }
    else if (s[i] == '+')
        i++;

    // only get consecutive digits
    char s2[strlen(s) - i + 1];
    int k = 0;
    while (i < strlen(s) && s[i] >= 48 && s[i] <= 57)
    {
        s2[k] = s[i];
        k++;
        i++;
    }
    s2[k] = '\0';

    // convert to integer
    long ans = 0;
    for (int i = 0; i < strlen(s2); i++)
    {
        if (ans > 2147483648)
            break;
        ans = (ans * 10) + (s2[i] - 48);
    }

    if (negative)
        if (ans > 2147483648)
            return -2147483648;
        else
            return ans * -1;
    if (ans > 2147483647)
        return 2147483647;
    else
        return ans;
}