x = 95
y = 2
s = 0
r = 0
i = 1

for y in range(1, 10):
    for x in range(1, 100):

        x2 = 100 #仮の値
        s2 = 101 # 仮の値

        r = x % y
        s = x // y

        x = str(x)

        x1 = int(x[-1])
        if int(x) >= 10:
            x2 = int(x[-2])

        s = str(s)

        s1 = int(s[-1])
        if int(s) >= 10:
            s2 = int(s[-2])

        if x1!=x2 and x1!=y and x1!=s1 and x1!=s2 and x1!=r and x2!=y and x2!=s1 and x2!=s2 and x2!=r and y!=s1 and y!=s2 and y!=r and s1!=s2 and s1!=r and s2!=r:
            print(int(x),y, s, r)


