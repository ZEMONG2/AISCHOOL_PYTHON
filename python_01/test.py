a = 10 / 3
print(id(a))
print(type(a))
print(type(10.5))
print(type("MBC"))
print(a)

b = """
aaa
bbb
ccc"""

print(b)

print("Hello Python!!")
print("Hello" + "Python!!")
print("Hello", "Python!!",sep="#")

print("%d * %d = %d" % (5,2,10))
print("%2d * %3d = %4d" % (5,2,10))
print("원주율은 %f 입니다" % 123.141592)
print("원주율은 %4.2f입니다." % 123.141592)
print("[%10d]" % 123)
print("[%-10d]" % 123)

print("이름은 {}입니다.".format("이기자"))
print("{1} 점수는 {0}점입니다. {0}점!".format(100, "수학"))
print("[{:>10}]".format("#"))
print("[{:<10}]".format("#"))
print("[{:<10.3f}]".format(123.456))
print("[{:15,}]".format(1234567890))

c = ["Mbc", "SBs", "Kbs"]
c.sort(key=str.upper, reverse=True)
print(c)

dat = [('john', 'C', 15),('ryan', 'A', 12),('dave', 'B', 17)]
dat.sort(key=lambda student: student[0], reverse=True)
print(dat)

a = [10, 10.5, "python"]
print(a)
print(a[0])
print(a[2])
print(a[2][0])
print(a[2][-1])
a[2] = "java"
print(a)

t = [1,2,3,4]
t.append(5)
print(t)

t.append([6,7])
print(t)

y = [4,1,2,3]
y.sort()
print(y)
y.reverse()
print(y)
print(y.index(1))