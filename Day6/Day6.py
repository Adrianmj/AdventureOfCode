def exercise_day6(input):
    steps = 0
    seen = False
    distributions_seen = {}
    second_loop_done = False
    loop_size = 0
    finalstring = ""
    while not seen or not second_loop_done and steps:
        # print("Pre: " + str(input))
        steps += 1
        max = input[0]
        max_index = 0
        loop_size += 1
        for i in range (1,len(input)):
            if(max < input[i]):
                max = input[i]
                max_index = i

        input[max_index] = 0
        while max is not 0:
            max_index += 1
            if(max_index >= len(input)):
                max_index = 0

            input[max_index] += 1
            max -= 1
        # print(finalstring)
        # print(str(input))
        if(finalstring == str(input)):
            # print(input)
            second_loop_done = True
        elif(not seen and str(input) in distributions_seen):
            seen = True
            loop_size = 0
            finalstring = str(input)
        else:
            distributions_seen[str(input)] = True

    return steps,loop_size


def get_array_from_input(input):
    input = open(input)
    return list(map(int,input.read().split()))


# print(exercise_day6(get_array_from_input("input.txt")))
print(exercise_day6(get_array_from_input("inputExercise")))