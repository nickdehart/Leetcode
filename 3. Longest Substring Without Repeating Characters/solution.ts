
function lengthOfLongestSubstring(s: string): number {
    let longest :number = 0;
    let current :number = 0;
    let lookup :{ [c: string]: number }= {};

    const arr = s.split("");

    for(let i = 0; i < s.length; i++) {
        const char = arr[i];

        if(lookup.hasOwnProperty(char)) {
            if(current > longest)
                longest = current;
            i = lookup[char]+1;
            current = 0;
            lookup = {};
        } else {
            current +=1;
            lookup[char] = i;
        }
    }

    if(current > longest)
        return current;
    return longest;
};
