# Frequency of characters:
# Constraints := 'a'<=s[i]<='z'
# Ques1:
s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

class Solution1:
    def getFrequency(self, x:list[int], y:list[int]) -> list[int]:
        hash_list = [0]*26

        for char in x:
            ascii_val = ord(char)
            index = ascii_val - 97
            hash_list[index] += 1
        for char in y:
            ascii_val = ord(char)
            index = ascii_val - 97
            print(hash_list[index])
        return hash_list

charFreq = Solution1()
charFreq.getFrequency(s, q)

# Ques2: with no constraints
s = "ABazCCCyxyyaaaaZZ"
q = ["a","a","y","x","A","Z","C"]