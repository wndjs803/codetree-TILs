k, n  = map(int, input().split())

index = 0
cur_num = 1
arr = []

def print_arr(arr):
    for i in arr:
        print(i, end=' ')
    print()

def recur(index):
    if index == n:
        print_arr(arr)
        return

    for i in range(1, k+1):
        arr.append(i)
        recur(index+1)
        arr.pop()

recur(index)