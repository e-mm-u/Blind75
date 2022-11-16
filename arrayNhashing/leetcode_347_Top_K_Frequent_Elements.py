#_________________ NOT EFFICIENT 
def topKFrequent(nums,k):

    unique = set(nums)
    countMap = {}
    
    for i in unique:
        count = nums.count(i)
        print(i, count)
        countMap[i] = count

    print(unique)
    print(countMap)
    dict(sorted(countMap.items(), key=lambda item: item[1]))
    print(countMap)
    ret = list(countMap.keys())
    return ret[0:k]

# nums = [1,1,1,2,2,3]
# k = 2
# nums = [7,8,9,7,4,3,3,1,9,8,7,4,3,3]
# k = 3
nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKFrequent(nums,k)) 