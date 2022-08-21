N=1
K=0
list=[]
while  K < 1000:
    K = (N ** 2 + 1) / N
    print (K)
    list.append(N)
    N = N + 1
    print (len (list)) 