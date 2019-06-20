i = 1+1
print(i)

sum_10=0
for j in range(1,11):
    sum_10=j+sum_10
print(sum_10)

sum_100=0
for j in range(1,101):
    sum_100=j+sum_100
print(sum_100)

#累加函数
def plus(x):
    sum_x=0
    for j in range(1,x+1):
        sum_x=j+sum_x
    print(sum_x)

plus(10)
plus(100)
