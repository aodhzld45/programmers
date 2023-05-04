# 프로그래머스 124 나라의 숫자

def solution(n):
    answer = ''
    # n이 0이 될 때까지 반복
    while n > 0:
        # 3진법으로 변환한 나머지를 구함
        remainder = n % 3
        # 1, 2, 4 중 하나로 변환하여 answer에 추가
        if remainder == 1:
            answer = '1' + answer
        elif remainder == 2:
            answer = '2' + answer
        else:
            answer = '4' + answer
        # n을 3으로 나눈 몫으로 업데이트
        n = (n - 1) // 3
    return answer

print(solution(10))


# 강사님의 풀이
def solution(n):
    answer = ''
    s = ['4','1','2'] # 나머지 0 1 2
    while True:
        a = n // 3 # 몫
        b = n % 3  # 나머지
        if a > 0 and b == 0: # 3의 배수 일때
            a -= 1
        answer = s[b]+ answer
        if a == 0:
            break
        n = a
    return answer

print(solution(5))

            
     
