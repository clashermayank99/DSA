# Method:1, Frequency map

nums = [5,6,7,7,2,9,111,1,1,5,1,1]

class Solution():
    def getFrequency(self, x:list[int]) -> dict[int,int]:
        freq_map = dict()

        nums = x
        for i in range(0,len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]] += 1
            else:
                freq_map[nums[i]] = 1
        return freq_map
    
frequency = Solution()
print(frequency.getFrequency(nums))

# Method:2,
class Solution2():
    def getFrequency(self, x:list[int]) -> dict[int, int]:
        hash_map = dict()
        n = len(x)
        for i in range(0,n):
            hash_map[x[i]] = hash_map.get(x[i],0)+1
        return hash_map
    
frequency2 = Solution2()
print(frequency2.getFrequency(nums))