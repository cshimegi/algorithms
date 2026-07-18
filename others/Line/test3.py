from collections import Counter

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

s_freq = Counter(s)
t_freq = Counter(t)

is_anagram = True

for c, f in s_freq.items():
    if t_freq.get(c, 0) != f:
        is_anagram = False
        break

print("true" if is_anagram else "false")