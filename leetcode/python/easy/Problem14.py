class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        l = len(strs)
        if l == 1:
            return strs[0]

        ans = ""
        for i in range(l-1):
            str_a, str_b = strs[i], strs[i+1]
            j = len(str_b) if len(str_a) > len(str_b) else len(str_a)
            temp = ""
            for k in range(j):
                if str_a[k] == str_b[k]:
                    temp += str_a[k]
                else:
                    break

            if temp == "":
                ans = ""
                break
            elif ans == "":
                ans = temp
            elif len(temp) < len(ans):
                ans = temp
        return ans

    # More concise
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        # Assume str1 is the common prefix
        prefix = strs[0]
        # Check
        for i in range(1, len(strs)):
            while prefix != "" and strs[i][:len(prefix)] != prefix:
                # Remove the last character to check again
                prefix = prefix[:len(prefix)-1]
            if prefix == "":
                return ""
        return prefix


# Problem 14
# Link: https://leetcode.com/problems/longest-common-prefix/description/
if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix2(strs = ["flower","flow","flight"]))
    print(s.longestCommonPrefix2(strs = ["dog","racecar","car"]))
    print(s.longestCommonPrefix2(strs = ["a"]))
    print(s.longestCommonPrefix2(strs = ["reflower","flow","flight"]))