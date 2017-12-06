import sys

def exercise_day2(input):
    result = 0
    for i in range (len(input)):
        output = get_min_max(input[i])
        result += output[1] - output[0]
    return result


def exercise_day2_part2(input):
    result = 0
    for i in range (len(input)):
        output  = get_evenly_numbers(input[i])
        result += output[0]/output[1]
    return result


def get_evenly_numbers(input):
    for i in range (len(input)):
        for j in range(i+1,len(input)):
            if(input[i]%input[j] == 0):
                return [input[i], input[j]]
            elif(input[j]%input[i] == 0):
                return [input[j], input[i]]


def get_min_max(input):
    min = sys.maxsize
    max = -sys.maxsize
    for i in range (len(input)):
        input[i] = input[i]
        if(input[i] < min):
            min = input[i]
        if(input[i]> max):
            max = input[i]

    return [min,max]


def textToMatrix(input):
    input = input.split("\n")
    for i in range (len(input)):
        input[i] = input[i].split()
        input[i] = list(map(int,input[i]))
        
    return input    


def matrixToString(input):
    for i in range (len(input)):
        for j in range(len(input[i])):
            print(" " + str(input[i][j]),end='')
            if(j == len(input[i])-1):
                    print("")
           



testExample = textToMatrix(open("inputExample.txt", 'r').read())
testInput = textToMatrix(open("input.txt", 'r').read())
testPart2 = textToMatrix(open("inputPart2.txt").read())
testInputPart2 = textToMatrix(open("inputExcersisePart2.txt", 'r').read())

assert (exercise_day2(testExample)) == 18
assert (exercise_day2(testInput)) == 58975

assert (exercise_day2_part2(testPart2)) == 9
assert (exercise_day2_part2(testInputPart2)) == 308
308