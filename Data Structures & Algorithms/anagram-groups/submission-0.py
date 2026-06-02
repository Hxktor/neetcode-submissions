class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}

        for word in strs:
            key = "".join(sorted(word))  # sort the word to get the key
            
            if key not in anagram_map:
                anagram_map[key] = []    # create a new group
            
            anagram_map[key].append(word) # add word to its group

        return list(anagram_map.values())