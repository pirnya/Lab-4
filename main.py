items = [ ['r', 3, 25],
          ['p', 2, 15],
          ['a', 2, 15],
          ['m', 2, 20],
          ['i', 1, 5],
          ['k', 1, 15],
          ['x', 3, 20],
          ['t', 1, 25],
          ['f', 1, 15],
          ['d', 1, 10],
          ['s', 2, 20],
          ['c', 2, 20] ]

'''
#для примера
items = [ ['ш', 3, 700],
          ['т', 1, 300],
          ['с', 2, 500],
          ['к', 2, 550]]
'''

res_points=15 #итоговые очки выживания
inv=8 #инвентарь

#два листа, в которых мы перебираем ценность предметов
items_old= [0]*inv #8 мест
items_new= [0]*inv

#названия
names_old=['']*inv #вместе с res_new сохраняем названия
names_new=['']*inv #вместе с res_new сохраняем названия

#размер
capacity_old=[0]*inv
capacity_new=[0]*inv

for i in items:

    for slot_num in range(inv): #проходим от единичного размера инвентаря -> макс размера инвентаря
        if i[1]==slot_num+1: #этот предмет полностью занимает все ячейки
            if i[2] > items_old[slot_num]:
                items_new[slot_num]=i[2]
                names_new[slot_num]=i[0]
                capacity_new[slot_num]=i[1]

        if i[1]<slot_num+1: #этот предмет оставляет место
            if ( i[2] + items_old[slot_num - i[1]] ) > items_old[slot_num]:
                items_new[slot_num] = i[2] + items_old[slot_num - i[1]]
                names_new[slot_num] = i[0] + names_old[slot_num - i[1]]
                capacity_new[slot_num] = str(i[1])+str(capacity_old[slot_num - i[1]])

    #обновляем списки (проходим по новому предмету)
    items_old = items_new.copy()
    names_old = names_new.copy()
    capacity_old = capacity_new.copy()


result=[]
i=0
for i in range(len(capacity_old[-1])): #дублируем название предмета столько раз, сколько места он занимает
    for _ in range(int(capacity_old[-1][i])):
        result.append(names_old[-1][i])


i=0
for lenght in range(2): #выводим предметы (2x4 размер)
    for width in range(4):
        print(result[i], end=' ')
        i += 1
    print('')

summa=0
for i in items: #считаем сумму ценности всех предметов
    summa+=i[2]

print('Итоговые очки выживания:', items_old[-1] - (summa-items_old[-1]))

