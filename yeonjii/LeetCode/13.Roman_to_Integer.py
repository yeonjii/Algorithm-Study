class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        i = 0
        while i < len(s):
            if i<len(s)-1 and s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                num += romans[s[i+1]]-romans[s[i]]
                i += 2
            elif i<len(s)-1 and s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                num += romans[s[i+1]]-romans[s[i]]
                i += 2
            elif i<len(s)-1 and s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                num += romans[s[i+1]]-romans[s[i]]
                i += 2
            else:
                num += romans[s[i]]
                i += 1
        return num


# Runtime: 68 ms, faster than 77.80% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14 MB, less than 30.65% of Python3 online submissions for Roman to Integer.