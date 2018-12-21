GRID_SIZE = 300

def get_hundreds_digit(num):
    assert num >= 100, "Number has no 100s digit"
    return int(num/100)%10

def get_power(x, y, serial):
    rack_id = 10 + x
    power = rack_id * y
    power += serial
    power *= rack_id
    power = get_hundreds_digit(power)
    return power - 5

def best_size(x, y, grid):
    total = 0
    totals = [grid[x][y]]
    n = 2
    new_x_layer = x + n - 1
    new_y_layer = y + n - 1
    while new_x_layer <= GRID_SIZE and new_y_layer <= GRID_SIZE and n <= GRID_SIZE:
        for cur_x in range(x, new_x_layer+1):
            total += grid[cur_x][new_y_layer]
        for cur_y in range(y, new_y_layer):
            total += grid[new_x_layer][cur_y]
        totals.append(total)
        n += 1
        new_x_layer = x + n - 1
        new_y_layer = y + n - 1
    best_total = max(totals)
    best_n = totals.index(best_total) + 1
    return best_total, best_n

def best_corner(grid, maxx=GRID_SIZE, maxy=GRID_SIZE):
    best = 0
    best_comb = (-1, -1, -1)
    for x in range(1, maxx + 1):
        print(f'Checking x : {x}')
        for y in range(1, maxy + 1):
            power_of_grid, n = best_size(x, y, grid)
            if power_of_grid > best:
                best_comb = (x, y, n)
                best = power_of_grid
    return best_comb

if __name__=='__main__':
    assert get_power(122, 79, 57) == -5
    assert get_power(217, 196, 39) == 0
    assert get_power(101, 153, 71) == 4


    serial_number = 3463
    grid = [[get_power(x, y, serial_number) for y in range(GRID_SIZE+1)] for x in range(GRID_SIZE + 1)]

    print(best_corner(grid))

# for 42 getting 232, 251, 13
# for 18 getting 90, 269, 16
# 233,282,11
