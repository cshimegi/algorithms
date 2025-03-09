# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        # O(n*log(log(n)))
        if left == right:
            return [-1, -1]

        def generate_primes(n):
            if n <= 2:
                return 0

            is_prime = [1] * n
            is_prime[0] = is_prime[1] = 0
            i = 2
            while i * i < n:
                if is_prime[i]:
                    is_prime[i * i:n:i] = [0] * (1 + (n - 1 - i * i) // i)  # n is exclusive
                i += 1 if i == 2 else 2

            return [p for p, v in enumerate(is_prime) if v and p >= left]

        primes = generate_primes(right + 1)
        total = len(primes)
        if total < 2:
            return [-1, -1]

        ans = [primes[0], primes[1]]
        diff = ans[1] - ans[0]
        k = 2
        while k < total:
            prime = primes[k]
            if prime - primes[k-1] < diff:
                ans = [primes[k-1], prime]
                diff = ans[1] - ans[0]
            k += 1

        return ans

# Problem 2523
# Link: https://leetcode.com/problems/closest-prime-numbers-in-range/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (10, 19),
        (4, 6),
    ]
    for left, right in cases:
        print(s.closestPrimes(left, right))
