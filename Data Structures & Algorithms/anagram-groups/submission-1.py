class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for ch in s:
                freq[self.abcOrder(ch)] += 1

            anagrams[tuple(freq)].append(s)
            
        return list(anagrams.values())

    def abcOrder(self, ch: str) -> int:
        return ord(ch) - 97