import sys,ast
file = open(sys.argv[1],"r") # The input File
eog_file = open(sys.argv[2],"w") # The Output file
FREQ_Fraction=int(sys.argv[3]) # The frequency fraction
content=file.read()
content+=']'
lis=ast.literal_eval(content)
counter = 1
for line in lis:
    if counter%FREQ_Fraction == 0:
        eog_file.write(str(line)+',')
    counter+=1
