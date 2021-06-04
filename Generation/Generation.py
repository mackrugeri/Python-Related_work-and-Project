#coding:utf-8
g = 0
i = 0
j = 0
k = 0
l = 0
n = 0
m = 0
T = []
U = []
V = []
o = 0
r = 0
W1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
W2 = []
X = []
A = [0,1,0,1,0,1,0,1]
B = [0,0,1,1,0,0,1,1]
C = [0,0,0,0,1,1,1,1]
print("specifie the rule number")
num = int(input())
print(num)
for i in range(0,256,1):
    U.append(0)
while (num > 0) :
    print("-----------------------------")
    print(num)
    module = num % 2
    num = int(num / 2)
    print(num)
    print(module)
    if 0 < module < 2 :
        print(1)
        T.append(1)
        print(T)
    else :
        print(0)
        T.append(0)
        print(T)
reversed_list = T[::-1]
print("The list T is",len(T)) 
print(reversed_list)
"""reversed(T)"""
if len(T) < 8 :
    for j in range(len(T),8,1) :
        T.append(0)

print("The length of T is",len(T))
for o in range(0,len(T),1) :
    print(T[o], C[o],B[o],A[o])
for g in range(0,21,1):
    X = []
    W2.append(W1[len(W1)-1])
    for m in range(0,len(W1),1):
        W2.append(W1[m])
    W2.append(W1[0])
    print(W2)
    #print("-----------------------------")
    #print("gen2")
    for k in range(1,len(W1)+1,1):
        #print("k = ", k)
        for l in range(0,8,1):
            #print("l = ", l)
            if ( W2[k] == B[l] and W2[k-1] == A[l] and W2[k+1] == C[l] ):
                #print("recived")
                X.append(T[l])
    print(len(X))
    W1 = []
    W2 = []
    for m in range(0,len(X),1):
        W1.append(X[m])
    g = g + 1