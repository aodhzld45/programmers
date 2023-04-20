function solution(absolutes, signs) {
    var answer = 0;
    var check = false; 
    
    // if(signs)
    
    /* absolutes.length와 signs.length같음 */

    for(let i=0; i<signs.length; i++ ){
        if(signs[i] === true){
            console.log("양수 " + absolutes[i])
            answer += absolutes[i]
            console.log(answer)
                                
        }else {
            console.log("음수 " + absolutes[i])
            answer += absolutes[i] * -1 // -1을 곱하여 음수로 처리

        }
        

    }
    
    return answer;
}