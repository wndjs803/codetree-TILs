k, n = map(int, input().split())

arr = []

def print_answer():
    for i in arr:
        print(i, end=' ')
    print()


def recur(index):
    if index == n:
        print_answer()
        return
    
    for i in range(1, k+1):
        if i > 2 and (arr[i-2] == i and arr[i-1] == i):
            continue 
        arr.append(i)
        recur(index+1)
        arr.pop()

recur(0)