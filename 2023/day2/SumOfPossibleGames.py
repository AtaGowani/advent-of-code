def getSumOfPossibleGames(filename, redCount, greenCount, blueCount):
    f = open(filename, "r")
    sumOfPossibleGames = 0
    colorToCountMap = {"red": redCount, "blue": blueCount, "green": greenCount}

    for game in f:
        validGame = True
        game = "".join(game.split())
        colonIndex = game.find(":")
        gameId = int(game[4:colonIndex])
        rounds = game[colonIndex + 1 :].split(";")

        for round in rounds:
            colorsWithCount = round.split(",")
            for colorWithCount in colorsWithCount:
                for boxColor, maxCount in colorToCountMap.items():
                    colorIndex = colorWithCount.find(boxColor)
                    if colorIndex != -1:
                        count = int(colorWithCount[:colorIndex])
                        if count > maxCount:
                            validGame = False
        if validGame:
            sumOfPossibleGames += gameId

    return sumOfPossibleGames


def getSumOfPowersOfGames(filename):
    f = open(filename, "r")
    sumOfPowerOfGames = 0

    for game in f:
        gamePower = 1
        colorToMinCount = {"red": 0, "blue": 0, "green": 0}
        game = "".join(game.split())
        colonIndex = game.find(":")
        rounds = game[colonIndex + 1 :].split(";")

        for round in rounds:
            colorsWithCount = round.split(",")
            for colorWithCount in colorsWithCount:
                for color in colorToMinCount:
                    colorIndex = colorWithCount.find(color)
                    if colorIndex != -1:
                        count = int(colorWithCount[:colorIndex])
                        if count > colorToMinCount.get(color):
                            colorToMinCount[color] = count
        for x in colorToMinCount.values():
            gamePower *= x
        sumOfPowerOfGames += gamePower

    return sumOfPowerOfGames


print(getSumOfPowersOfGames("input.txt"))
print(getSumOfPossibleGames("input.txt", 12, 13, 14))
