import sys
import time
questions = []
questions.append({"q": "Это - полупроводниковый прибор, который может выполнять функцию ключа или усилителя.", "a": "транзистор", "h": "У него есть эмиттер, коллектор, и база. Или затвор, сток и исток."})
questions.append({"q": "Это - электронный компонент, способный накапливать заряд.", "a": "конденсатор", "h": "Бывает электролитический, керамический, трубчатый и плоскостной."})
questions.append({"q": "Это - электронный компонент, увеличивающий сопротивление цепи.", "a": "резистор", "h": "Измеряется в Омах."})
questions.append({"q": "Это - полупроводниковый прибор, излучающий свет.", "a": "светодиод", "h": "Проводит ток в одну сторону"})
questions.append({"q": "Это - электронный компонент, изменяющий сопротивление в зависимости от интенсивности света.", "a": "фоторезистор", "h": "****резистор"})
questions.append({"q": "Это - полупроводниковый прибор, проводящий ток только в одном направлении.", "a": "диод", "h": "Обозначается на схемах как \"VD\"."})
questions.append({"q": "Это - электронный компонент, который при нажатии производит замыкание цепи.", "a": "кнопка", "h": "Бывает тактовая."})
questions.append({"q": "Это - источник питания для схем.", "a": "батарейка", "h": "Бывает AA, AAA, D, Крона и другие."})
questions.append({"q": "Это - прибор, переводящий электрическую энергию во вращательную механическую.", "a": "электромотор", "h": "Он же вращается."})
questions.append({"q": "Это - электронный компонент, который замыкает цепь, при перемещении его бегунка в противоположную сторону.", "a": "выключатель", "h": "Есть у каждого по несколько штук (а то и по 15) дома"})
questions.append({"q": "Это - электронный компонент, который производит механическое замыкание цепи под действием магнитного поля.", "a": "геркон", "h": "герметизированный магнитоуправляемый контакт"})
questions.append({"q": "Это - разновидность звукоизлучающего устройства.", "a": "пьезоизлучатель", "h": "В основе его работы лежит пьезоэффект."})
questions.append({"q": "Это - переменный резистор изменяющий сопротивление перемещением ползунка.", "a": "реостат", "h": "Сейчас чаще называется потенциометром."})
questions.append({"q": "Это - перезаряжаемый источник питания для схем.", "a": "аккумулятор", "h": "Бывает Li-Ion, Li-Pol, металл гибридный."})
questions.append({"q": "Это - полупроводниковый прибор, изменяющий свою проводимость в зависимости от света.", "a": "фотодиод", "h": "****диод"})
questions.append({"q": "Это - электронный компонент, состоящий из множества транзисторов.", "a": "интегральная схема", "h": "Может быть в корпусе DIP."})
questions.append({"q": "Это - искусственный источник света, в котором свет испускает тело накала, нагреваемое электрическим током до высокой температуры.", "a": "лампа", "h": "Бывает накаливания, электросберегающая."})
questions.append({"q": "Это - разновидность звукоизлучающего устройства.", "a": "динамик", "h": "Состоит из мембраны, и магнитной катушки."})
questions.append({"q": "Это - электронный компонент, состоящий из миллионов транзисторов.", "a": "процессор", "h": "Вставляется в сокет."})
questions.append({"q": "Это - винтовая, спиральная или винтоспиральная катушка из свёрнутого изолированного проводника, обладающая значительной индуктивностью при относительно малой ёмкости и малом активном сопротивлении.", "a": "дроссель", "h": ""})

import random
import string
import os
import pathlib

def maskLetters(word, knownLetters):
    r = "";
    for s in word:
        if knownLetters.find(s) >=0:
            r = r + s
        else:
            r = r + "*"
    return r



i = random.randint(1, len(questions))
word = questions[i - 1]["a"]
questions.remove(i-1)
print(questions[i-1]["q"])
letters = ""
life = 5

while 1:
    print("Слово: " + maskLetters(word, letters + "\n"))
    l = input("Введи букву: ")
    
    if word.find(l) >= 0:
        letters += l
        if maskLetters(word, letters).find("*") < 0:
            print("Вы отгадали слово " + word + "!")
            if len(questions)==0:
                print("Викторина окончена!")
                break
            b=input("Повторить?[Д/н]\n")
            if b == "Д" or b == "д" or b == "":
                i = random.randint(1, len(questions))
                word = questions[i - 1]["a"]
                questions.remove(i-1)
                print(questions[i-1]["q"])
                letters = ""
                life = 5
            else:
                break
    else:
        life = life -1
        if life == 3:
            print(questions[i-1]["h"])
        if life == 0:
            print("Вы НЕ отгадали слово " + word)
            break
            
        else:
            w = ""
            for i in range(life):
                w = w + "♡"
            print(w)
    