# -*- coding: utf-8 -*-

# Обновление:
# Отныне локации хранятся в базе данных, а не в txt файле

# импортирую библиотеку для работы с базой данных
import sqlite3

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

# Подключаюсь к Базе данных и выгружаю все данные из таблицы locations
connection = sqlite3.connect('base.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM locations")
rows = cursor.fetchall()

# выгруженные данные из таблицы locations дабавляю в пустые массивы
locations = []
zombies = []
for row in rows:
    loc = row[0]
    zom = row[1]
    locations.append(loc)
    zombies.append(zom)

print "Квестовая игра: Зомбиапокалипсис"
print "Как играть: Вводишь цифру соответствующего пункта и нажимаешь ENTER."
print "  *** ИГРА НАЧАЛАСЬ ***"
print "Город наполнен живыми мертвецами, тебе нужно передвигаться по локациям и убивать их."

# цикл, который не дает игре завершиться, пока не умрут все зомби
while sum(zombies) > 0:
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
    print "Всего зомби в городе:", sum(zombies)

print ""
print "В городе больше нет живых мертвецов."
print "*** КОНЕЦ ИГРЫ ***"
