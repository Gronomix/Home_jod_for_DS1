#a = 7

#b = 3.8

#c = 'Hello'

#a_id = id(a)

#print(a, b, c)
#print(type(a), type(b),type(c))
#print(f'Заданные числа', id(b), id(a), id(c))

#a = "hello"

#a_id2 = id(a)
#print(a, id(a_id2))

#print(a_id == a_id2)

h = input(f'введите целое число  ')

if h == int:
    print(f'Ввел целое число красава')
else:
    input(f'пробуй снова  ')
    if h != int:
        print(h)

ls = [3, 7, 6, 7, 9, 22, 66]

del ls[3]
print(ls)