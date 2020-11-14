import csv
import re


def dataChek(timeSet):
    timeSet = str(timeSet[0:19])
    timeStart = str(timeInput[0])
    timeFinish = str(timeInput[1])
    if timeStart <= timeSet <= timeFinish:
        return True
    else:
        return False


def top_up(stringFill, volume):
    zalivaem = re.findall(r'\d+', stringFill[0])
    zalivaem = int(zalivaem[0])
    global VolumeKeg
    global KolichestvoVodiNalito
    global KolichestvoVodiHeNalito
    global KolichestvoOshibok
    if zalivaem + VolumeKeg <= volume:
        VolumeKeg += zalivaem
        KolichestvoVodiNalito += zalivaem
    elif zalivaem + VolumeKeg > volume:
        KolichestvoVodiHeNalito += zalivaem
        KolichestvoOshibok += 1


def scoop(stringFill, volume):
    zabiraem = re.findall(r'\d+', stringFill[0])
    zabiraem = int(zabiraem[0])
    global VolumeKeg
    global KolichestvoHeZabor
    global KolichestvoZabor
    global KolichestvoOshibok
    if VolumeKeg - zabiraem < 0:
        KolichestvoHeZabor += zabiraem
        KolichestvoOshibok += 1
    elif VolumeKeg - zabiraem >= 0:
        VolumeKeg -= zabiraem
        KolichestvoZabor += zabiraem


time = input().split(' ')
timeInput = time[1:3]
KolichestvoPopitok, KolichestvoOshibok, KolichestvoVodiNalito, KolichestvoVodiHeNalito = 0, 0, 0, 0
KolichestvoZabor, KolichestvoHeZabor = 0, 0

with open(time[0], 'r', encoding="utf-8") as log:
    volume = log.readline()
    while re.fullmatch(r'\D*', volume):
        volume = log.readline().rstrip()  # максимальный объем бочки
    volume = int(volume)
    VolumeKeg = int(log.readline().rstrip())  # текущий объем бочки
    FinishVolumeKeg = VolumeKeg
    for line in log:
        workLine = line.rstrip()
        if not (re.fullmatch(r'\d+.\d\d.\d\d.\d\d.\d\d.\d\d.+[wanna].+\d+.', workLine)):
            print(workLine)
            print("USAGE")
            break
        if dataChek(workLine):  # проверка на вхождение в заданную дату
            KolichestvoPopitok += 1
            if "top up" in workLine:
                top_up(re.findall(r'top up.*', workLine), volume)
            elif 'scoop' in workLine:
                scoop(re.findall(r'wanna.*', workLine), volume)

with open('output.csv', 'w', encoding='UTF-8') as file:
    questions = [
        ["- какое количество попыток налить воду в бочку было за указанный период? - ", KolichestvoPopitok],
        ["- какой процент ошибок был допущен за указанный период? - ", round((KolichestvoOshibok / KolichestvoPopitok * 100),2)],
        ["- какой объем воды был налит в бочку за указанный период? - ", KolichestvoVodiNalito],
        ["- какой объем воды был не налит в бочку за указанный период? - ", KolichestvoVodiHeNalito],
        ["- какой объем воды забрали из бочки за указанный период? -", KolichestvoZabor],
        ["- какой объем воды не забрали из бочки за указанный период? - ", KolichestvoHeZabor],
        ['- объем воды в бочке в начале указанного периода', FinishVolumeKeg],
        ["- объем воды в бочке в конце указанного периода", VolumeKeg]]

    writer = csv.writer(file)
    for fow in questions:
        writer.writerow(fow)
