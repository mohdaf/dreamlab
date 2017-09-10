file = open("/home/mohammed/dreamlab/hw/sc4012e0_data.txt","r")
eog_file = open("/home/mohammed/dreamlab/hw/sc4012e0_data_EOG.txt","w")

for line in file:
    eog_file.write(line.split(',')[3]+',')
