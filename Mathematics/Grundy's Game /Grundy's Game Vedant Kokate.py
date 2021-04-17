# def mex(l):
#     d={}
#     for i in l:d[i]=0
#     for i in range(10**6+2):
#         if i not in d:
#             return i

# dp=[0,0,0]
# for i in range(3,10000):
#     l=[]
#     for j in range(1,i):
#         if i-j<=j:
#             break
#         l.append(dp[j]^dp[i-j])
#     dp.append(mex(l))
# print(dp.count(0))
# ans=[]
# for i in range(10000):
#     if dp[i]==0:
#         ans.append(i)
# print(ans)
ans=[1, 2, 4, 7, 10, 20, 23, 26, 50, 53, 270, 273, 276, 282, 285, 288, 316, 334, 337, 340, 346, 359, 362, 365, 386, 389, 392, 566, 630, 633, 636, 639, 673, 676, 682, 685, 923, 926, 929, 932, 1222]
ans=set(ans)
for _ in range(int(input())):
    n=int(input())
    if n in ans:
        print('second')
    else:print('first')