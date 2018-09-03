# -*- coding: utf-8 -*-

# Обновление:
# Решил, что добавлять локации прямо в код не есть правильно,
# поэтому решил создать отдельный текстовый файл, в котором
# они будут храниться. Теперь можно просто прописать новую
# локацию в текстовом файле 'locations.txt' и она появится в игре.

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
for loc in open_file.readlines():
    locations.append(loc.strip())

# Количество зомби на каждую локацию.
zombies = [2, 5, 8, 10]

print "Квестовая игра: Зомбиапокалипсис"
print "Как играть: Вводишь цифру соответствующего пункта и нажимаешь ENTER."

print "  *** ИГРА НАЧАЛАСЬ ***"

print "Город наполнен живыми мертвецами, тебе нужно передвигаться по локациям и убивать их."

all_zombies = sum(zombies)

while all_zombies > 0:
    print 20*"-"
    print "Выберите локацию:"
    number_location = 1
    for i in locations:
        print "  %d. %s" % (number_location, i)
        number_location += 1
    action = raw_input(" -> ")
    if action == "1":
        zombies[0] = change_location(locations[0], zombies[0])
    elif action == "2":
        zombies[1] = change_location(locations[1], zombies[1])
    elif action == "3":
        zombies[2] = change_location(locations[2], zombies[2])
    elif action == "4":
        zombies[3] = change_location(locations[3], zombies[3])
    else:
        print "--- Неверная команда. ---"
    print "Всего зомби:", sum(zombies)
    all_zombies = sum(zombies)

print ""
print "Ты прошел все три локации."
print "*** КОНЕЦ ИГРЫ ***"
