#copy another file and read and write and print content ....
#python Pro8.py first.txt second.txt
import sys
ffile = open(sys.argv[1] , 'r')
print(ffile.read())
ffile.seek(0)#read kare tyare pointer end of file hoy at that time starting with read 
sfile = open(sys.argv[2] , 'w') 
i = 1 
for line in ffile:
    word = line.splitlines()
    for w in word:
        print(i, w, file=sfile)
        i = i + 1
ffile.close()
sfile.close()