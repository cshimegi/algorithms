class Solution:
    # Questions to ask:
    # 1. What is the time complexity? O(n)
    # 2. What is the space complexity?
    #
    # graph = [
    #     [1,1,0],
    #     [0,1,0],
    #     [1,1,1]
    # ]
    #
    # def knows(a, b, graph=graph):
    #     return graph[a][b]
    #
    def fourCelebrity(self, n: int) -> int:
        # Step 1: Assume the first person is celebrity
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):  # If candidate knows i, candidate cannot be celebrity
                candidate = i  # i might be celebrity

        # Step 2: Validate the candidate
        for i in range(n):
            if i != candidate:
                # Candidate should not know anyone else, and should be known by everyone
                if knows(candidate, i) or not knows(i, candidate):
                    return -1  # No celebrity

        return candidate


# Problem 277
# Link: https://leetcode.com/problems/find-the-celebrity/description/
# https://memorylimitexceeded.gitlab.io/leetcode/problems/0277-find-the-celebrity.html
if __name__ == '__main__':
    s = Solution()
    cases = [4,7,5]
    for case in cases:
        print(s.fourCelebrity(case))

