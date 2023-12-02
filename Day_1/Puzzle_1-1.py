import re;

total = 0;



with open('./Day_1/input.txt', 'r', encoding='UTF-8') as file:
    while line := file.readline():
        thisLine = line.rstrip();
        print('line: ' + thisLine);

        firstNum = re.search(r'\d', thisLine).group()[0];
        print('firstNum: ' + firstNum);

        lastNum = re.findall(r'\d', thisLine)[-1];
        print('lastNum: ' + lastNum);

        numString = '' + firstNum + '' + lastNum;
        print(numString);

        total += int(numString);
        print(total);

print(total);