import re;

total = 0;

with open('./Day_2/input.txt', 'r', encoding='UTF-8') as file:
    
    cubeAmounts = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    def adjustMinimums(cube, minimums):
        thisCube = cube.strip();
        cubeDetails = thisCube.split(' ');

        # update minimum value for each color if greater than current
        if(int(cubeDetails[0]) > minimums.get(cubeDetails[1])):
            minimums[cubeDetails[1]] = int(cubeDetails[0]);

    while line := file.readline():
        thisLine = line.rstrip();

        gamePower = 1

        minimums = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        # get gameId
        idMatch = re.search('Game (.*):', thisLine);
        gameId = int(idMatch.group(1));

        print('gameId: ' + str(gameId));

        # get grabs per game
        grabs = thisLine.split(':')[1].split(';');

        # check each amount of cube type retrieved
        for grab in grabs:
            print('grab: ' + grab);

            # check for each grab if multiple grabs
            if(grab.find(',') != -1):
                cubes = grab.split(',');

                for cube in cubes:
                    adjustMinimums(cube, minimums);
            
            # check single grab
            else:
                thisCube = grab.strip();
                adjustMinimums(thisCube, minimums);

        # multiply minimums to get power and add it to total
        for i in minimums:
            if(minimums[i] != 0):
                gamePower = gamePower * minimums[i]

        print('gamePower: ' + str(gamePower));

        total += gamePower;

        print('===============================');

print(total);