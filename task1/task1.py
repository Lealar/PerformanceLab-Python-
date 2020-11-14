def itoBase(nb, base):
    answer = []
    dictionary = dict()
    for i in range(len(base)):
        dictionary[str(i)] = str(base[i])   #Создание словаря числовое значение:ключ из ввода
    baza = len(base)        #определение системы исчесления
    while nb >= baza:
        answer.append(dictionary.get(str(nb % baza)))   #добавление ключа из словаря в список ответов
        nb = nb // baza                 #целочисленное деление
        if nb < baza:
            answer.append(dictionary.get(str(nb)))  #Добавление последнего числа, не проитерированного
    answer.reverse()    #переворачиваем список для правильной послежовательности ответа
    for i in range(len(answer)):
        print(answer[i], end='')    #вывод ответа
    print()

print(
    "Введите два числа для конвертации из десятичной системы исчисления в любую другую. \n"
    "Для выхода из программы введите 'stop'\n"
    "Первое число - подаваемое число, второе - система исчисления \n"
    "Пример ввода: 32 01\n"
    "(Пример ввода системы исчесления:  «01» - двоичная, «012» - троичная, \n"
    "«0123456789abcdef» - шеснадцатиричная, «котики» - система исчисления в котиках)")

while True:
    input_ = input().split(' ')
    if 'stop' in input_[0]:
        print("Программа закончила работу.")
        break
    else:
        try:
            itoBase(int(input_[0]), list(str(input_[1])))
        except :
            print("Usage")
            continue
