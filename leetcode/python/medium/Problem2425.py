# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        r1 = 0
        r2 = 0
        if l1 % 2 == 1 and l2 % 2 == 1:
            for n in nums1:
                r1 ^= n
            for n in nums2:
                r2 ^= n
        elif l1 % 2 == 1:
            for n in nums2:
                r2 ^= n
        elif l2 % 2 == 1:
            for n in nums1:
                r1 ^= n

        return r1 ^ r2

# Problem 2425
# Tips:
# 1. XOR is commutative and associative, meaning the order of operations doesn't matter.
# 2. Any number XORed with itself results in 0.
# 3. For every even occurrence, the XOR value is 0 (from 2)
# 4. If the length of one array is even, all XOR contributions from that array cancel out.
#    If the length is odd, only the XOR of the elements of the other array matters.
# Link: https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/
if __name__ == '__main__':
    s = Solution()
    print(s.xorAllNums(nums1 = [1,2,3], nums2 = [6,5]))
