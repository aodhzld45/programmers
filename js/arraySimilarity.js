function solution(s1, s2) {
    //필터를 이용한 풀이
    var answer = s1.filter(v => s2.includes(v)).length;
    
    //집합을 이용한 풀이
    //answer = s1.length + s2.length - new Set([...s1, ...s2]).size
    
    return answer

}
//  for (let i=0; i<s1.length; i++) {
//             for (let j=0; j<s2.length; j++) {
//                 if (s1[i].includes(s2[j])) {
//                     answer += 1;
//                 }
//             }
//         }
    
   
//     return answer;
// }