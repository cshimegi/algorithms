package leetcode.java.easy;


/**
 * Leetcode 2923
 * <p>
 * Link: <a href="https://leetcode.com/problems/find-champion-i/description/">Problem</a>
 * <p>
 * Hint: Checking half side of the grid is enough
 * */
public class Problem2923 {
    public static int findChampion(int[][] grid) {
        int n = grid.length;
        int[] records = new int[n];
        // Count the records from bottom-left of the grid
        // because the half side records opposite is the same
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (grid[i][j] == 1) {
                    records[i] += 1;
                } else {
                    records[j] += 1;
                }
            }
        }
        // Find the index with maximum value in the records
        int champion = 0;
        int maxValue = 0;
        for (int i = 0; i < n; i++) {
            if (records[i] > maxValue) {
                maxValue = records[i];
                champion = i;
            }
        }
        return champion;
    }

    public static void main(String[] args) {
        int[][] tournament = new int[][]{
                {0, 1, 0},
                {0, 0, 0},
                {1, 1, 0},
        };
        System.out.println(findChampion(tournament));

        int[][] tournament2 = new int[][]{
                {0, 1},
                {0, 0},
        };
        System.out.println(findChampion(tournament2));

        int[][] tournament3 = new int[][]{
                {0, 1, 0, 1},
                {0, 0, 0, 1},
                {1, 1, 0, 1},
                {0, 0, 0, 0},
        };
        System.out.println(findChampion(tournament3));

        int[][] tournament4 = new int[][]{
                {0, 0, 0},
                {1, 0, 1},
                {1, 0, 0},
        };
        System.out.println(findChampion(tournament4));
    }
}
