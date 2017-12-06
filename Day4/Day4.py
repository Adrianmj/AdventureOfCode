from collections import Counter

def checkWord(input):
    input = input.split()
    seenWords = []
    for i in range (len(input)):
        if(input[i] not in seenWords):
            seenWords.append(input[i])
        else:
            return False

    return True

def exerciseDay4(input):
    result = 0
    for i in range (len(input)):
        if(checkWord(input[i])):
            result += 1
    return result
   

def checkAnagram(word1, word2):
    return Counter(word1) == Counter(word2)


def searchAnagram(input):
    input = input.split()
    for i in range(len(input)-1):
        for j in range(i+1,len(input)):
            
            if (checkAnagram(input[i],input[j])):
                return False       
    return True     

def excersiseDay4part2(input):
    result = 0
    for i in range (len(input)):
        if(searchAnagram(input[i])):
            result += 1
    return result  



## PART 1
example1 = "aa bb cc dd ee"
example2 = "aa bb cc dd aa"
example3 = "aa bb cc dd aaa"
inputString = open("input.txt", 'r').read().split("\n")

assert checkWord(example1) == True
assert checkWord(example2) == False
assert checkWord(example3) == True

print(exerciseDay4(inputString))


## PART 2
example1part2 = "abcde fghij"
example2part2 = "abcde xyz ecdab"
example3part2 = "a ab abc abd abf abj"
example4part2 = "iiii oiii ooii oooi oooo"
example5part2 = "oiii ioii iioi iiio"
inputStringPart2 = open("inputPart2.txt", 'r').read().split("\n")

assert searchAnagram(example1part2) == True
assert searchAnagram(example2part2) == False
assert searchAnagram(example3part2) == True
assert searchAnagram(example4part2) == True
assert searchAnagram(example5part2) == False

# problema = "linzaeu qbwdke fdg pykw"
# searchAnagram(problema)

print(excersiseDay4part2(inputStringPart2))