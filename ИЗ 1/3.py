def is_eng(char):
    return 64 < ord(char) < 91 or 94 < ord(char) < 123


letter = None
word = []

while True:
    letter = input('Введите латинскую букву: ')
    if len(letter) == 1 and is_eng(letter):
        word.append(letter)
    elif letter == '.':
        break
    else:
        print('Ошибка! Нужно вводить только букву латникого алфавита')

flag = True
palindrome = ''
d = {}
for letter in set(word):
    d[letter] = word.count(letter)

if len(word) % 2 == 0:
    for letter in set(word):
        d[letter] = word.count(letter)
        if word.count(letter) % 2 != 0:
            flag = False
    if flag:
        for letter in sorted(list(d.keys())):
            palindrome += letter * (d[letter] // 2)
        palindrome += palindrome[::-1]
else:
    counter = 0
    for item in d.keys():
        if d[item] > 1 and d[item] % 2 != 0:
            flag = False
        elif d[item] == 1:
            counter += 1
    if counter > 1:
        flag = False
    if flag:
        for letter in sorted(list(d.keys())):
            if d[letter] % 2 == 0:
                palindrome += letter * (d[letter] // 2)
            if d[letter] == 1:
                mid_char = letter
        palindrome += mid_char + palindrome[::-1]

if palindrome:
    print(f'Да\n{palindrome}')
else:
    print('Нет')
