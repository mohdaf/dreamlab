from flask import Flask, render_template
import glob,ast
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


app = Flask(__name__)

@app.route('/logs')
def logs():
    files= glob.glob("/var/www/dreamlab/hw/logs/*.eog")
    logs=[]
    files.sort()
    for filepath in files:
        filename=filepath.split('/')[-1]
        details=filename.split('_')
        dt=details[0]+' '+details[1][:2]+':'+details[1][2:4]+':'+details[1][4:6]
        freq=int(details[2].split('.')[0])
        file = open(filepath,"r")
        content=file.read()
        content+=']'
        lis=ast.literal_eval(content)
        seconds=len(lis)/freq
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        duration= "%d:%02d:%02d" % (h, m, s)
        logs.append((filename,dt,str(freq),str(len(lis)),duration))
    return render_template('logs.html', logs=logs)



@app.route('/log/<name>')
def log(name):
    filepath="/var/www/dreamlab/hw/logs/"+name
    file = open(filepath,"r")
    content=file.read()
    content+=']'
    log=ast.literal_eval(content)
    details=name.split('_')
    dt=details[0]+' '+details[1][:2]+':'+details[1][2:4]+':'+details[1][4:6]
    freq=int(details[2].split('.')[0])
    return render_template('log.html', log=log,freq=freq,date=dt)

@app.route('/analysis/<name>')
def analysis(name):
    filepath="/var/www/dreamlab/hw/logs/"+name
    file = open(filepath,"r")
    content=file.read()
    content+=']'
    log=ast.literal_eval(content)
    log=butter_lowpass_filter(log,5.0,10.0)
    details=name.split('_')
    dt=details[0]+' '+details[1][:2]+':'+details[1][2:4]+':'+details[1][4:6]
    freq=int(details[2].split('.')[0])
    summ = 0
    num = 0
    last = 0
    c = 1
    values=[]
    one_minute = 60*freq
    five_minutes = 5*60*freq
    i = 0
    while i < len(log)-five_minutes:
        for reading in log[i:i+five_minutes]:
            diference = abs(reading - last)
            last = reading
            summ+=diference
            num+=1
            if num == five_minutes:
                avg = summ / num
                values.append(avg)
                summ = 0
                num = 0
                c += 1
        i+=one_minute
    return render_template('analysis.html', values=values,freq=freq,date=dt)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
