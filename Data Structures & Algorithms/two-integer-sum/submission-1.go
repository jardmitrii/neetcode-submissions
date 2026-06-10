func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

    for i,v := range nums {
        j, found := seen[target - v]
        if found {
            return []int{j, i}
        }

        seen[v] = i
    }

    return nil
}
