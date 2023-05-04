# 프로그래머스 타겟 넘버 - 참고용 예제
# 알고리즘 - 깊이 우선 탐색 (DFS, Depth-First Search) 활용


# 1. dfs 재귀 함수를 이용한 방법 - 프로그래머스 테스트에서 RecursionError 발생
# - Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 RecursionError 발생
# import sys
# sys.setrecursionlimit(10 ** 6) # 재귀 함수의 limit값을 설정
# def solution(numbers, target):
#     answer = 0
    
#     def dfs(idx, value):
#         nonlocal answer
#         if idx == len(numbers):
#             if value == target:
#                 answer += 1 
#             return
#         dfs(idx + 1, value + numbers[idx])
#         dfs(idx - 1, value + numbers[idx])
        
#     dfs(0, 0)
#     return answer 

# print(solution([1, 2, 3, 4, 5], 5)) # 3


# 2 . stack을 이용한 풀이

def solution(numbers, target):
    answer = 0
    stack = [(0, 0)]  # (현재까지 누적된 합, 현재 인덱스)를 저장하는 스택
    while stack:
        current_sum, current_index = stack.pop()
        if current_index == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            stack.append((current_sum + numbers[current_index], current_index + 1))
            stack.append((current_sum - numbers[current_index], current_index + 1))
    return answer



print(solution([1, 2, 3, 4, 5], 5)) # 3



