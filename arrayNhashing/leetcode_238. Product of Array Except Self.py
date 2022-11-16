def fnc(nums):
    l = len(nums)
    pre, post = 1 , 1
    res = [] #[1 for i in range(l)]
          
# get all the prefix multiplication result for each index
    for i in range(l):
        # res[i] = pre
        res.append(pre)
        pre *= nums[i]

# as we already got prefix multiplication result , multiply by post fix multiplication
    for i in range(l-1,-1,-1):
        res[i] *= post
        post *= nums[i]

    print(res)


    l = len(nums)
    res = [1 for i in range(l)]
    res[0] = 1
    for i in range(1,l,1):
        res[i] = res[i-1]*nums[i-1]

    for i in range(l-1,0,-1)


nums = [1,2,3,4,5]
fnc(nums)