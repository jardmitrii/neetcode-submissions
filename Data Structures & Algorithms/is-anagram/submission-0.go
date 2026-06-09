func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    chMap := make(map[rune]int)

    for i,v := range s {
        chMap[v] += 1
        chMap[rune(t[i])] -= 1
    }
    
    for _, v := range chMap {
        if v != 0 {
            return false
        }
    }

    return true 
}
