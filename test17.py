print('введите строку')
stroka=input()
spisok=[]
i=0
tet=stroka.split(' ')

while i<len(tet):
     spisok.append(int(tet[i]))
     i=i+1


def sort (array):
 for i in range(len(array)):  # проходим по всему массиву
     idx_min = i  # сохраняем индекс предположительно минимального элемента
     for j in range(i, len(array)):
          if array[j] < array[idx_min]:
               idx_min = j
     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
          array[i], array[idx_min] = array[idx_min], array[i]
 return array


spisok2 = sort(spisok)
print('отсортированный список')
print(spisok2)


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

print('введите число')
element = int(input())
array = spisok2

if element<array[0] or element>array[len(array)-1]: print('ваше число за пределами списка')
else: print('искомый индекс ',binary_search(array, element, 0, len(array)-1))