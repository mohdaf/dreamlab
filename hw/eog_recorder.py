import subprocess,time,sys
FREQ=sys.argv[1]
log = open('logs/' + time.strftime("%Y-%m-%d_%H%M%S") + '_' + FREQ + '.eog',"w")
subprocess.Popen(['python','adc.py',FREQ], stdout=log,stderr=log)
