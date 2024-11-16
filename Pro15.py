import re
s = "hello i am urvisha and my email address is aa@g my age is 20 and a.gvp@gmail.com and aa@gmail.com and a-b@gujaratvidhyapith.org this also gujaratvidhyapith id in your assing strings."
pattern = r'\w+@\w'
pattern2= r'\w+@[\w+\.]+\w'
pattern3= r'[-\w]+@[\w\.-]+\w+'
result=re.findall(pattern,s)
result3=re.findall(pattern2,s)
result4=re.findall(pattern3,s)
print(result)
print(result3)
print(result4)