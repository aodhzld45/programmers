# 스테이지의 갯수 N, 각각의 사용자가 몇번의 스테이지에 있는지 나타내는 배열 stages 

# 1. 총사용자의 명수 구하기 
# 2. 각각의 스테이지에 몇몇의 사용자가 있는지 구하기 
# 3. 각 스테이지별 실패율 구하기
# ★스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의
# from functools import cmp_to_key

# def compare(a, b):
#     if a[i] == b[i]:
#         return a[0] - b[0]
#     return b[i] - a[i]

# def solution(N, stages):
#     answer = []
#     failure = [] # 실패율을 담을 배열
#     # 1. 총사용자의 명수 -> stages의 크기(길이)만큼
#     total = len(stages);
#     # 2. 각각의 스테이지에 몇몇의 사용자가 있는지 구하기

#     # 2-1 제한사항 stages에는 1 이상 N + 1 이하의 자연수
#     users = [0 for _ in range(N+1)]
#     # 2-2 stages 인덱스를 읽어와서 하나씩 count    
#     for s in stages:   
#     # s-1은 index를 0부터 count하기 위해
#         users[s-1] += 1
        
#     # 3. 각 스테이지별 실패율 구하기
#     # 3-1 각 스테이지 번호를 나타내는 i
#     for i in range(N):
#     # ★스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의
#         if users[i] == 0:
#             failure.append((i+1, 0)) # tuple 형태
#     # 3-2 해당 스테이지의 사용자수 / 전체 사용자로 나눈값 = 실패율
#         else:
#             failure.append((i+1, users[i]/total)) # tuple 형태
#     # 3-3 그 다음 스테이지의 값을 구하기 위해 전체 사용자에서  해당 스테이지 도달한 사용자를 빼기
#             total -= users[i]
#         # 정렬
#         for f in sorted(failure, key=cmp_to_key(compare)):
#             answer.append(f[0])
            
#         return answer
    
#########################
'''
Simple Code
'''
        
# 스테이지의 갯수 N, 각각의 사용자가 몇번의 스테이지에 있는지 나타내는 배열 stages 

# 1. 총사용자의 명수 구하기 
# 2. 각각의 스테이지에 몇몇의 사용자가 있는지 구하기 
# 3. 각 스테이지별 실패율 구하기
# ★스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의

def solution(N, stages):
    failure = {} # 실패율 딕셔너리로 key: 스테이지 / value: 실패율로 정의하기 위해 사용
    total = len(stages) # 총사용자의 명수 -> stages의 크기(길이)만큼
    
    for stage in range(1, N+1): # stages에는 1 이상 N + 1 이하의 자연수
    
        if total != 0:
            
            count = stages.count(stage) # count함수를 이용한 사용자수 순환 체크
            failure[stage] = count / total # 실패율 구하기 = 해당 스테이지의 사용자수 / 전체 사용자로 나눈값 
            total -= count # 그 다음 스테이지의 값을 구하기 위해 전체 사용자에서  해당 스테이지 도달한 사용자를 빼기
            
        else:
            failure[stage] = 0 # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의
    
        failureArr = list(failure.items()) # failure 딕셔너리의 key value값을 모두 가져오기 위해 items() 사용
        failureArr.sort(key=lambda x: (-x[1], x[0])) #enumalate를 이용한 반복
        sorted_failure = [f[0] for f in failureArr] # enumerate() 메소드를 활용해서 keypad의 index와 value가 같이 나오도록 순환
         
        print(sorted_failure)

    return sorted_failure


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(9, [8, 7, 6, 5, 4, 3, 2, 1]))













    
    