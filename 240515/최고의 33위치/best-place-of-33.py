n =  int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

grid = 3
max_cnt = 0
for i in range(n-2):
    # if i+3 > n: break
    for j in range(n-2):
        # if j+3 > n: continue
        cnt = 0
        for k in range(i, i+3):
            for l in range(j, j+3):
                if arr[k][l] == 1:
                    cnt += 1
        
        max_cnt = max(max_cnt, cnt)

print(max_cnt)