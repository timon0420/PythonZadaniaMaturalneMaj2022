with open('zadania maturalne maj 2022\przyklad.txt', 'r') as f: txt = [x.rstrip() for x in f]
print('Zad1.',[x for x in txt if x[0] == x[-1]][0])
liczby = list(map(lambda x: int(x), txt))
lista = []
for i in liczby:
    txt = int(i)
    d = 2
    lst = []
    while txt != 1:
        if txt%d == 0:
            lst.append(d)
            txt = int(txt/d)
        else:
            d += 1
    lst.append(i)
    lista.append(lst)
print('Zad2.', max(lista, key=len)[-1], len(max(lista, key=len))-1)
x = list(max(list(map(lambda x: set(x), lista)), key=len))
print('Zad2.', x[-1], len(x)-1)