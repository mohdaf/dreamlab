import sys,ast
filename=sys.argv[1]
FREQ=int(filename.split('.')[0].split('_')[2])
file = open(filename,'r')
content=file.read()
content+=']'
lis=ast.literal_eval(content)
print str(len(lis)) + ' reads for '+str(len(lis)/(60*FREQ)) + ' minutes' 
