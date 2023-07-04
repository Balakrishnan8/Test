lst = ["abcsadf","abcrign","abcnkdnv","abscpwoejmc"]

s = sorted(lst)
first = s[0]
last = s[-1]
ans = ""

for i in range(min(len(first),len(last))):
    print(i)
    if first[i] != last[i]:
        break
    ans += first[i]

print(ans)
