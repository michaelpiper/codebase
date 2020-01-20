def find_treasure(t_map, row, col, curr_steps, min_steps):
    if row >= len(t_map) or row < 0 or col >= len(t_map[0]) or col < 0 or t_map[row][col] == 'D' or t_map[row][col] == '#':
        return None, min_steps

    if t_map[row][col] == 'X':
        curr_steps += 1
        if min_steps > curr_steps:
            min_steps = min(curr_steps, min_steps)

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


def main(tr_mp):
    main_min_steps = float('inf')
    start = None
    for row in range(len(treasure_map)):
        for col in range(len(treasure_map[0])):
            # min_res = [0, 0]
            if treasure_map[row][col] == 'S':
                min_res = find_treasure(tr_mp, row, col, -1, main_min_steps)

            if min_res[1] < main_min_steps:
                start = row, col
                main_min_steps = min_res[1]

    return main_min_steps, start


if __name__ == '__main__':
    treasure_map = [['S', 'O', 'O', 'S', 'S'],
                    ['D', 'O', 'D', 'O', 'D'],
                    ['O', 'O', 'O', 'O', 'X'],
                    ['X', 'D', 'D', 'O', 'O'],
                    ['X', 'D', 'D', 'D', 'O']]
    print(main(treasure_map)[0])