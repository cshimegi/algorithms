# Questions to ask:
# 1. What is the time complexity? O(n*m)
# 2. What is the space complexity?
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter, defaultdict

        len_word = len(words[0])
        total_s = len(s)
        total_words = len(words)
        word_count = Counter(words)
        ans = []

        for i in range(len_word):
            start = i
            curr_window = defaultdict(int)
            match_count = 0

            for j in range(i, total_s - len_word + 1, len_word):
                word = s[j:j + len_word]
                
                if word in word_count:
                    match_count += 1
                    curr_window[word] += 1

                    while curr_window[word] > word_count[word]:
                        curr_window[s[start:start + len_word]] -= 1
                        start += len_word
                        match_count -= 1

                    if match_count == total_words:
                        ans.append(start)
                else:
                    start = j + len_word
                    curr_window.clear()
                    match_count = 0
        
        return ans


# Problem 30
# Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        # ("barfoothefoobarman", ["foo", "bar"]),
        # ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
        # ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
        # ("barfoofoobarthefoobarman", ["bar", "foo", "the", "foo"]),
        ("bcabbcaabbccacacbabccacaababcbb", ["c", "b", "a", "c", "a", "a", "a", "b", "c"]),
        # ("catbatbatcat", ["cat", "bat", "bat"]),
    ]

    for string, words in cases:
        print(s.findSubstring(string, words))
        print(s.findSubstring2(string, words))
