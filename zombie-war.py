# -*- coding: utf-8 -*-

# Обновление:
# Наконец-то смог решить проблему добавления локаций.
# Отныне не нужно в коде прописывать ни локацию, ни количество зомби.
# Теперь можно добавить локацию и количество зомби в
# файле 'locations.txt'.


def change_location(location, count_zombie):
    print "Ты находишься в локации" , location
    if count_zombie > 0:
        while count_zombie > 0:
            print "Перед тобой %d зомби. Твои действия?" % count_zombie
            print "  1. Убить зомби."
            print "  2. Перейти в следующую локацию."
            choice = raw_input(" -> ")
            if choice == "1":
                count_zombie = count_zombie - 1
                print "Ты убил 1 зомби."
                print "Теперь в этой локации %d зомби." % count_zombie
            elif choice == "2":
                print "  *** СМЕНА ЛОКАЦИИ ***"
                break
            else:
                print "--- Неверная команда. ---"
    else:
        print "--- В этой локации нет зомби. ---"
    return count_zombie


# Создаю пустой массив для локаций
locations = []

# Открываю текстовый файл 'locations.txt'.
open_file = open('locations.txt', 'r')

# Выгружаю все локации из файла 'locations.txt'
# и помещаю эти локации в пустой массив 'locations[]'.
for loc in open_file:
    loc = loc[:-4]
    loc = loc.strip('=')
    locations.append(loc.strip())


# Создаю пустой массив для количества зомби на каждую локацию
zombies = []

# Открываю текстовый файл 'locations.txt'.
open_file = open('locations.txt', 'r')

# Выгружаю все локации из файла 'locations.txt'
# и помещаю эти локации в пустой массив 'zombies[]'.
for zom in open_file:
    zom = zom[-3:-1]
    zom = zom.strip('=')
    zombies.append(int(zom))


print "Квестовая игра: Зомбиапокалипсис"
print "Как играть: Вводишь цифру соответствующего пункта и нажимаешь ENTER."

print "  *** ИГРА НАЧАЛАСЬ ***"

print "Город наполнен живыми мертвецами, тебе нужно передвигаться по локациям и убивать их."


all_zombies = sum(zombies)

# цикл, который не дает игре завершиться, пока не умрут все зомби
while all_zombies > 0:
    print 20*"-"
    print "Выбери локацию:"
    number_location = 1
    # цикл, который выводит все локации
    for i in locations:
        print "  %d. %s" % (number_location, i)
        number_location += 1
    action = raw_input(" -> ")
    if action >= "1" and action <= str(len(locations)):
        action = int(action) - 1
        zombies[action] = change_location(locations[action], zombies[action])
    else:
        print "--- Неверная команда. ---"
    print "Всего зомби:", sum(zombies)
    all_zombies = sum(zombies)


print ""
print "Ты прошел все три локации."
print "*** КОНЕЦ ИГРЫ ***"
