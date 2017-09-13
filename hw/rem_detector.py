#seiesmic
import ast
from matplotlib import pyplot
import numpy as np
from scipy.signal import butter, lfilter, freqz

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=1):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

freq = 10
file = open("/home/mohammed/dreamlab/hw/logs/2017-05-18_090005_10.eog","r")
content=file.read()
content+=']'
lis=ast.literal_eval(content)
print str(len(lis)) + ' reads for '+str(len(lis)/(60*freq)) + ' minutes' 
lis=butter_lowpass_filter(lis,5.0,10.0)
# print str(len(lis)) + ' reads for '+str(len(lis)/(60*100)) + ' minutes' 
summ = 0
num = 0
last = 0
c = 1
values=[]
one_minute = 60*freq
five_minutes = 5*60*freq
i = 0
while i < len(lis)-five_minutes:
    for reading in lis[i:i+five_minutes]:
        diference = abs(reading - last)
        last = reading
        summ+=diference
        num+=1
        if num == five_minutes:
            avg = summ / num
            print c,avg
            values.append(avg)
            summ = 0
            num = 0
            c += 1
    i+=one_minute
    
pyplot.plot(values)
pyplot.xlabel('Minutes')
pyplot.ylabel('Avg Differences')
pyplot.xticks(range(1,70,10))
pyplot.show()
