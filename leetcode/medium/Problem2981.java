package leetcode.medium;


import java.util.HashMap;

/**
 * Leetcode 2981
 * <p>
 * Link: <a href="https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description/">Problem</a>
 * <p>
 * Hint: Traverse and check all substrings
 * */

public class Problem2981 {
    public static int maximumLength(String s)  {
        HashMap<String, Integer> records = new HashMap<>();

        String k0 = String.valueOf(s.charAt(0));
        records.put(k0, records.getOrDefault(k0, 0) + 1);

        int n = s.length();
        for (int i = 1; i < n; i++) {
            String k = String.valueOf(s.charAt(i));
            records.put(k, records.getOrDefault(k, 0) + 1);

            int j = i-1;
            while (j >= 0 && s.charAt(j) == s.charAt(i)) {
                String str = s.substring(j, i+1);
                records.put(str, records.getOrDefault(str, 0) + 1);
                j--;
            }
        }
        int ans = -1;
        for (String k : records.keySet()) {
            int v = records.get(k);
            if (v >= 3) {
                System.out.println(k + " " + v);
                ans = Math.max(k.length(), ans);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(maximumLength("aaaa"));
        System.out.println(maximumLength("abcdef"));
        System.out.println(maximumLength("abcaba"));
    }
}
