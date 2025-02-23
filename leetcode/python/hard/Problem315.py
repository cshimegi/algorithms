# Questions to ask:
# 1. What is the time complexity? O(n*log(n)) ?
# 2. What is the space complexity?
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        from sortedcontainers import SortedList

        sorted_list = SortedList()
        ans = []

        # Traverse from right to left
        for num in reversed(nums):
            # Count elements smaller than `num` using binary search
            count = sorted_list.bisect_left(num)
            ans.append(count)
            # Insert `num` into sorted order
            sorted_list.add(num)

        return ans[::-1]
    
    def countSmaller2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n  # Stores count of smaller elements for each index
        indices = list(range(n))  # Track original indices

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)   # Sort left half
            merge_sort(mid + 1, right)  # Sort right half
            merge(left, mid, right)  # Merge while counting smaller elements

        def merge(left, mid, right):
            temp = []
            i, j = left, mid + 1
            right_count = 0  # Count of smaller elements on the right

            while i <= mid and j <= right:
                if nums[indices[j]] < nums[indices[i]]:
                    temp.append(indices[j])
                    right_count += 1  # Count smaller elements
                    j += 1
                else:
                    temp.append(indices[i])
                    ans[indices[i]] += right_count  # Update count
                    i += 1

            while i <= mid:
                temp.append(indices[i])
                ans[indices[i]] += right_count  # Remaining left elements get the count
                i += 1

            while j <= right:
                temp.append(indices[j])
                j += 1

            indices[left:right + 1] = temp  # Copy back sorted indices

        merge_sort(0, n - 1)
        return ans


# Problem 315
# Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [5,2,6,1],
        [-1],
        [-1,-1]
    ]
    for nums in cases:
        print(s.countSmaller(nums))

