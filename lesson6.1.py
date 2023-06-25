lst_r = [123, 344, 434, '343', '4']
lst_n = list(map(lambda a: a == int if a == str(a) else str(a), lst_r))  #int(a) if a == str else str(a) if a == int else int(a), lst_r))
lst_n_2 = list(map(lambda a: a == str if a == int(a) else int(a), lst_r))

print(lst_n)
print(lst_n_2)

