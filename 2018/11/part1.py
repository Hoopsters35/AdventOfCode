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

def power_of_3x3(x, y, serial):
    total = 0
    for cur_x in range(x, x + 3):
        for cur_y in range(y, y + 3):
            total += get_power(cur_x, cur_y, serial)
    return total

def best_corner(serial, maxx=300, maxy=300):
    best = 0
    best_coord = (-1, -1)
    for x in range(1, maxx + 1 - 3):
        for y in range(1, maxy + 1 - 3):
            power_of_grid = power_of_3x3(x, y, serial)
            if power_of_grid > best:
                best_coord = (x, y)
                best = power_of_grid
    return best_coord

if __name__=='__main__':
    assert get_power(122, 79, 57) == -5
    assert get_power(217, 196, 39) == 0
    assert get_power(101, 153, 71) == 4

    assert power_of_3x3(33, 45, 18) == 29
    assert power_of_3x3(21, 61, 42) == 30

    assert best_corner(18) == (33, 45)
    assert best_corner(42) == (21, 61)

    serial_number = 3463
    print(best_corner(serial_number))

# 235,60 
