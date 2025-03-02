# When to use hash-list and when to frequenct-map
# Q - Return frequency of integers of "m" in list "n"
# Contraints - (1) 1<n[i]<=10, (2) "n" can have 10**8 elements, (3) "m" can have 10**8 elements

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,6,7,2]

# Brute-force :TC - O(M*N) which 10**16 and will result in TLE error
class Solution1:
    def getFrequency(self, x:list[int], y:list[int]) -> dict[int,int]:
        freq = dict()
        for i in y:
            count = 0
            for j in x:
                if j == i:
                    count += 1
            freq[i] = count
        return freq
freq1 = Solution1()
print(freq1.getFrequency(n,m))

# Optimal solution 1: We can use hash-list if the constraint is something like this "1<n[i]<=10"
class Solution2:
    def getFrequency(self, x:list[int], y:list[int])-> list[int]:
        hash_list = [0]*11
        for num in x:
            hash_list[num] += 1
        for num in y:
            if  num <1 or num > 10:
                # hash_list[num] = 0
                print(0)
            else:
                print(hash_list[num])
        return hash_list
freq2 = Solution2()
print(freq2.getFrequency(n,m))

# Optimal solution 2: We can use frequency-map if the contraint of n doesn't have constant values
class Solution3:
    def getFrequency(self, x:list[int], y:list[int]) -> dict[int, int]:
        freq_map = dict()
        final_freq_map = dict()
        for i in range(0, len(x)):
            if x[i] in freq_map:
                freq_map[x[i]] += 1
            else:
                freq_map[x[i]] = 1
        for j in range(0, len(y)):
            if y[j] in freq_map:
                final_freq_map[y[j]] = freq_map[j]
            else:
                final_freq_map[y[j]] = 0
        return final_freq_map

freq3 = Solution3()
print(freq3.getFrequency(n,m))
