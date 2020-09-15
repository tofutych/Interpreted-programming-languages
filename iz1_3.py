from itertools import permutations


def is_palindrome(word):
    return word == word[::-1]


letter = None
word = list()
while letter != '.':
    letter = input('Введите латинскую букву: ')
    word.append(letter)
word.remove('.')

words = list(map(lambda x: ''.join(x), list(permutations(word))))
words.sort()

flag = False
for word in words:
    if is_palindrome(word):
        flag = True
        print(f'Да\n{word}')
        break
if not flag:
    print('Нет\n')
