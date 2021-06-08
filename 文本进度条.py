from time import*
p=perf_counter()
scale=50
print("执行开始".center(scale//2,"="))
for i in range(scale+1):
    a='*' * i
    b='-' * (scale-i)
    c=(i/scale)*100
    l=perf_counter()-p
    print("\r","{:^3.0f}%[{}->{}]{:.2f}秒".format(c,a,b,l),end="")
    time,sleep(0.1)
print("\n{:=^20}".format("执行结束"))
n=perf_counter()
print("{:.2f}s".format(n-p))
