class Solution:
    def first_missing_positive_binary(arr):
        left, right = 0, len(arr) - 1
        # Adjust logic: expected number at index i should be arr[0] + i
        base = arr[0]
        if base > 1:
            return 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - base == mid:
                left = mid + 1
            else:
                right = mid - 1

        return base + left


if __name__ == "__main__":
    cases = [
        ([1,2,3,4,5], 6),
        ([1,2,3,4,5,6,7,8,9,10], 11),
        ([1], 2),
        ([2], 1),
        ([3], 1),
        ([1,3,4,5,6,7,8,9,10], 2),
        ([1,2,3,4,5,6,7,9,10], 8),
        ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 21),
    ]
    for case, expected in cases:
        print(Solution.first_missing_positive_binary(case) == expected)
