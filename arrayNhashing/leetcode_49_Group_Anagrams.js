var groupAnagrams = function (strs) {
    const hashmap = {}
    for (let str of strs) {
        let key = str.split('').sort();
        // hashmap[key] = hashmap[key] ? hashmap[key].push(str) : (hashmap[key] = [], hashmap[key] = hashmap[key].push(str))

        if(hashmap[key]){
            
            hashmap[key].push(str);
        }else{
            hashmap[key] = []
            hashmap[key].push(str);
        }
    }

    const ret = [];
    for (key in hashmap){
        ret.push(hashmap[key])
    }

    // console.log(ret)
    return ret;
};

// ---- test case ---- 
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)
// console.log(groupAnagrams(strs))