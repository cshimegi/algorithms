class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of 1's in num1 and num2
        num1_count1, num2_count1 = num1.bit_count(), num2.bit_count()

        # Assume x since x XOR num1 is minimal
        x = num1

        # Assume machine is using 32 bit
        for i in range(32):
            # Remove the position of 1 in x because num1_count1 > num2_count1 and
            # it needs to be the same bit sets as num2 by decreasing the number of 1's
            if num1_count1 > num2_count1 and (1 << i) & num1 > 0:
                x ^= 1 << i
                num1_count1 -= 1
            # Other the other hand, it needs to add more bit sets to be the same bit set as num1
            # by increasing the number of 1's because num1_count1 < num2_count1
            if num1_count1 < num2_count1 and (1 << i) & num1 == 0:
                x ^= 1 << i
                num1_count1 += 1

        return x

# Problem 2429
# Link: https://leetcode.com/problems/minimize-xor/description/
if __name__ == '__main__':
    s = Solution()
    print(s.minimizeXor(3, 5))  # 3
    print(s.minimizeXor(1, 12))  # 3
