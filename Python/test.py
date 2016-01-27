import ajplanet
from numpy import pi,arange

t = 2 * 30.433 * arange(10)/999

v0 = 0
K = 968.6
w = 189.1 * pi / 180.
e = 0.5170
t0 = 0.0
P = 5.633

K=1000.0
w=0
e=0
t0=0
P=1
t=arange(11)/10.
print t

for i in range(10):
    y = ajplanet.pl_rv(t[i], v0, K, w, e, t0, P)
    print y

res = ajplanet.pl_rv_array(t,v0, K, w, e, t0, P)
print res
