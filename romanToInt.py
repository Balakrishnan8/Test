"""
m = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

s = input("->>>")
ans = 0
for i in range(len(s)):
    print(i,s[i])
    if i<len(s)-1 and m[s[i]]<m[s[i+1]]:
        ans -= m[s[i]]
    else:
        ans += m[s[i]]

print(ans)
"""

def romanToInt(s: str) -> int:
    roman_dict = {'I' :1,'V' :5,'X' :10,'L' :50,'C' :100,'D' :500,'M' :1000}
    s = s.replace("IV", "IIII").replace("IX", "IIIIIIIII")
    s = s.replace("XL", "XXXX").replace("XC", "XXXXXXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "CCCCCCCCC")
    res = 0
    for char in s:
        print(char)
        res += roman_dict[char]

    return res
