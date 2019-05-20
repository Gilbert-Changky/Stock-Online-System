price: 'time:data,time:data,time:,'
time: 'second' #传秒数，显示的时候导成时间，见群里链接
preferList: '[a,b,c,d]'
status: '0'/'1'


# 时间显示可以和秒数相互转化
import time

p = '2019-5-4-20-11-31'
timeTuple = time.strptime(p,"%Y-%m-%d-%H-%M-%S")
sec = time.mktime(timeTuple)



sec1 = 1556971891
n = time.ctime(sec)
comp = n.split(' ')
clock = comp[3].split(:)
p1 = '%s-%s-%s-%s-%s-%s-%s' %(str(comp[4]),)
[]