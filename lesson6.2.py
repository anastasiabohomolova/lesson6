lst = [132, 434, 432, '343', '454']

def func(x):
    return x, int(x) if isinstance(x, str) else str(x)
    



list_1 = list(map(func, lst))
print(list_1)


    
