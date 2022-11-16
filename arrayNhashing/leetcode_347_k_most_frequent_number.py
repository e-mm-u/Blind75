def fnc(nums,k):
    l = len(nums)
    # -----------------------------------
    d_count  = { } # hash map with value and their count

    for num in nums:
        d_count[num] = 1 + d_count.get(num,0) # do ++ with previous one, if doesn;t exist add with 0
    # print(d_count)
# ------------------------------------
    bucket = [ [] for i in range(l+1)] # max repetation could be 'l', [] list for eact index 
    # print(bucket)

    for num,count in d_count.items():
        bucket[count].append(num) #more than one number can repeat x times, so keep all the number that repeats x time in the array where index is the count number
    
    # print(bucket)
# -------------------------------------------
    ans = [] # output list

    for i in range(l,0,-1): # visit in a reverse way to make it quick
        for num in bucket[i]: # enter this loop if index value is not an empty array
            ans.append(num)
            if(len(ans)==k):
                # print('ans', ans)
                return ans

nums = [2,3,1,2,1,1]
k = 2
fnc(nums,k)