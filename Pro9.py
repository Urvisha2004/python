# write a program to split text into words to form sentences from one file to another file  split()
#python Pro9.py first.txt second.txt 
import sys
ffile=open(sys.argv[1],'r')
sfile=open(sys.argv[2],'w')
s=ffile.read()
print(s)
words=s.split()
sentence = ' '.join(words)
sfile.write(sentence)
ffile.close()
sfile.close()