# -*- coding: utf-8 -*-

# Вместо статических данных сделал отдельные переменные для локаций

nl = "Национальная Библиотека"
br = "ТЦ Беркат"
gp = "ТРЦ Гранд-Парк"

print "Квестовая игра: Зомбиапокалипсис"
print "Правила просты: Вводишь цифру соответствующего пункта и нажимаешь ENTER"

print "*** ИГРА НАЧАЛАСЬ ***"

print "Город наполнен живыми мертвецами, тебе нужно передвигаться по локациям и убивать их."

print "Ты находишься в локации" , nl
print "Перед тобой 2 зомби. Твои действия?"
choice = raw_input("1. Убить их.\n2. Перейти в следующую локацию.\n -> ")
if choice == "1":
    print "Ты убил 2 зомби и очистил локацию."
else:
    print "Ты сменил локацию"

print "*** СМЕНА ЛОКАЦИИ ***"

print "Ты находишься в локации" , br
print "Перед тобой 5 зомби. Твои действия?"
choice = raw_input("1. Убить их.\n2. Перейти в следующую локацию.\n -> ")
if choice == "1":
    print "Ты убил 5 зомби и очистил локацию."
else:
    print "Ты сменил локацию"
    
print "*** СМЕНА ЛОКАЦИИ ***"

print "Ты находишься в локации" , gp
print "Перед тобой 8 зомби. Твои действия?"
choice = raw_input("1. Убить их.\n2. Перейти в следующую локацию.\n -> ")
if choice == "1":
    print "Ты убил 8 зомби и очистил локацию."
else:
    print "Больше нет локаций"

print ""
print "Ты прошел все три локации."
print "*** КОНЕЦ ИГРЫ ***"
