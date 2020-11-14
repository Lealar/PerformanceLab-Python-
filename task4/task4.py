import re


def comparison(strring, pattern):
    if '*' in pattern:
        patternChek = re.sub(r"\*", r".*", pattern) #решение с помощью регулярных выражений
    if re.fullmatch(patternChek, strring):
        return print('«' + strring + "» " + '«' + pattern + "» " '-OK')
    else:
        return print('«' + strring + "» " + '«' + pattern + "» " '-KO')


print("Программа, которая сравнивает 2 строки одинаковые ли они.\n"
      "Результат: вывод «ОК»,если строки идентичны, «КО», если не идентичны\n"
      "Для выхода из программы введите 'stop'")
while True:
    strring = input().split()
    if "stop" in strring:
        print("Программа закончила работу")
        break
    else:
        try:
            comparison(strring[0], strring[1])
        except:
            print("Некорректный ввод. \n "
                  "Пример работы программы:«аааа» «аааа» - ОК ")
            continue
