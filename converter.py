from functions import *

file = open("/Users/yahyahusain/Desktop/SEACSTA/Input_Data/test 7.py", "r")
writefile = open("/Users/yahyahusain/Desktop/SEACSTA/Generated_Output_Data/example.txt", "w")


for line in file.readlines():
    val = ParseLine(line)
    writefile.write(val)

if len(loops) != 0:
    writefile.write(loops.pop())  
file.close()