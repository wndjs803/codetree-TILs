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
        if index > 1 and (arr[index-2] == i and arr[index-1] == i):
            continue 
        arr.append(i)
        recur(index+1)
        arr.pop()

recur(0)