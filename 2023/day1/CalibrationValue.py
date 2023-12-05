def getCalibrationValue(filename):
    calibrationValue = 0
    f = open(filename, "r")

    for line in f:
        gotFirstDigit = False
        digits = []
        for ch in line:
            if ch.isnumeric():
                if not gotFirstDigit:
                    digits.append(ch)
                    digits.append(ch)
                    gotFirstDigit = True
                else:
                    digits[1] = ch
        calibrationValue += int("".join(digits))

    return calibrationValue


def getCalibrationValuePart2(filename):
    spelledDigits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    calibrationValue = 0
    f = open(filename, "r")

    for line in f:
        gotFirstDigit = False
        digits = []
        start = 0
        curr = 0
        for ch in line:
            if ch.isnumeric():
                if not gotFirstDigit:
                    digits.append(ch)
                    digits.append(ch)
                    gotFirstDigit = True
                else:
                    digits[1] = ch
            else:
                for digit in spelledDigits:
                    if digit in line[start : curr + 1]:
                        if not gotFirstDigit:
                            digits.append(spelledDigits.get(digit))
                            digits.append(spelledDigits.get(digit))
                            gotFirstDigit = True
                        else:
                            digits[1] = spelledDigits.get(digit)
                        start = curr
            curr += 1

        calibrationValue += int("".join(digits))

    return calibrationValue


print(getCalibrationValue("input.txt"))
print(getCalibrationValuePart2("input.txt"))
