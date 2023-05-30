def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    if(sum1 + sum2) % 2 == 1: # # 전체 합이 홀수인 경우, 숫자를 공평하게 나눌 수 없음
        return -1 # 바로 -1을 return
    
    #l1, r1 = 0, len(queue1) -1 # l1, r1은 각각 queue1의 첫번째 원소 left[1], 마지막 원소 len(queue1) - 1 
    #l2, r2 = 0, len(queue2) -1  # l1, r1은 각각 queue2의 첫번째 원소 left[1], 마지막 원소 len(queue2) - 1 
    
    n = len(queue1) # n을 q1의 길이로 정의
    # 포인터 적용 -
    l1, l2 = 0, n  #왼쪽 포인터 l1과 l2를 각각 0과 n으로 초기화 -> 큐1과 큐2에서 요소를 가리키는 포인터
    
    def get_num(index): # get_num(index) 함수는 주어진 인덱스에 해당하는 요소를 가져오는 역할
            index %= 2 * n # 인덱스를 큐의 길이에 맞게 조정
            return queue1[index] if index < n else queue2[index - n] # 인덱스가 n보다 작으면 큐1에서 해당 요소를, 그렇지 않으면 큐2에서 해당 요소를 가져옴
    answer = 0
    
    while sum1 != sum2 and answer <=  3 * n: # 밑의 작업을 합이 같아지거나 최대 3 * n번 반복할 때까지 반복 -> 한 번의 반복에서 최대 2개의 요소가 이동하므로 3배의 n까지 반복하여도 충분
        answer += 1
        if sum1 > sum2: # 큐1의 합이 큐2의 합보다 큰 경우
            num = get_num(l1) # 큐1에서 현재 포인터 위치의 요소를 가져옴
            sum1 -= num # 큐1의 합에서 해당 요소를 뺌
            sum2 += num # 큐2의 합에서 해당 요소를 더함
            l1 += 1  # 큐1의 왼쪽 포인터를 오른쪽으로 이동
        else:  # 큐2의 합이 큐1의 합보다 큰 경우
            num = get_num(l2) # 큐2에서 현재 포인터 위치의 요소를 가져옴
            sum1 += num # 큐1의 합에서 해당 요소를 더함
            sum2 -= num # 큐2의 합에서 해당 요소를 뺌
            l2 += 1 # 큐2의 왼쪽 포인터를 오른쪽으로 이동
    
    return answer if answer <= 3 * n else -1 # # 최종 결과를 반환 /  최대 반복횟수 : 3 * n번 반복한 경우에는 -1을 반환

# queue1 = [3, 2, 7, 2]
# queue2 = [4, 6, 5, 1]

# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]

queue1 = [1, 1]
queue2 = [1, 5]

answer = solution(queue1,queue2)
print(f"answer: {answer}")