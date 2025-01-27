# Questions to ask:
# 1. What is the time complexity? O(n*log(log(n)))
# 2. What is the space complexity?
class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes
        if n <= 2:
            return 0

        is_prime = [1]*n
        is_prime[0] = is_prime[1] = 0

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = 0
        return sum(is_prime)

    def countPrimes2(self, n: int) -> int:
        # Sieve of Eratosthenes; this one performs better
        if n <= 2:
            return 0

        is_prime = [1]*n
        is_prime[0] = is_prime[1] = 0

        i = 2
        while i*i < n:
            if is_prime[i]:
                is_prime[i*i:n:i] = [0]*(1+(n-1-i*i)//i) # n is exclusive
            i += 1 if i == 2 else 2

        return sum(is_prime)


# Problem 204
# Link: https://leetcode.com/problems/count-primes/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    s.countPrimes(100)