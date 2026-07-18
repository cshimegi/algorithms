f"""
Given an array of number strings representing the intercepted codes 
and a number string representing the target access code.
Count all pairs of intercepted codes that can be concatenated to form the target access code.
As long as the indexes of pairs are not the same, the pair is unique. For example, (i, j) != (j, i).


intercepted_codes = ["1", "2", "12", "121", "12"]
target_access_code = "1212" -> "1" + "212" or "12" + "12"

output = 3
"""

from collections import Counter

def count_pairs(codes, target):
    freq = Counter(codes)
    count = 0

    for code in codes:
        if target.startswith(code):
            suffix = target[len(code):]

            if suffix in freq:
                count += freq[suffix]

                if suffix == code:
                    count -= 1

    return count


if __name__ == "__main__":
    intercepted_codes = ["1", "2", "12", "121", "12"]
    target_access_code = "1212"
    print(count_pairs(intercepted_codes, target_access_code))
