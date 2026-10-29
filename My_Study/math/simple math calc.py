from math import *

num, dat = int(input()), input()
def kv(): return num**2
def kb(): return num**3
def kr(): return num**0.5
def md(): return abs(num)
def sn(): return sin(num)
dic = {'квадрат': kv(),'куб': kb(),'корень': kr(),'модуль': md(), 'синус': sn}

print(dic[dat])
