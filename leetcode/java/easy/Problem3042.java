package leetcode.java.easy;


/**
 * Leetcode 3042
 * <p>
 * Link: <a href="https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/">Problem</a>
 * <p>
 * Hint:
 * */
public class Problem3042 {
    public static int countPrefixSuffixPairs(String[] words) {
        int total = words.length;
        int count = 0;
        for (int i = 0; i < total; i++) {
            for (int j = i+1; j < total; j++) {
                int l = words[i].length();
                int m = words[j].length();
                if (l > m) {
                    continue;
                }
                boolean canCount = true;
                for (int k = 0; k < l; k++) {
                    boolean isPrefix = words[i].charAt(k) == words[j].charAt(k);
                    boolean isSuffix = words[i].charAt(l-k-1) == words[j].charAt(m-k-1);
                    if (!isSuffix || !isPrefix) {
                        canCount = false;
                        break;
                    }
                }
                if (canCount) {
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countPrefixSuffixPairs(new String[]{"a", "aba", "ababa", "aa"}));
        System.out.println(countPrefixSuffixPairs(new String[]{"bb", "bb"}));
        System.out.println(countPrefixSuffixPairs(new String[]{"a", "c", "cacaa", "ccccc"}));
        System.out.println(countPrefixSuffixPairs(new String[]{"pa", "papa", "ma", "mama"}));
        System.out.println(countPrefixSuffixPairs(new String[]{"abab", "ab"}));
    }
}
