function solution(cipher, code) {
    var answer = [];
    
    //문자를 배열로 취급
    //const arr = cipher.split();
    for(let i= code-1; i<cipher.length; i+=code){
        //answer.push(cipher(i));
        answer.push(cipher[i]);
        
    // console.log(answer);
    // if(i % code === 0){
    //    answer =  cipher.push(i);
    // }
    // console.log("배열에 문자열을 합침" + answer.join(''));
        
}
    //공백도 하나의 문자로 취급 
    return answer.join('');
}