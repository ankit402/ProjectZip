name1 = input("enter  name1")
name2 = input("enter name2")
concatenate = name1.lower() + name2.lower()
t = concatenate.count('t')
r = concatenate.count('r')
u = concatenate.count('u')
e = concatenate.count('e')

l = concatenate.count('l')
o = concatenate.count('o')
v = concatenate.count('v')
e = concatenate.count('e')

score =  t+r+u+e+l+o+v+e
score = int(score)
if score <10:
    print(f"your love  score is {score} and great ")
else :
    print(f"try  another partner name")
