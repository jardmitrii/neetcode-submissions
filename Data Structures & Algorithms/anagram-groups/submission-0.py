class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            
            freq = [0] * 26
            for ch in s:
                freq[self.abcOrder(ch)] += 1
            
            freq = tuple(freq)
            if freq in anagrams:
                anagrams[freq].append(s)
            else:
                anagrams[freq] = [s]
            
        return list(anagrams.values())

    def abcOrder(self, ch: str) -> int:
        return ord(ch) - 97