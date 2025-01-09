package leetcode.easy;


/**
 * Leetcode 2185
 * <p>
 * Link: <a href="https://leetcode.com/problems/counting-words-with-a-given-prefix/description/">Problem</a>
 * <p>
 * Hint:
 * */
public class Problem2185 {
    public static int prefixCount(String[] words, String pref) {
        int count = 0;
        for (String word : words) {
            if (word.startsWith(pref)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(prefixCount(new String[]{"pay", "attention", "practice", "attend"}, "at"));
        System.out.println(prefixCount(new String[]{"leetcode", "win", "loops", "success"}, "code"));
        System.out.println(prefixCount(new String[]{"i", "am", "learning", "leetcode"}, "l"));
    }
}
