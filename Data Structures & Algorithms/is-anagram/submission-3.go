func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    chMap := make(map[byte]int)

    for i := range len(s) {
        chMap[s[i]]++
        chMap[t[i]]--
    }
    
    for _, v := range chMap {
        if v != 0 {
            return false
        }
    }

    return true 
}
