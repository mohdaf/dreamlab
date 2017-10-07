import sys
file = open(sys.argv[1],"r") # The input File
eog_file = open(sys.argv[2],"w") # The Output file
signal_index=int(sys.argv[3]) # The signal index
eog_file.write('[')
for line in file:
    eog_file.write(line.split(',')[signal_index]+',')