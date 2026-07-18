package main

func searchMatrix(matrix [][]int, target int) bool {
	r, c := len(matrix), len(matrix[0])
	i, j := 0, c-1
	for 0 <= i && i < r && 0 <= j && j < c {
		if matrix[i][j] == target {
			return true
		} else if matrix[i][j] < target {
			i += 1
		} else {
			j -= 1
		}
	}

	return false
}
