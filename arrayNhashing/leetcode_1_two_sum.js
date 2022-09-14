// init a hash map. initially empty 
// go through a for loop , if (target - arr[]) does not exist in hashmap
// add the value : index to hashmap
// otherwise if the value is in hashmap
// then return the arr index and the index of that value

var twoSum = function(nums, target) {
    const hashmap = { };
    const len = nums.length;

    for(let i = 0; i < len ; i++){
        const d = target-nums[i]
        console.log(d, i);

        console.log('hash map : ', hashmap)
        if(d in hashmap){
            console.log(d);
            return [hashmap[d], i]
        }
        hashmap[nums[i]] = i;
    }

};

var nums =  [2,7,11,15];
var target = 9;
console.log(twoSum(nums, target));