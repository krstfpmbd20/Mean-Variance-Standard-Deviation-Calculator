#Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')

#Set .intersection() Operation
n = int(input())
english = set(input().split())
b = int(input())
french = input().split()
print(len(english.intersection(french)))

#Set .difference() Operation
e = int(input())
english = set(input().split())
f = int(input())
french = input().split()
print(len(english.difference(french)))

#Set .symmetric_difference() Operation
e = int(input())
english = set(input().split())
f = int(input())
french = input().split()
print(len(english.symmetric_difference(french)))

#Set Mutations
n = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd, num = input().split()
    if(cmd == "intersection_update"):
        A.intersection_update([*map(int, input().split())])
    elif(cmd == "update"):
        A.update([*map(int, input().split())])
    elif(cmd == "difference_update"):
        A.difference_update([*map(int, input().split())])
    else:
        A.symmetric_difference_update([*map(int, input().split())])
print(sum(A))

#The Captain's Room
from collections import defaultdict

dd = defaultdict(int)
mem = int(input())
ll = list(map(int,input().split()))
for v in ll:
    if v in dd.keys():
        dd[v]=dd[v]+1
    else:
        dd[v]=1

for k,v in dd.items():
    if v==1:
        print(k)

#Check Subset
T = int(input())

for i in range(T):
    a = int(input())
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    
    print(A.issubset(B))

#Check Strict Superset
A = set(input().split())
n = int(input())
for i in range(n):
    s = set(input().split())
    
    if(len(s) == len(A)):
        print(False)
        break
    elif(not A.issuperset(s)):
        print(False)
        break
else:
    print(True)

#Exceptions
T = int(input().strip())
for i in range(T):
    try:
        a, b = input().strip().split()
        result = int(int(a) / int(b))
    except ZeroDivisionError as e:
        print(f"Error Code: integer division or modulo by zero")
    except ValueError as ve:
        print(f"Error Code: {ve}")
    else:
        print(result)

