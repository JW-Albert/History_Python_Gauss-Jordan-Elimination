import numpy as np
import sys

# 未知數數量設為 3 個(x ,y ,z)
n = 3

a = np.zeros((n,n+1))
x = np.zeros(n)

print('請依據足碼填入相應值：　')
a[0][0] ,a[0][1] ,a[0][2] ,a[0][3] = map(float ,input("(a10 ,a11 ,a12 ,常數項) : ").split(","))
a[1][0] ,a[1][1] ,a[1][2] ,a[1][3] = map(float ,input("(a20 ,a21 ,a22 ,常數項) : ").split(","))
a[2][0] ,a[2][1] ,a[2][2] ,a[2][3] = map(float ,input("(a30 ,a31 ,a32 ,常數項) : ").split(","))

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit("聯立出現無解或無限多組解")

    for j in range(n):
        if i != j:
            ratio = a[j][i] / a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]


for i in range(n):
    x[i] = a[i][n]/a[i][i]

print("求得 x, y, z 分別為")
print("x =" ,x[0])
print("y =" ,x[1])
print("z =" ,x[2])