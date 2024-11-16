import re
file=open("academifile.txt")
data=file.read()
print(data)
pattern="credit - (\\d+)\npoint - (\\d+.\\d+)"
info=re.findall(pattern,data)
print(data)
cr=0
er=0
for i in info:
    cr+=(int(i[0])*float(i[1]))
    er+=int(i[0])
print("cgpa: ",end=" ")
print(cr/er)
file.close()