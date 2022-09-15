// ---------- my solution ---------------
// var isAnagram = function(s, t) {
//     const lenS = s.length;

//     if(lenS !== t.length){
//         return false
//     }

//     const hashmapS = {}
//     const hashmapT = {}

//     for(let i=0; i<lenS; i++){

//         if(s[i] in hashmapS){
//             hashmapS[s[i]] += 1;
//         }else{
//             hashmapS[s[i]] = 1;
//         }

//         if(t[i] in hashmapT){
//             hashmapT[t[i]] += 1;
//         }else{
//             hashmapT[t[i]] = 1;
//         }
//     }

//     // console.log(hashmapS, hashmapT);

//     const hashmapSlen = hashmapS.length;
//     let c = 0;

//     if(hashmapSlen !== hashmapT.length){
//         return false;
//     }

//     for(key in hashmapS){
//         if(key in hashmapT){
//             if(hashmapT[key]!==hashmapS[key]){
//                return false;
//             }

//         }else{
//             return false;
//         }
//     }
    
//     return true;

// };


// ------------ another solution --------
var isAnagram = function(s, t) {
    if(s.length !== t.length){
        return false;
    }
    const hashmapS = {};
    const hashmapT = {};

    for(i = 0; i<s.length; i++){
        if(s[i] in hashmapS){
            hashmapS[s[i]] += 1;
        }else{
            hashmapS[s[i]] = 1;
        }

        if(t[i] in hashmapT){
            hashmapT[t[i]] += 1;
        }else{
            hashmapT[t[i]] = 1;
        }
    }

    for(let key in hashmapS){
        if(hashmapS[key] !== hashmapT[key]){
            return false;
        }
    }
    return true;
}
// ---------- test cases ----------
// s = "rat"
// t = "cat"
s = "anagram"
t = "nagaram"
console.log(isAnagram(s,t))