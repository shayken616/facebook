import os,sys

u = raw_input("raymond rivera: ")
fn = raw_input("raymond: ")
ln = raw_input("rivera: ")
bm = raw_input("august: ")
bd = raw_input("23: ")
by = raw_input("1984: ")
pn = raw_input("0966371429#: ")
a = raw_input("37: ")
c = raw_input("custom fav: ")
n = raw_input("nickname: ")
stdoutOrigin=sys.stdout
sys.stdout = open("password.txt", "w")
print(fn + bd)
print(fn + bm + bd)
print(fn + bm + bd + by)
print(u + bm)
print(u + bm + bd)
print(ln + bd)
print(ln + bm + bd)
print(ln + bm + bd + by)
print(fn + a)
print(ln + a)
print(n + bd)
print(n + bm + bd)
print(n + bm + bd + by)
print(n + a)
print(c + a)
print(c + bd)
print(c + bm)
print(c + bm + bd)
print(c + bm + bd + by)
sys.stdout.close()
sys.stdout=stdoutOrigin










