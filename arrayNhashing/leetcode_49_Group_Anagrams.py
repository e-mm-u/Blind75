# def groupAnagrams(strs):
#     l = len(strs)
#     hashmap = { }

#     for i in range(l):
#         # x = ''.join(sorted(strs[i]))
#         # x = str(sorted(strs[i]))
#         x = sorted(strs[i])

#         hashmap[x] = hashmap.get(x,[]) + [x]

#         if(x in hashmap):
#             hashmap[x].append(strs[i])
#         else :
#             hashmap[x] = [strs[i]]


#     return hashmap.values()

# ----------------- sol 2 --------------
# def groupAnagrams(strs):
#     hashmap = { }

#     for s in strs:
#         x = str(sorted(s))
#         hashmap[x] = hashmap.get(x, []) + [s]

#     return hashmap.values()
# ----------------- sol 3 --------------

from collections import defaultdict
from itertools import count


def groupAnagrams(strs):
    res = defaultdict(list)

    for str in strs:
        count = [0] * 26
        for char in str:
            count[ord(char)-ord('a')] += 1
        res[tuple(count)].append(str)    
        
    return(res.values())

strs = ["eat","tea","tan","ate","nat","bat"]
# groupAnagrams(strs)
print(groupAnagrams(strs))