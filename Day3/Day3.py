def move_right(x, y):
    return x + 1, y


def move_down(x, y):
    return x, y - 1


def move_left(x, y):
    return x - 1, y


def move_up(x, y):
    return x, y + 1


def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)


def gen_points(end):
    final = []
    puntos = {}
    from itertools import cycle
    moves = [move_right, move_up, move_left, move_down]
    _moves = cycle(moves)
    n = 1
    pos = 0, 0
    times_to_move = 1

    # yield n,pos

    while n <= end:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                puntos[pos] = get_value(pos,puntos)
                if(puntos[pos] > end):
                    return puntos[pos]
                # puntos[pos] = n
                pos = move(*pos)
                n += 1
                # yield n,pos

        times_to_move += 1

    return puntos


def exercise_day3(goal):
    return manhattan_distance((0, 0), (goal[0], goal[1]))


def get_value(current, puntos):
    salida = 0
    if current[0] == 0 and current[1] == 0:
        return 1
    else:
        if ((current[0]+1, current[1]+1) in puntos):
            salida += puntos[(current[0]+1, current[1]+1)]
        if ((current[0]-1, current[1]-1) in puntos):
            salida += puntos[(current[0]-1, current[1]-1)]
        if ((current[0]-1, current[1]+1) in puntos):
            salida += puntos[(current[0]-1, current[1]+1)]
        if ((current[0]+1, current[1]-1) in puntos):
            salida += puntos[(current[0]+1, current[1]-1)]
        if ((current[0], current[1]+1) in puntos):
            salida += puntos[(current[0], current[1]+1)]
        if ((current[0], current[1]-1) in puntos):
            salida += puntos[(current[0], current[1]-1)]
        if ((current[0]+1, current[1]) in puntos):
            salida += puntos[(current[0]+1, current[1])]
        if ((current[0]-1, current[1]) in puntos):
            salida += puntos[(current[0]-1, current[1])]
        return salida




# salida = gen_points(361527)
salida = gen_points(361527)

# (2, -1)
print (salida)
# print(salida[(1, 0)])

# print(exercise_day3((301, 25)))

# if [361527, (301, 25)] in list(gen_points(361527)):
#     print(True)
