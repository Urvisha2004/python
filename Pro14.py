import re
pera = "hello student (91)-079-40016326 mt pincode number is 360311 and my ip address is 192.168.2.200 and student come in date 01/07/2024 your website name id another contact number is.. 99899 88988 "
m1 = r'\(\d{2}\)-\d{3}-\d{8}'
m2=r'3\d{4}1'
m3=r'\d{3}\.\d{3}\.\d{1}\.\d{3}'
m4=r'\d\d/\d\d/\d\d'
m5=r'\d{5}\s\d{5}'
findr = re.findall(m1,pera)
finda = re.findall(m2,pera)
findb = re.findall(m3,pera)
findc=re.findall(m4,pera)
findd=re.findall(m5,pera)
print(findr)
print(finda)
print(findb)
print(findc)
print(findd)
