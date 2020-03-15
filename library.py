indentationLevel = 0
elseFlag = False
count = 0
ifLocation = []

loops = []
endif = False
previous = 0
lineNum = 0

def ParseLine(line):
    global elseFlag
    global ifLocation
    global previous

    if elseFlag:
        line = " " * (indentationLevel + 4) + line
    else:
        line = " " * indentationLevel + line

    newS = AddLoopEnd(line, previous)
    previous = 0
    for l in line:
        if l != ' ':
            break
        previous += 1

    if "print" in line:
        # produce output pseudocode
        newS += ConvertPrint(line)
    elif "input" in line and not ("print" in line):
        newS += ConvertInput(line)
    elif line.count("=") == 1 and not ("input") in line and not "while" in line and not "if" in line:
        newS += ConvertAssignment(line)
    elif 'if' in line or 'else' in line:
        # Case if statement\
        newS += ConvertIf(line)
    elif 'for' in line:
        newS += ConvertForLoop(line)
    elif 'while' in line:
        newS += ConvertWhileLoop(line)
    else:
        return line
    if elseFlag:
        global count
        count += 1
        if count == 2:
            newS += " " * ifLocation.pop() + "ENDIF" + "\n"
            elseFlag = False
            count = 0

    
    return newS




def ConvertInput(line):
    newString = ""
    indent = line.count('   ') * '    '

    # if the input has a prompt
    if line.count('"') > 0:
        start = line.index('"')
        end = line.index(')')

        newString += indent + "OUTPUT " + line[start:end] + "\n"

    end = line.index("=") - 1
    start = line.count('    ') * 4
    variable = line[start:end]

    newString += indent + "INPUT " + variable + "\n"
    
    newString += ConvertType(line, variable)
    
    return newString




def ConvertType(line, variable):
    
    if 'int' in line:
        return variable + ' <- ' + 'STRING_TO_NUM(' + variable + ')\n'
    elif 'str' in line:
        return variable + ' <- ' + 'NUM_TO_STRING(' + variable + ')\n'
    else:
        return ''




def ConvertPrint(line):
    line = line.replace("+", ", ")
    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace("print", "OUTPUT ")
    
    return line



def ConvertAssignment(line):
    
    line = line.replace('=', '<-')
    line = line.replace('%', ' MOD ')
    line = line.replace('int', 'STRING_TO_NUM')
    line = line.replace('str', 'INT_TO_STRING')
    
    return line




def ConvertForLoop(line):

    line = line.replace('for', 'FOR')
    line = line.replace('in', '<-')
    line = line.replace(',', ' TO ')
    line = line.replace('range(', '')
    line = line.replace('):', '')

    # if a step is given
    if line.count('TO') != 1:
        line = line.replace('TO', 'STEP')
        line = line.replace('STEP', 'TO', 1)

    loops.append('ENDFOR')
    return line



def ConvertWhileLoop(line):

    line = line.replace('while', 'WHILE')
    line = line.replace(':', ' DO')
    line = line.replace(' == ', '=')
    line = line.replace('!=', '<>')
    line = line.replace('%', ' MOD ')

    line = line.replace('and', 'AND')
    line = line.replace('or', 'OR')
    line = line.replace('not', 'NOT')
    
    loops.append('ENDWHILE')
    return line



def ConvertIf(line):
    global ifLocation
    global indentationLevel
    global endif
    if "if" in line and not "elif" in line:
        endif = True    
        line = line.replace("if", "IF")
        line = line.replace("==", "=")
        spaces = 4
        for char in line:
            if char != " ": 
                break
            spaces += 1
        indentationLevel += 4
        replaced = "\n" + " " * spaces + "THEN"
        line = line.replace(":", replaced)
        ifLocation.append(line.index("IF"))
    elif "else" in line:
        indentationLevel -= 8
        line = line.replace("else", "ELSE")
        replaced = " " * indentationLevel
        line = line.replace(":", replaced)
        global elseFlag
        elseFlag = True
        indentationLevel += 4
        endif = False
    return line




def AddLoopEnd(line, previous):
    global endif

    spaces = 0
    for l in line:
        if l != ' ':
            break
        spaces += 1

    if endif == False and len(loops) != 0:
            
            if (spaces < previous):
                val = loops[-1] + '\n'
                loops.pop()
                return val

    return ''