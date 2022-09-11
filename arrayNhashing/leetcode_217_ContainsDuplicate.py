class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        print (hashSet)
        for num in nums :
            if(num in hashSet):
                return True
            hashSet.add(num)
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsset = set(nums)
        return len(nums) > len(numsset)

