function solution(numbers) {
    //1. 각 배열에서 두개의 원소를 뽑아서 더하기
    //2. 자기 자신은 제외 더하지 않음 ex)1+1 2+2X
    //3. 중복되는 수를 제거   
    var answer = [];
    
    for(let f_idx=0; f_idx<numbers.length; f_idx += 1){
        //두번째 s_idx값을 처음부터 첫번째 인덱스 +1로 루프 -> 같은값 방지
        for(let s_idx = f_idx+1; s_idx < numbers.length; s_idx += 1) {
            if(!answer.includes((numbers[f_idx] + numbers[s_idx]))){
                answer.push((numbers[f_idx] + numbers[s_idx]));
            }
        }
    }
    
    answer.sort(function(a, b) { //오름차순 정렬
        return a - b;
        
    });
    
    console.log(answer);

    return answer;
    
}
    
    
//     var index = 0;
//     var sum = 0;
//     var check = false;
    
//     for(let f_idx=0;  f_idx < numbers.length; f_idx++){
//         for(let s_idx=0; s_idx < numbers.length; s_idx++){
//             if(f_idx !== s_idx) { //자기자신 같은수를 더하지 않도록 조건 추가 
//                 // result[index] = numbers[f_idx] + numbers[s_idx];
//                 // index += 1;
//                 sum = numbers[f_idx] + numbers[s_idx];
//                 for(let dup = 0; dup < index; index++){
//                     if(sum === answer[dup]){
//                         check = true;
//                         break;
//                     }
//                 }
                
//                 if(check == false){
//                     answer[index] = sum;
//                     index += 1;
//                 }  
//             }
//         }
        
//     }
    
//     return answer;
// }
