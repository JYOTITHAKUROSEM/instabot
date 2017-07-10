# from pylab import *
# ax =axes([0.1,0.1,0.8,0.8])
# labels='frogs','hogs','DOGS','LOGS'
# fraces=(15,30,45,10)
# explode=(0,0.5,0,0)
# pie(fraces,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
# show()
from pylab import *
ax =axes([0.1,0.1,0.8,0.8])
labels='Reaading','Teaching','Writing','Flower'
fraces=(15,20,45,10)
explode=(0,0.5,0,0)
pie(fraces,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
show()