function solution(absolutes, signs) {
    var answer = 0;
    var check = false; 
    
    // 음양 더하기
    
    /* absolutes.length와 signs.length같음 */

    for(let i=0; i<signs.length; i++ ){
        if(signs[i] === true){
            console.log("양수 " + absolutes[i])
            answer += absolutes[i]
                                
        }else {
            console.log("음수 " + absolutes[i])
        }
        

    }
    
    return answer;
}