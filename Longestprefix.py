class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        end = 0
        count = 1
        for i in range(len(strs)-1):
            count = 1
            mins = len(strs[i]) if len(strs[i])<len(strs[i+1]) else len(strs[i+1])
            for j in range(mins):
                print(i,j,strs[i][j],strs[i+1][j])
                if  strs[i][j] == strs[i+1][j]:
                    end = j
                    count += 1
                    continue
                else:
                    break
        print(count)
        if count==len(strs):
            return strs[0][:end+1]
        else:
            return ""
s = Solution()
a=s.longestCommonPrefix(["reflower","flow","flight"])
print(a)

"""

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

"""
