Задача 5. Представитель большинства
================================
Описание:
--------------------------------
В данной задаче реализуется алгоритм для нахождения элемента, который встречается более чем n/2 раз в массиве (элемент большинства). 


Формат входных данных:
------------------------------
* входные файлы находяться в файле input.txt
* в первой строке входного файла содержиться число n (1 <= n <= 10**5) - число элементов массива
* во второй строке находяться n различных положительных целых чисел, по модулю не превосходящих 10**9

Формат выходных данных:
--------------------
* выходные данные находяться в файле output.txt
* данные файл должен содержать одну строку с отсортированным массивом. между любыми двумя числами должен стоять ровно один пробел

Ограничения:
--------
* ограничение по времени. 2 сек.
* ограничение по памяти. 256 мб

Структура проекта:
-------
* task5/ - папка со всеми файлами для задачи
* src/ - исходный код программы
    * input.txt - файл с входными данными
    * output.txt - файл с выходными данными
* tests/ - тестирование алгоритма

Запуск проекта
----
1. перейдите в директорию src
2. вставте корректные данные в файл input.txt (или убедитесь что он содержит корректные данные)
3. запустите скрипт ```majority_element.py```
4. результат выполнения кода будет в файле output.txt
