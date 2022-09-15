# def isAnagram(s,t):
#     hash_map = { }
#     lenS = len(s)
#     lenT = len(t)

#     if(lenS ==lenT):
#         for i in range(lenS):
#             if(s[i] in hash_map):
#                 continue
#             else :
#                 hash_map[s[i]] = s.count(s[i])

#         hashLen = len(hash_map)
#         c = 0
#         # print(hash_map, hashLen)

#         setT = set(t)
#         setLen = len(setT)
#         # print(setT)
#         for i in setT :
#             if(i in hash_map):
#                 if(hash_map[i] == t.count(i)):
#                     c += 1
#             else :
#                 return False
#         if(c == hashLen):
#             return True
    
#     return False


# -------------------------------- solution 2 ------------

# def isAnagram(s,t):
#     return sorted(s) == sorted(t)

# -------------------------------- solution 3 ------------

# from typing import Counter


# def isAnagram(s,t):
#     return Counter(s) == Counter(t)
    

# -------------------------------- solution 4 ------------

# def isAnagram(s,t):

#     lenS = len(s)
#     hashmapS = {}
#     hashmapT = {}

#     if(lenS != len(t)):
#         return False

#     for i in range(lenS):
#         if(s[i] not in hashmapS):
#             hashmapS[s[i]] = s.count(s[i])
#         if(s[i] not in hashmapT):
#             hashmapT[s[i]] = t.count(s[i])
    
    
#     hashmapSlen = len(hashmapS)

#     if(hashmapSlen != len(hashmapT)):
#         return False
    
#     else :
#         for i in hashmapS:
#             if hashmapS[i] != hashmapT[i] :
#                 return False
#             else:
#                 continue

#         return True


# -------------------------------- solution 5 ------------

# def isAnagram(s,t):

#     lenS = len(s)
#     hashmapS = {}
#     hashmapT = {}

#     if(lenS != len(t)):
#         return False

#     for i in range(lenS):
#         if(s[i] not in hashmapS):
#             hashmapS[s[i]] = s.count(s[i])
#         if(s[i] not in hashmapT):
#             hashmapT[s[i]] = t.count(s[i])

#     return hashmapS == hashmapT

# -------------------------------- solution 6 ------------

def isAnagram(s,t):
    lenS = len(s)

    if(lenS != len(t)):
        return False

    hashmapS, hashmapT = {}, {}

    for i in range(lenS):
        hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
        hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

    return hashmapS == hashmapT

# ------------------------ test case ---------------------
# s = "rat"
# t = "cat"
s = "anagram"
t = "nagaram"
print(isAnagram(s,t))