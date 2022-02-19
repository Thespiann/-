#Άσκηση 7
xlist=[]
ylist=[]
zlist=[]
with open('dictionary.txt','r') as file:
    lines= file.readlines()
for line in lines:
    corr1=line.replace("{","")
    corr2=corr1.replace("}","")
    corr3=corr2.replace("\n","")
    corr4=corr3.replace('"','')
    line=corr4.split(",")

    xcorr=line[0].replace("x:","")
    xlist.append(xcorr)

    ycorr=line[1].replace("y:","")
    ylist.append(ycorr)

    zcorr=line[2].replace("z:","")
    zlist.append(zcorr)

xlist.sort()
xmax=xlist[-1]
xmin=xlist[0]
from collections import Counter
xs = Counter(xlist)
mostcommonx=xs.most_common(1)
if mostcommonx[0][1]==1:
    xcommon="All values are unique!"
else:
    xcommon=mostcommonx[0][0]

ylist.sort()
ymax=ylist[-1]
ymin=ylist[0]
from collections import Counter
ys = Counter(ylist)
mostcommony=ys.most_common(1)
if mostcommony[0][1]==1:
    ycommon="All values are unique!"
else:
    ycommon=mostcommony[0][0]

zlist.sort()
zmax=zlist[-1]
zmin=zlist[0]
from collections import Counter
zs = Counter(zlist)
mostcommonz=zs.most_common(1)
if mostcommonz[0][1]==1:
    zcommon="All values are unique!"
else:
    zcommon=mostcommonz[0][0]

key= input("My keys are x, y and z. Which one do you want? \n")

if key=="x" or key=="X":
    print("The key you gave me is x.\n The most common value of it is: "+xcommon+"\n The maximum value is: "+xmax+"\n The minimum value is: "+xmin+"\n Goodbye!")
if key=="y" or key=="Y":
    print("The key you gave me is y.\n The most common value of it is: "+ycommon+"\n The maximum value is: "+ymax+"\n The minimum value is: "+ymin+"\n Goodbye!")
if key=="z" or key=="Z":
    print("The key you gave me is z.\n The most common value of it is: "+zcommon+"\n The maximum value is: "+zmax+"\n The minimum value is: "+zmin+"\n Goodbye!")
if key!="x" and key!="X" and key!="y" and key!="Y" and key!="z" and key!="Z":
    print("Your key is incorrect! Better luck next time <3")
