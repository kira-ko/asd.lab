Задача 2. Сортировка вставкой с отслеживанием индексов
================================
Описание:
--------------------------------
В данной задаче реализуется алгоритм сортировки вставками с отслеживанием индексов перемещения элементов. Алгоритм осуществляет сортировку путем перебора элементов массива слева направо, и при этом, размещает каждый следующий элемент таким образом, чтобы он оказался на правильной позиции между ближайшими элементами с минимальным и максимальным значением. Но также алгоритм возвращает индексы позиций элементов.

Формат входных данных:
------------------------------
* входные файлы находяться в файле input.txt
* в первой строке входного файла содержиться число n (1 <= n <= 10**3) - число элементов массива
* во второй строке находяться n различных целых чисел, по модулю не превосходящих 10**9

Формат выходных данных:
--------------------
* выходные данные находяться в файле output.txt
* первая строка - индексы позиций элементов после сортировки
* вторая строка - отсортированный массив

  
Ограничения:
--------
* ограничение по времени. 2 сек.
* ограничение по памяти. 256 мб

Структура проекта:
-------
* task2/ - папка со всеми файлами для задачи
* src/ - исходный код программы
    * input.txt - файл с входными данными
    * output.txt - файл с выходными данными
* tests/ - тестирование алгоритма

Код задачи:
---------
```
"""Задание 2. Сортировка вставкой +"""
def insertion_sort(list_arr):
    index_result = [1]
    for i in range(1, len(list_arr)):
        for j in range(i - 1, -1, -1):
            if list_arr[i] < list_arr[j]:
                list_arr[i], list_arr[j] = list_arr[j], list_arr[i]
                i, j = j, i
        index_result.append(i + 1)
    return index_result, list_arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, mas = f.readlines()
    ind, array = insertion_sort(list(map(int, mas.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, ind))), file=f)
        print(' '.join(list(map(str, array))), file=f)
```

Запуск проекта
--------
1. перейдите в директорию src
2. вставте корректные данные в файл input.txt (или убедитесь что он содержит корректные данные)
3. запустите скрипт ```python isertion_sort_index.py```
4. результат выполнения кода будет в файле output.txt

Тестирование
----------
для проверки работы алгоритма выполняються тесты, находящиеся в директории tests в файле insertion_sort_index_test

```
import unittest

from lab1.task2.src.insertion_sort_index import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_index(self):
        ind, arr = insertion_sort([1, 8, 4, 2, 3, 7, 5, 6, 9, 0])
        self.assertEqual(arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(ind, [1, 2, 2, 2, 3, 5, 5, 6, 9, 1])


if __name__ == '__main__':
    unittest.main()
```

