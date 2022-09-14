class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        hashmap = { }
        for i in range(l):
            d = target - nums[i]

            if d in hashmap:
                return [hashmap[d], i]
            hashmap[i] = i

        