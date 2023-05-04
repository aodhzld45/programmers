function solution(s) {
    // 제한 사항 s가 공백, 숫자 'Z'로 이루어져 있어서 split ' ' 공백을 따로 분리
    s = s.split(' ');

    let answer = [];
    //순환을 돌면서 Z을 만났을 때 
    for(let i of s){
        if(i === 'Z'){
            answer.pop() // 마지막에 더한 값을 빼주기위해 pop 
        }else{
            answer.push(+i) //숫자로 변환해서 push하고 싶을 때 앞에 +붙임
        }
    }
    
    //모든 배열의 누적된 값 합을 구하기 위해 reduce / 초기값 0으로 설정
    //a에 자신을 더해감 -> "1 2 Z 3" 일때 1+2+Z+3 조건문에 Z를 만나면 pop 이기 때문에 1+3 = 4 가 반환됨. 
    return answer.reduce((a, c) => a + c, 0)
}
