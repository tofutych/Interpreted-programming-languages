# ИЗ 1

> На вход программы подаются прописные латинские буквы, ввод этих символов
> заканчивается точкой. Напишите эффективную по времени работы и по используемой
> памяти программу, которая будет определять, можно ли переставить эти буквы так, чтобы
> получился палиндром (палиндром читается одинаково слева направо и справа налево).
> Программа должна вывести ответ «Да» или «Нет», а в случае ответа «Да» – еще и сам
> полученный палиндром (первый в алфавитном порядке).
> Пример входной строки: GAANN.
> Пример выходных данных: Да ANGNA

Результат

      Введите латинскую букву: a
      Введите латинскую букву: a
      Введите латинскую букву: b
      Введите латинскую букву: b
      Введите латинскую букву: c
      Введите латинскую букву: .
      Да
      abcba

# ИЗ 2

> Дана база данных о продажах некоторого интернет-магазина. Каждая
> строка входного файла представляет собой запись вида Покупатель товар
> количество, где Покупатель — имя покупателя (строка без
> пробелов), товар — название товара (строка без пробелов), количество —
> количество приобретенных единиц товара.
> Создайте список всех покупателей, а для каждого покупателя
> подсчитайте количество приобретенных им единиц каждого вида товаров.
> Выведите список всех покупателей в лексикографическом порядке, после
> имени каждого покупателя выведите двоеточие, затем выведите список
> названий всех приобретенных данным покупателем товаров в
> лексикографическом порядке, после названия каждого товара выведите
> количество единиц товара, приобретенных данным покупателем. Информация
> о каждом товаре выводится в отдельной строке.

Результат

     input.txt                                                                      output.txt

     Adin cat 1                                                                     Adin:
     Ivanov paper 10                                                                cat 2
     Ruchkin marker 1                                                               Ivanov:
     Ruchkin lopata 666                                                             paper 17
     Petrov pen 5                                                                   marker 3
     Ivanov marker 3                                                                envelope 5
     Ivanov paper 7                                                                 Petrov:
     Petrov envelope 20                                                             pen 5
     Ivanov envelope 5                                                              envelope 20
     Ruchkin paper 10                                                               Ruchkin:
     Adin cat 1                                                                     marker 1
                                                                                    lopata 666
                                                                                    paper 10
