from flask import Flask, render_template
import glob,ast

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
