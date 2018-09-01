# -*- coding: utf-8 -*-

# Изменил функцию first_function на change_location.
# Также добавил еще цикл while в функцию change_location.
# Теперь есть возможность смены локации, даже если игрок не убил всех зомби.
# Игра работает замечательно, но есть много вложенностей if-ов и while-ов

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
            else:
                print "  *** СМЕНА ЛОКАЦИИ ***"
                break
    else:
        print "--- В этой локации нет зомби. ---"
    return count_zombie
        
locations = ["Национальная Библиотека",
             "ТЦ Беркат",
             "ТРЦ Гранд-Парк"]

zombies = [2, 5, 8]

print "Квестовая игра: Зомбиапокалипсис"
print "Как играть: Вводишь цифру соответствующего пункта и нажимаешь ENTER."

print "  *** ИГРА НАЧАЛАСЬ ***"

print "Город наполнен живыми мертвецами, тебе нужно передвигаться по локациям и убивать их."

all_zombies = zombies[0] + zombies[1] + zombies[2]

while all_zombies > 0:
    print "Выберите локацию:"
    print "  1.", locations[0]
    print "  2.", locations[1]
    print "  3.", locations[2]
    action = raw_input(" -> ")
    if action == "1":
        zombies[0] = change_location(locations[0], zombies[0])
    elif action == "2":
        zombies[1] = change_location(locations[1], zombies[1])
    elif action == "3":
        zombies[2] = change_location(locations[2], zombies[2])
    all_zombies = zombies[0] + zombies[1] + zombies[2]

print ""
print "Ты прошел все три локации."
print "*** КОНЕЦ ИГРЫ ***"
