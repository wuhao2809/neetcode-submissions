func twoSum(nums []int, target int) []int {
    valueIdxMap := make(map[int]int)
	for i, num := range nums {
		valueIdxMap[num] = i
	}
	for i, num := range nums {
		diff := target - num
		if j, found := valueIdxMap[diff]; found && j != i {
			return []int{i, j}
		}
	}
	return []int{}
}
