list = [2, 4, 3, 0, 6, 7]
global n
n = 4
def search(list, n):
    for i in range(n):
        i += 1
        if i > n:
            print('Found it')
        else: print('Not here')
search(list, n)
