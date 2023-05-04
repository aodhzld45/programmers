# 2020 카카오 인턴쉽 기출 키패드 누르기 

def solution(numbers, hand):
    answer = ''
    # 147 - left / 2580 - center / 369 - right
    # 왼손잡이 / 오른손 잡이 구분 -> 두 엄지손가락의 길이가 같을 때 
    # 좌표 값 구하기
    pad = dict()
    pad[1] = ['1', '4', '7', '*'] # 왽쪽
    pad[2] = ['2', '5', '8', '0'] # 중앙
    pad[3]=  ['3', '6', '9', '#'] # 오른쪽
    
    left = [1,3]
    right = [3,3]
    
    for i in numbers:
        for j in range(1,4):
            for k in range(len(pad[j])):
                if pad[j][k] == str(i):
                    nx, ny = j, k
                    break
        if i in [1,4,7]:
            answer += "L"
            left = [nx, ny]
        elif i in [3,6,9]:
            answer += "R"
            right = [nx, ny]
        else:
            if abs(left[0]-nx)+abs(left[1]-ny) < abs(right[0]-nx)+abs(right[1]-ny):
                answer += "L"
                left = [nx, ny]
            elif abs(left[0]-nx)+abs(left[1]-ny) > abs(right[0]-nx)+abs(right[1]-ny):
                answer += "R"
                right = [nx, ny]
            else:
                if hand == "right":
                    answer += "R"
                    right = [nx, ny] 
                else:
                    answer += "L"
                    left = [nx, ny]   
    
    return answer
