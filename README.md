# ИЗ 1
> На вход программы подаются прописные латинские буквы, ввод этих символов
> заканчивается точкой. Напишите эффективную по времени работы и по используемой
> памяти программу, которая будет определять, можно ли переставить эти буквы так, чтобы
> получился палиндром (палиндром читается одинаково слева направо и справа налево).
> Программа должна вывести ответ «Да» или «Нет», а в случае ответа «Да» – еще и сам
> полученный палиндром (первый в алфавитном порядке).
> Пример входной строки:
>   GAANN.
> Пример выходных данных:
>   Да
>   ANGNA

Результат

      Введите латинскую букву: a
      Введите латинскую букву: a
      Введите латинскую букву: b
      Введите латинскую букву: b
      Введите латинскую букву: c
      Введите латинскую букву: .
      Да
      abcba

- [X]  Ввод символов с клавиатуры, создание списка из перестановок(между данными символами), проверка на палиндром
- [ ] Проверка на существование палиндрома на заданных символах
