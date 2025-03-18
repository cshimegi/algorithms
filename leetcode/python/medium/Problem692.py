# Questions to ask:
# 1. What is the time complexity? O(n*log(k)) k is the number of unique words
# 2. What is the space complexity? O(n)
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # O(n*log(n))
        from collections import Counter
        cnt = Counter(words)
        sortedCnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
        return [x[0] for x in sortedCnt[:k]]

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        # O(n+k*log(n))
        import heapq
        from collections import Counter
        count = Counter(words)  # Count word frequencies
        # Use heapq to extract top k elements based on (-freq, word) sorting
        return [word for word, freq in heapq.nsmallest(k, count.items(), key=lambda x: (-x[1], x[0]))]

    def topKFrequent3(self, words: List[str], k: int) -> List[str]:
        # O(k*log(n))
        from collections import Counter
        import heapq
        cnt = Counter(words)
        heap = [(-count, word) for word, count in cnt.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]



# Problem 692
# Link: https://leetcode.com/problems/top-k-frequent-words/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (
            ["i", "love", "leetcode", "i", "love", "coding"],
            2
        ),
        (
            ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
            4
        ),
        (
            ["vbimix", "ztj", "ztj", "vbimix", "zgoedv", "itnsxvvevu", "bftirwsc", "nlv", "ithxcskb", "walxnr", "amkjox",
         "ehzbw", "ithxcskb", "bftirwsc", "amkjox", "vbimix", "ztj", "amkjox", "itnsxvvevu", "ithxcskb", "oveunzoevl",
         "bdqinoduvu", "tfbpcjj", "itnsxvvevu", "vbimix", "tfbpcjj", "rllqmb", "iwj", "iwj", "ithxcskb", "ehzbw",
         "ehzbw", "bdqinoduvu", "vbimix", "ithxcskb", "ithxcskb", "ehzbw", "iwj", "bdqinoduvu", "nlv", "tfbpcjj", "nlv",
         "ehzbw", "ztj", "ztj", "tfbpcjj", "oveunzoevl", "itnsxvvevu", "amkjox", "vbimix", "itnsxvvevu", "ehzbw", "iwj",
         "rllqmb", "itnsxvvevu", "ehzbw", "iwj", "tfbpcjj", "amkjox", "vbimix", "itnsxvvevu", "amkjox", "nlv",
         "tfbpcjj", "nlv", "ztj", "iwj", "bftirwsc", "bdqinoduvu", "zgoedv", "ithxcskb", "itnsxvvevu", "vbimix",
         "walxnr", "amkjox", "bftirwsc", "vbimix", "itnsxvvevu", "tfbpcjj", "bdqinoduvu", "ithxcskb", "ithxcskb", "ztj",
         "bftirwsc", "iwj", "bftirwsc", "tfbpcjj", "ehzbw", "ehzbw", "amkjox", "ztj", "itnsxvvevu", "zgoedv", "nlv"],
            14
        ),
        (
            ["rfztgq", "vinxobozm", "csemdxcokc", "kuegnfkg", "jtboohkil", "znbxy", "cdyxo", "pvwjlopest", "ttjas",
             "jtboohkil", "zzgu", "inpmjnq", "crbiax", "uazcty", "noabilwk", "ycjekaxsa", "jemuhohn", "ycjekaxsa",
             "rjyzxiw", "mak", "bmrdpuoarp", "fgd", "bmrdpuoarp", "ttjas", "zycjtviif", "tqturfkvoe", "znbxy", "znbxy",
             "ttjas", "afsastr", "gjxsl", "bvncwzzc", "jemuhohn", "numj", "bbqwkhqn", "znbxy", "vvlcpgbwmk", "pvwjlopest",
             "ycjekaxsa", "jtboohkil", "numj", "mak", "rfztgq", "dlw", "numj", "mak", "pvwjlopest", "qagju", "jemuhohn",
             "fgd", "bbqwkhqn", "mak", "cdyxo", "uazcty", "dwe", "jemuhohn", "csemdxcokc", "ldhy", "zycjtviif", "pzblgf",
             "knzp", "bbqwkhqn", "izxlibp", "crbiax", "bbqwkhqn", "wsgpo", "rfztgq", "bmrdpuoarp", "znbxy", "inpmjnq",
             "uazcty", "izxlibp", "jgra", "jtboohkil", "khftkj", "jemuhohn", "exxwu", "qupkzsyb", "ylezdikd", "ttjas",
             "vinxobozm", "dwe", "cdyxo", "pvwjlopest", "bvncwzzc", "ycjekaxsa", "khftkj", "ylezdikd", "khftkj", "izxlibp", "qagju", "inpmjnq", "rjyzxiw", "ylezdikd", "noabilwk", "mak", "ylezdikd", "noabilwk", "znbxy", "uazcty", "csemdxcokc", "pzblgf", "noabilwk", "fgd", "ldhy", "ldhy", "knzp", "gjxsl", "ylezdikd", "exxwu", "ldhy", "ttjas", "gvtmh", "knzp", "ylezdikd", "zycjtviif", "zycjtviif", "bmrdpuoarp", "ycjekaxsa", "fgd", "ycjekaxsa", "cdyxo", "pvwjlopest", "uazcty", "zycjtviif", "ttjas", "vinxobozm", "ttjas", "pzblgf", "rfztgq", "tqturfkvoe", "ldhy", "zycjtviif", "dwe", "ldhy", "vkbl", "ycjekaxsa", "jtboohkil", "qagju", "bmrdpuoarp", "exxwu", "gvtmh", "dlw", "jtboohkil", "fgd", "qagju", "gvtmh", "inpmjnq", "lmd", "khftkj", "gvtmh", "zzgu", "ylezdikd", "cdyxo", "pvwjlopest", "khftkj", "ycjekaxsa", "qagju", "noabilwk", "knzp", "numj", "ycjekaxsa", "uazcty", "numj", "ldhy", "khftkj", "vkbl", "knzp", "bmrdpuoarp", "ycjekaxsa", "dlw", "dwe", "fgd", "afsastr", "inpmjnq", "pzblgf", "rfztgq", "jtboohkil", "khftkj", "vvlcpgbwmk", "jgra", "cdyxo", "noabilwk", "dlw", "rjyzxiw", "bvncwzzc", "numj", "ylezdikd", "jemuhohn", "exxwu", "afsastr", "bvncwzzc", "ldhy", "wsgpo", "dwe", "kuegnfkg", "jemuhohn", "jemuhohn", "cdyxo", "fgd", "vvlcpgbwmk", "jgra", "numj", "vkbl", "inpmjnq", "mak", "jtboohkil", "jemuhohn", "fgd", "afsastr", "vinxobozm", "noabilwk", "numj", "ylezdikd", "fgd", "zycjtviif", "znbxy", "znbxy", "vinxobozm", "ttjas", "csemdxcokc", "tqturfkvoe", "khftkj", "mak", "bbqwkhqn", "znbxy", "mak", "zycjtviif", "jgra", "izxlibp", "dwe", "znbxy", "noabilwk", "jtboohkil", "vinxobozm", "kuegnfkg", "vvlcpgbwmk", "uazcty", "pzblgf", "inpmjnq", "cdyxo", "kuegnfkg"],
        26),
        (["rfztgq", "vinxobozm", "csemdxcokc", "kuegnfkg", "jtboohkil", "znbxy", "cdyxo", "pvwjlopest", "ttjas",
         "jtboohkil", "zzgu", "inpmjnq", "crbiax", "uazcty", "noabilwk", "ycjekaxsa", "jemuhohn", "ycjekaxsa",
         "rjyzxiw", "mak", "bmrdpuoarp", "fgd", "bmrdpuoarp", "ttjas", "zycjtviif", "tqturfkvoe", "znbxy", "znbxy",
         "ttjas", "afsastr", "gjxsl", "bvncwzzc", "jemuhohn", "numj", "bbqwkhqn", "znbxy", "vvlcpgbwmk", "pvwjlopest",
         "ycjekaxsa", "jtboohkil", "numj", "mak", "rfztgq", "dlw", "numj", "mak", "pvwjlopest", "qagju", "jemuhohn",
         "fgd", "bbqwkhqn", "mak", "cdyxo", "uazcty", "dwe", "jemuhohn", "csemdxcokc", "ldhy", "zycjtviif", "pzblgf",
         "knzp", "bbqwkhqn", "izxlibp", "crbiax", "bbqwkhqn", "wsgpo", "rfztgq", "bmrdpuoarp", "znbxy", "inpmjnq",
         "uazcty", "izxlibp", "jgra", "jtboohkil", "khftkj", "jemuhohn", "exxwu", "qupkzsyb", "ylezdikd", "ttjas",
         "vinxobozm", "dwe", "cdyxo", "pvwjlopest", "bvncwzzc", "ycjekaxsa", "khftkj", "ylezdikd", "khftkj", "izxlibp",
         "qagju", "inpmjnq", "rjyzxiw", "ylezdikd", "noabilwk", "mak", "ylezdikd", "noabilwk", "znbxy", "uazcty",
         "csemdxcokc", "pzblgf", "noabilwk", "fgd", "ldhy", "ldhy", "knzp", "gjxsl", "ylezdikd", "exxwu", "ldhy",
         "ttjas", "gvtmh", "knzp", "ylezdikd", "zycjtviif", "zycjtviif", "bmrdpuoarp", "ycjekaxsa", "fgd", "ycjekaxsa",
         "cdyxo", "pvwjlopest", "uazcty", "zycjtviif", "ttjas", "vinxobozm", "ttjas", "pzblgf", "rfztgq", "tqturfkvoe",
         "ldhy", "zycjtviif", "dwe", "ldhy", "vkbl", "ycjekaxsa", "jtboohkil", "qagju", "bmrdpuoarp", "exxwu", "gvtmh",
         "dlw", "jtboohkil", "fgd", "qagju", "gvtmh", "inpmjnq", "lmd", "khftkj", "gvtmh", "zzgu", "ylezdikd", "cdyxo",
         "pvwjlopest", "khftkj", "ycjekaxsa", "qagju", "noabilwk", "knzp", "numj", "ycjekaxsa", "uazcty", "numj",
         "ldhy", "khftkj", "vkbl", "knzp", "bmrdpuoarp", "ycjekaxsa", "dlw", "dwe", "fgd", "afsastr", "inpmjnq",
         "pzblgf", "rfztgq", "jtboohkil", "khftkj", "vvlcpgbwmk", "jgra", "cdyxo", "noabilwk", "dlw", "rjyzxiw",
         "bvncwzzc", "numj", "ylezdikd", "jemuhohn", "exxwu", "afsastr", "bvncwzzc", "ldhy", "wsgpo", "dwe", "kuegnfkg",
         "jemuhohn", "jemuhohn", "cdyxo", "fgd", "vvlcpgbwmk", "jgra", "numj", "vkbl", "inpmjnq", "mak", "jtboohkil",
         "jemuhohn", "fgd", "afsastr", "vinxobozm", "noabilwk", "numj", "ylezdikd", "fgd", "zycjtviif", "znbxy",
         "znbxy", "vinxobozm", "ttjas", "csemdxcokc", "tqturfkvoe", "khftkj", "mak", "bbqwkhqn", "znbxy", "mak",
         "zycjtviif", "jgra", "izxlibp", "dwe", "znbxy", "noabilwk", "jtboohkil", "vinxobozm", "kuegnfkg", "vvlcpgbwmk",
         "uazcty", "pzblgf", "inpmjnq", "cdyxo", "kuegnfkg"],
        26)
    ]

    for words, k in cases:
        print(s.topKFrequent2(words, k))