# import re
# def solution(babbling):
#     answer = 0
#     for msg in babbling:
#         msg = msg.replace('aya', '@', 1)
#         msg = msg.replace('ye', '@', 1)
#         msg = msg.replace('woo', '@', 1)
#         msg = msg.replace('ma', '@', 1) 
#         msg = msg.replace('@', '')
#         if(len(msg) == 0):
#             answer += 1
#     return answer

def solution(babbling):
    count = 0
    babble = [ "aya", "ye", "woo", "ma" ]
    for a in babbling:
        for b in babble:
            if b * 2 not in a:
                a = a.replace(b, ' ')
        if a.strip()== '':
            count += 1
    return count