func hasDuplicate(nums []int) bool {
    // sort, check siblings
    // use a dict, check the freq O(n)
    freq := make(map[int]int)
    for _, val :=range(nums) {
        _, ok := freq[val]
        if ok {
            return true;
        } else {
            freq[val] = 1
        }
    }
    return false
}
