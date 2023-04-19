    // 1. 주어진 정수 배열 arr1, arr2 각 원소(x)를 이진수로 변환 
    // 2. arr1을 지도1 arr2 지도2로 명시
    // 3. 벽은 or / 공백은 and로처리
    
    // function solution(price) {
    // if (price >= 100000 && price < 300000) {
    //     return Math.floor(price * .95)
    // } else if (price >= 300000 && price < 500000) {
    //     return Math.floor(price * .9)
    // } else if (price >= 500000) {
    //     return Math.floor(price * .8)
    // } else {
    //     return price
    // }

    //  //배열 정렬
    // sides.sort((a, b) => a - b); //배열 오름차순(큰 순으로 정렬)

    // sides.sort((a, b) => b - a); //배열 내림차순(큰 순으로 정렬)

    // return answer;
//  }

    // 1. 주어진 정수 배열 arr1, arr2 각 원소(x)를 이진수로 변환 
    // 2. arr1을 지도1 arr2 지도2로 명시
    // 3. n은 정사각형의 크기 한변 
    // 4. 벽은 or / 공백은 and로처리

    function solution(n, arr1, arr2) {
        var answer = [];
    //  1. js map 메서드는 배열 내의 모든 요소 각각에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환
    //  2. map은 callback 함수를 각각의 요소에 대해 한번씩 순서대로 불러 그 함수의 반환값으로 새로운 배열을 만듬     
        const map1 = arr1.map(binaryString); //callback 함수형태로 전달
        const map2 = arr2.map(binaryString);
        
        // let bin_arr1 = arr1.toString(2);
        for(let i=0; i < n; i++){ //n : 행
            let row = ''; //열 
            for(let j=0; j< n; j++){
                if(map1[i][j] === '1' || map2[i][j] === '1'){
                    row += '#';
                }else {
                    row += ' ';
                }
            }
            answer.push(row);
        //1. 정수형 배열 arr1[] , arr2[]의 원소를 2진법으로 변환 -> 함수로 따로 작성
            // var bin_arr1 = arr1[i].toString(2);
            // var bin_arr2 = arr2[i].toString(2);
            // console.log(bin_arr1);
        }
            console.log(answer) 
    
        return answer;
    }
    
    //  10진수를 2진수로 변환하는 함수.
    function binaryString(binStr, n){
        let binaryString = binStr.toString(2);
        
    //  변환한 값이 n보다 작을경우 앞에 0을 채움
        while(binaryString.length < n){
            binaryString = '0' + binaryString
        }
        return binaryString;
    }
    
    
    