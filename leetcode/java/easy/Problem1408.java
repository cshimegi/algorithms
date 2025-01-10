package leetcode.java.easy;


import java.util.ArrayList;
import java.util.List;

/**
 * Leetcode 1408
 * <p>
 * Link: <a href="https://leetcode.com/problems/string-matching-in-an-array/description/">Problem</a>
 * <p>
 * Hint:
 * */
public class Problem1408 {
    public static List<String> stringMatching(String[] words) {
        int total = words.length;
        List<String> result = new ArrayList<>();
        for (int i = 0; i < total; i++) {
            for (int j = i+1; j < total; j++) {
                if (words[i].contains(words[j]) && !result.contains(words[j])) {
                    result.add(words[j]);
                } else if (words[j].contains(words[i]) && !result.contains(words[i])) {
                    result.add(words[i]);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(stringMatching(new String[]{"mass", "as", "hero", "superhero"}));
        System.out.println(stringMatching(new String[]{"leetcode","et","code"}));
        System.out.println(stringMatching(new String[]{"blue","green","bu"}));
    }
}
