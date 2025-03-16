# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(m)
class Solution:
    def wordsCanBeTyped(self, string1: str, letters: list[str]) -> int:
        """
        A keyboard is only with some broken letters. All others like punctuations, digits, etc. are ok.
        :param string1:
        :param letters: the given letters are the ones that can be typed.
        :return: how many words can be typed
        """
        set_letters = set(letters)
        ans = 0
        for word in string1.split(" "):
            is_ok = True
            for c in word:
                if c.isalpha() and c.lower() not in set_letters:
                    is_ok = False
                    break
            if is_ok:
                ans += 1

        return ans

    def wordsCanBeTyped2(self, string1: str, letters: list[str]) -> int:
        l_string1 = len(string1)
        set_letters = set(letters)
        i = 0
        ans = 0
        while i < l_string1:
            if string1[i] == " ":
                i += 1
                continue

            is_ok = True
            if string1[i].isalpha():
                j = i
                while j < l_string1 and string1[j] != " ":
                    # lower() for case insensitive match
                    if string1[j].isalpha() and string1[j].lower() not in set_letters:
                        is_ok = False
                    j += 1
                if is_ok:
                    ans += 1
                i = j  # Move i to the end of the word
            else:
                if is_ok:
                    ans += 1
                i += 1
        return ans

# Problem XXX3
# Link: from Ken (Agoda)
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("Hello, this is CodeSignal!", ['e', 'i', 'h', 'l', 'o', 's'], 2),
        ("Hi, this is Chris!", ['r', 's', 't', 'c', 'h'], 0),
        ("2 + 3 = 5", [], 5)
    ]
    for string1, letters, expected in cases:
        print(" wordsCanBeTyped =============== ")
        print(s.wordsCanBeTyped(string1, letters) == expected)
        print(" wordsCanBeTyped2 =============== ")
        print(s.wordsCanBeTyped2(string1, letters) == expected)
