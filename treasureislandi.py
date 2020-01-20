# use point.py instead
def find_treasure(t_map, row, col, curr_steps, min_steps):
    if row >= len(t_map) or row < 0 or col >= len(t_map[0]) or col < 0 or t_map[row][col] == 'D' or t_map[row][col] == '#':
        return None, min_steps
    if t_map[row][col] == 'O':
        # print(row,col)
        pass
    if t_map[row][col] == 'X':
        curr_steps += 1
        if min_steps > curr_steps:
            min_steps = min(curr_steps, min_steps)
        # print(row,col)
        return None, min_steps

    else:
        tmp = t_map[row][col]
        t_map[row][col] = '#'
        curr_steps += 1
        left = find_treasure(t_map, row, col-1, curr_steps, min_steps)
        right = find_treasure(t_map, row, col+1, curr_steps, min_steps)
        up = find_treasure(t_map, row-1, col, curr_steps, min_steps)
        down = find_treasure(t_map, row+1, col, curr_steps, min_steps)

        t_map[row][col] = tmp

        return curr_steps, min(left[1], right[1], up[1], down[1])


if __name__ == '__main__':
    treasure_map = [['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]
#     treasure_map = [['O', 'O', 'O', 'X'],
#  ['O', 'O', 'O', 'O'],
#  ['O', 'O', 'O', 'O'],
#  ['O', 'O', 'O', 'O']]

    res = find_treasure(treasure_map, 0, 0, -1, float('inf'))
    print("Result: ", res[1])