package main

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	letters := map[byte]string{
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
	}

	ans := []string{""}

	for i := 0; i < len(digits); i++ {
		chars := letters[digits[i]]
		temp := []string{}

		for _, prefix := range ans {
			for _, ch := range chars {
				temp = append(temp, prefix+string(ch))
			}
		}

		ans = temp
	}

	return ans
}
