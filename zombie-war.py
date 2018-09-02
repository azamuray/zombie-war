# -*- coding: utf-8 -*-

# Добавил еще одну локацию.
# Из-за этого пришлось поменять код в 5 местах.
# Это нужно как-то сократить.
# Я решил написать встроенную функцию 'sum(chars)', которая суммирует все числа массива.
# Теперь, если нужно добавить локацию, нужно код поменять лишь в 3 местах

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

locations = ["Национальная Библиотека",
             "ТЦ Беркат",
             "ТРЦ Гранд-Парк",
             "Башня Ахмат"]

zombies = [2, 5, 8, 10]

print "Квестовая игра: Зомбиапокалипсис"
print "Как играть: Вводишь цифру соответствующего пункта и нажимаешь ENTER."

print "  *** ИГРА НАЧАЛАСЬ ***"

print "Город наполнен живыми мертвецами, тебе нужно передвигаться по локациям и убивать их."

all_zombies = sum(zombies)

while all_zombies > 0:
    print 20*"-"
    print "Выберите локацию:"
    print "  1.", locations[0]
    print "  2.", locations[1]
    print "  3.", locations[2]
    print "  4.", locations[3]
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
