import random
from re import finditer
# импорт библиотек для случайного числа и регулярного выражения
def gallows(theme):
    word = ""
    num_word = random.randint(1, 5)
    death = 11
    answer = []
    for words in theme:
        if words == num_word:
            word = theme.get(words)
            print("Длина слова = " + str(len(list(word))))
            #если ключ словаря = случ.числу, то берём его значение для игры
    while death > 0:
        print("Введите букву")
        letter = input()
        if letter in word:
            answer.append(letter)
            numbers_letter = [m.start() for m in finditer(letter, word)]
            for i in numbers_letter:
                i = i + 1
                print("Порядковый номер буквы: " + str(i))
            #если в слове есть буква, то добавляем её в список ответа, выводим порядковый номер
        else:
            print("Такой буквы нет в слове")
            death = death - 1
            #если буквы нет в слове, уменьшаем счётчик смертей
        if sorted(set(answer)) == sorted(set(word)):
            print("Вы выиграли. Загаданное слово - " + word)
            break
        # в случае победы - сверяем множество "ответов" и множ-во загаданного слова
    else:
        print("Вы проиграли. попробуйте ещё раз.")

print("Выберите тему.Введите число (1 - Спорт, 2 - География, 3 - Развлечения, 4 - Программирование )")
choice = int(input())
while choice not in range(0, 5):
    print("Тема не найдена. \n Введите число (1 - Спорт, 2 - География, 3 - Развлечения, 4 - Программирование ")
    choice = int(input())
# проверка на правильно введённое число
sport = {1: "лыжи", 2: "гандбол", 3: "атлетика", 4: "гребля", 5: "шахматы"}
georaphy = {1: "вулкан", 2: "море", 3: "алебастр", 4: "рельеф", 5: "ландшафт"}
games = {1: "квест", 2: "бильярд", 3: "боулинг", 4: "дайвинг", 5: "рыбалка"}
develop = {1: "проектирование", 2: "архитектура", 3: "итерация", 4: "запрос", 5: "прокрастинация"}
# далее - выбор темы для загаданного слова
if choice == 1:
    gallows(sport)
elif choice == 2:
    gallows(georaphy)
elif choice == 3:
    gallows(games)
else:
    gallows(develop)
