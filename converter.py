from functions import *

filepath = input("Enter python filepath: ")
writepath = input("Enter write filepath: ")
file = open(filepath, "r")
writefile = open(writepath, "w")

for line in file.readlines():
    val = ParseLine(line)
    writefile.write(val)

if len(loops) != 0:
    writefile.write(loops.pop())  
file.close()
