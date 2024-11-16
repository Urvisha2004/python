#replace() use write a program find and replace all the occurrence of a word ...
#python Pro10.py first.txt
import sys
myfile = open(sys.argv[1], 'r') 
for line in myfile:
    replacecontent = line.replace('good', 'better')
    myfile=open(sys.argv[1],'w')
    myfile.write(replacecontent)
    #print(modecontent, file=myfile, end='')
myfile.close()