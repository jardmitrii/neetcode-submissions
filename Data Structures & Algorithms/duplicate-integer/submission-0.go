func hasDuplicate(nums []int) bool {
    uniq := map[int]struct{}{}
    for _, v := range nums{
        uniq[v] = struct{}{}
    }

    return len(nums) != len(uniq)
}
