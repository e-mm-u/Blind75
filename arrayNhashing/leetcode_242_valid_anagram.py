def isAnagram(s,t):
    hash_map = { }
    lenS = len(s)
    lenT = len(t)

    if(lenS ==lenT):
        for i in range(lenS):
            if(s[i] in hash_map):
                continue
            else :
                hash_map[s[i]] = s.count(s[i])

        hashLen = len(hash_map)
        c = 0
        # print(hash_map, hashLen)

        setT = set(t)
        setLen = len(setT)
        # print(setT)
        for i in setT :
            if(i in hash_map):
                if(hash_map[i] == t.count(i)):
                    c += 1
            else :
                return False
        if(c == hashLen):
            return True
    
    return False

s = "rat"
t = "cat"
# s = "anagram"
# t = "nagaram"
print(isAnagram(s,t))