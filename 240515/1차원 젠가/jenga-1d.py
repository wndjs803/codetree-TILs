n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))


for i in range(2):
    start, end = map(int, input().split())
    temp = []

    for j in range(len(arr)):
        if j >= start-1 and j <=end-1:
            continue
        
        temp.append(arr[j])
    
    arr = temp

print(len(arr))

if arr:
    for i in arr:
        print(i)