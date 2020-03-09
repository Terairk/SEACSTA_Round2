# This file houses the functions

# Assignment Conversion

# Print --> Output

# input() --> INPUT

# print : output
# input(): input
# line.count('=') == 1 : assignment
# to be continued

# returns one of the values above eg output, input & assignment
def ParseLine(line):
    if "print" in line:
        # produce output pseudocode
        return ConvertPrint(line)
    elif "input" in line and not ("print" in line):
        return ConvertInput(line)
    elif line.count("=") == 1 and not ("input") in line:
        return ConvertAssignment(line)


def ConvertInput(line):
    newString = ""
    # if the input has a prompt
    if line.count('"') > 0:
        start = line.index('"')
        end = len(line) - 2

        newString += "OUTPUT " + line[start:end] + "\n"

    variable = line.index("=") - 1
    newString += "INPUT " + line[:variable] + "\n"
    return newString


def ConvertPrint(line):
    newString = ""

    # 2 things are being outputed
    if "+" in line:
        start = line.index("(") + 1
        end = len(line) - 2
        plus = line.index("+")

        newString = "OUTPUT " + line[start:plus] + ", " + line[(plus + 1) : end] + "\n"

    # only 1 string is being outputed
    elif '"' in line and not ("+" in line):
        start = line.index('"')
        end = len(line) - 2

        newString = "OUTPUT " + line[start:end] + "\n"

    # only one variable is being outputed
    else:
        start = line.index("(") + 1
        end = len(line) - 2

        newString = "OUTPUT " + line[start:end] + "\n"

    return newString


def ConvertAssignment(line):
    return line.replace("=", "<-")

