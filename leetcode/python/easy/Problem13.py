class Solution:
    def romanToInt(self, s: str) -> int:
        value_maps = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        l = len(s)
        i, ans = 0, 0
        while i < l:
            if i+1 < l and s[i:i+2] in value_maps:
                ans += value_maps[s[i:i+2]]
                i += 2
            else:
                ans += value_maps[s[i]]
                i += 1

        return ans



# Problem 13
# Link: https://leetcode.com/problems/roman-to-integer/description/
if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt(s = "III"))
    print(s.romanToInt(s = "LVIII"))
    print(s.romanToInt(s = "MCMXCIV")) # 1994
