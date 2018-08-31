# -*- coding: utf-8 -*-

# Переменные, содержащие локации, перевел в массив (список)
# Написал функцию, чтоб убрать дублирование

def first_function(location, count_zombie):
    print "Ты находишься в локации" , location
    while count_zombie > 0:
        print "Перед тобой %d зомби. Твои действия?" % count_zombie
        choice = raw_input("1. Убить зомби.\n2. Перейти в следующую локацию.\n -> ")
        if choice == "1":
            count_zombie = count_zombie - 1
            print "Ты убил 1 зомби."
            print "Теперь в этой локации %d зомби." % count_zombie
        else:
            print "Ты не можешь сменить локацию, пока не убьешь всех зомби"

    print "*** СМЕНА ЛОКАЦИИ ***"

locations = ["Национальная Библиотека",
             "ТЦ Беркат",
             "ТРЦ Гранд-Парк"]

print locations[0]

count = [2, 5, 8]

print "Квестовая игра: Зомбиапокалипсис"
print "Правила просты: Вводишь цифру соответствующего пункта и нажимаешь ENTER"

print "*** ИГРА НАЧАЛАСЬ ***"

print "Город наполнен живыми мертвецами, тебе нужно передвигаться по локациям и убивать их."

first_function(locations[0], count[0])
first_function(locations[1], count[1])
first_function(locations[2], count[2])

print ""
print "Ты прошел все три локации."
print "*** КОНЕЦ ИГРЫ ***"
