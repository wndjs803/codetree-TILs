n, m = map(int, input().split())

arr = []

def print_arr():
    for i in arr:
        print(i, end=' ')
    print()

def recur(index):
    if index == m:
        print_arr()
        return

    for i in range(1, n+1):
        if i in arr:
            continue
        if index > 0 and arr[index-1] > i:
            continue
        arr.append(i)
        recur(index+1)
        arr.pop()

recur(0)