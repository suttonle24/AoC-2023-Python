import re;

total = 0;

with open('./Day_2/input.txt', 'r', encoding='UTF-8') as file:
    
    cubeAmounts = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    def checkPossibility(cube):
        thisCube = cube.strip();
        cubeDetails = thisCube.split(' ');

        # if more cubes of this color were grabbed than what was put in,
        # game is not possible
        if(int(cubeDetails[0]) > cubeAmounts.get(cubeDetails[1])):
            return False;
        else:
            return True;

    while line := file.readline():
        thisLine = line.rstrip();

        gameIsPossible = True;

        # get gameId
        idMatch = re.search('Game (.*):', thisLine);
        gameId = int(idMatch.group(1));

        print('gameId: ' + str(gameId));

        # get grabs per game
        grabs = thisLine.split(':')[1].split(';');

        # check each amount of cube type retrieved
        for grab in grabs:
            print('grab: ' + grab);
            possible = True;

            # check for each grab if multiple grabs
            if(grab.find(',') != -1):
                cubes = grab.split(',');

                for cube in cubes:
                    if(checkPossibility(cube) == False):
                       gameIsPossible = False;
                       break;
            
            # check single grab
            else:
                thisCube = grab.strip();
                if(checkPossibility(thisCube) == False):
                    gameIsPossible = False;
                    break;

        # add game ID to total if game is possible
        if(gameIsPossible == True):
            total += gameId;

        print('===============================');

print(total);