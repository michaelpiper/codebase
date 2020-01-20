from collections import deque
def solution(m):
    if len(m) == 0 or len(m[0]) == 0:
        return -1  # impossible

    matrix = [row[:] for row in m]
    nrow, ncol = len(matrix), len(matrix[0])

    q = deque([((0, 0), 0)])  # ((x, y), step)
    matrix[0][0] = "D"
    while q:
        (x, y), step = q.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= x+dx < nrow and 0 <= y+dy < ncol:
                if matrix[x+dx][y+dy] == "X":
                    # q.append(((x+dx, y+dy), step+1))
                    # print(q)
                    return step+1
                elif matrix[x+dx][y+dy] == "O":
                    # mark visited
                    
                    matrix[x + dx][y + dy] = "D"
                    q.append(((x+dx, y+dy), step+1))
                    

    return -1

if __name__ == '__main__':
    treasure_map = [['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O']]
    print(solution(treasure_map))