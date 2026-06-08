func hasDuplicate(nums []int) bool {
    uniq := make(map[int]bool)
    for _, v := range nums{
        uniq[v] = true
    }

    return len(nums) != len(uniq)
}
