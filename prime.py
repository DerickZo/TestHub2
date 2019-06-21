"""
#打印100以内的质数
#质数：大于等于2，只能被自身和1整除
#思路：列举10以内的质数，这一组质数都不能整除的数，就是质数

for i in range(2,100):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i)
"""

"""
思路2：
设 n 为整数，n >= 2；
若 n == 2，n 是质数；
若 n > 2，就把 n 作为被除数，从 2 开始一直到 n - 1 都作为除数，逐一计算看看余数是否等于 0？
如果是，那就不用接着算了，它不是质数；
如果全部都试过了，余数都不是 0，那么它是质数。
""" 
for i in range(2,100):
    if i == 2:
        print(i)
    else:
         for  n in range(2,i):
            if i % n == 0 :
                 break
            elif n == (i-1) :
                print(i)
print("done")
print("is sync now?")
print("try again!")
print("i get it!")
