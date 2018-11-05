text_1 = "Bu cümlede 4 elma 5 armut 8 tane de muz var"
text_2 = 'bu ikinci cümlede 9 kiraz 3 karpuz var'

a=text_1.replace("Bu" ,"")
b=a.replace("cümlede" , "")
c=b.replace("elma" , "")
d=c.replace("armut" , "")
e=d.replace("tane" , "")
f=e.replace("de" , "")
g=f.replace("muz" , "")
h=g.replace("var" , "")
i=h.replace(" ", "")

x = int(i)

m=text_2.replace("bu" , "")
k=m.replace("ikinci" , "")
l=k.replace("cümlede" , "")
o=l.replace("kiraz" , "")
n=o.replace("karpuz" , "")
v=n.replace("var" , "")
t=v.replace(" " , "")

y = int(t)

print(x)
print(y)
print(x + y)


