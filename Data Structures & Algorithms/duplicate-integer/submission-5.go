func hasDuplicate(nums []int) bool {
    uniq := make(map[int]struct{})
    for _, v := range nums{
        uniq[v] = struct{}{}
    }

    return len(nums) != len(uniq)
}
