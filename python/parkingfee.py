import math
# 시간을 분으로 계산하여 리턴하는 함수
def convert(time):
    hh, mm = time.split(':') # 시:분으로 구분하기 위해 : 기준으로 split문자열 나누기
    return int(hh) * 60 + int(mm)

# map 자료구조 이용 key value 형태로 담음
def solution(fees, records):
    intime = {} # 입차시간을  딕셔너리
    result = {} # 누적 주차시간을 저장할 딕셔너리
    
    # 입력을 받을 레코드 처리
    for r in records:
        # 입출차 시각, 차량번호, 입출차 여부를 구분하기 위해 split() 공백기준 문자열 나누기
        time, carnum, inout = r.split()
        # 입출차 여부 조건
        if inout == 'IN': # 입차인 경우
            intime[carnum] = convert(time) # key를 차량번호 value를 시간(분단위)
            if carnum not in result: # result에 차량번호가 없는경우
                result[carnum] = 0 # 차량번호 초기값을 0으로
        
        #elif inout == 'OUT':        
        else: # OUT 출차인 경우 
            result[carnum] += convert(time) - intime[carnum] # 주차 시간 - 입차시간을 뺀값을 result에 누적 = 시간을 계산                  
            del intime[carnum] # 차량이 out 나갔으니깐 intime에서 delete 삭제
        
    # 차량이 입차만하고 출차를 하지 않은 경우 - 23:59에 출차되었다고 간주
    # 1. 남은 차량이 있는지 확인
    for key, value in intime.items(): # key-차량번호:value-입차시간 형태로 반환 - items() 
        # out과 비슷하지만 주차시간이 고정 23:59
        result[key] += 23 * 60 + 59 - value 
            
    answer = []
    for key, value in sorted(result.items()): # key-차량번호: value-누적된 총 주차시간
        if value <= fees[0]: # 총 주차시간이 fees[0] - 기본시간 이하일 경우
            answer.append(fees[1])
        else: # 기본시간 이상일경우
            # 기본요금 + (누적된 총 주차시간 - 기본시간 / 단위시간) * 단위요금
            answer.append(fees[1] + math.ceil((value-fees[0]) / fees[2]) * fees[3])
            
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
    