import re;

total = 0;

numberDict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
};

numberArray = ['1','2','3','4','5','6','7','8','9'];

def getNumberString(inputLine):
    print('line: ' + inputLine);

    valueDict = {}

    # add all index-value pairs for written numbers
    for number in numberDict:
        if (inputLine.find(number) > -1):
            indicies = [m.start() for m in re.finditer(number, inputLine)]
            for index in indicies:
                valueDict[index] = numberDict[number];
    
    # add all index-value pairs for digit numbers
    for number in numberArray:
        if (inputLine.find(number) > -1):
            indicies = [m.start() for m in re.finditer(number, inputLine)]
            for index in indicies:
                valueDict[index] = numberArray[int(number) - 1];
    
    # sort the dict to prep for first/last index retrieval
    sortedDict = dict(sorted(valueDict.items()))

    # concatenate first and last number text
    number = list(sortedDict.values())[0] + list(sortedDict.values())[-1]

    print('number: ' + number);

    return number;

with open('./Day_1/input.txt', 'r', encoding='UTF-8') as file:
    while line := file.readline():
        numberString = getNumberString(line.rstrip());

        total += int(numberString);
        print('total: ' + str(total));

print(total);