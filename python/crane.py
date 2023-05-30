def solution(board, moves):
    answer = 0
    basket = []  # 바구니

    # 크레인을 차례대로 작동시킴
    for move in moves:
        # 인형을 집을 열 번호 index는 0부터 시작 전체 -1
        col = move - 1

        # 크레인이 해당 열에서 가장 위에 있는 인형을 찾음
        for row in range(len(board)): 
            #board의 첫번째 행은 가장 아래 / 마지막 행은 가장 위
            if board[row][col] != 0:
                doll = board[row][col]  # 인형을 집음
                board[row][col] = 0  # 인형을 집은 자리는 빈칸으로 표시

                # 바구니에 같은 모양의 인형이 있는지 확인하여 터트림
                if len(basket) > 0 and basket[-1] == doll:
                    basket.pop()  # 바구니에서 인형을 제거
                    answer += 2  # 인형이 터졌으므로 개수를 2 증가
                else:
                    basket.append(doll)  # 바구니에 인형을 추가
                break

    return answer

board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

result = solution(board, moves)
print(result) 