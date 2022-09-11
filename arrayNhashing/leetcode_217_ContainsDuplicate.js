// var containsDuplicate = function(nums) {
//     const arrSet = new Set(nums);
//     return (nums.length > arrSet.size);
// };

var containsDuplicate = function(nums) {

    const hashSet = new Set();

    for (let num of nums){

        if(hashSet.has(num)){
            return true;
        }else{
            hashSet.add(num);
        }
    };

    return false;

};



// // -------- for testing purpose -----

nums = [1,2,3,1]
ans = containsDuplicate(nums);
console.log(ans);
//  //for testing purpose --------

// console.log(`nums : ${nums} length : ${nums.length}`);
// console.log(`set ${arrSet} length : ${arrSet.size}`);

