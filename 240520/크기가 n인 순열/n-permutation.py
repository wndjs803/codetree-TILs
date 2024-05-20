n = int(input())

arr = []
visited = [False] * (n + 1) 

def print_arr():
    for i in arr:
        print(i, end=' ')
    print()

def recur(index):
    if index == n:
        print_arr()
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        arr.append(i)
        recur(index+1)

        arr.pop()
        visited[i] = False

recur(0)