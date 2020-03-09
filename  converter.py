# import only the necessary io things later on
import io
from library import *


file = open("Input_Data/test 2.py", "r")
writefile = open("Generated_Output_Data/gen_test 2.txt", "w")


for line in file.readlines():
    val = ParseLine(line)
    writefile.write(val)

file.close()

# sample = 'print("Please input your team name")'
# sample2 = 'print("Hello "+name)'
# sample3 = "print(message+team_name)"
# sample4 = 'message = "Congratulations "'
# sample5 = "correct = False"


# print(ConvertInput("team_name = input()"))
# print(ConvertInput('name = input("Please input your name")'))

# print("input" in sample and not ("print" in sample))
# print(ConvertPrint(sample))
# print(ConvertPrint(sample2))
# print(ConvertPrint(sample3))

# print(ConvertAssignment(sample4))
# print(ConvertAssignment(sample5))
