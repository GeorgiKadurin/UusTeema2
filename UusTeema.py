from класс1 import*

est_words = loe_failist('est.txt')
rus_words = loe_failist('rus.txt')


#text_est = loe_failist('est.txt')
#text_rus = loe_failist('rus.txt')


while True:
           print("1-Перевод с эстонского языка на русский")
           print("2-Перевод с русского языка на эстонский")
           print("3-Добавте слово в словарь")
           print("4-Можете исправить ошибку в слове")
           print("5-Проверка знания слов")
           print("6-Закончить работу")
           v=int(input("Выберите действие: "))
           if v==1:
                  est_word = input('Введите слово на эстонском: ')
                  rus_word = est_to_rus(est_word, est_words, rus_words)
           if rus_word:
                print('Перевод:', rus_word)
           else:
                print('Слово не найдено в словаре.')









                #print("Перевод слова с эстонского языка на русский")
                #t_est = input('Введите слово на эстонском: ')
                #t_ru = text_est_in_text_rus(t_est, text_est, text_ru)
                #if t_ru:
                #   print('Перевод:', text_ru)
                #else:
                #    print("Слова нету в списке")
          

           #elif v==2:
           #     print()

           #elif v==3:
           #     print()

           #elif v==4:
           #     print()

           #elif v==5:
           #     print()

           #else:
           #     print("Конец")
           #     break

















#from класс1 import*
#laused=["Tere tulemast"]

#while True:
#    v=int(input("1-loeme failist\n2-salvestame failisse\n3-tekstit kõne\n"))

#    if v==1:
#        laused=loe_failist("laused.txt")
#        for line in laused:
#            print(line)

#    elif v==2:
#        line=input("lisa lause: ")
#        laused.append(line)
#        kirjuta_failist("laused.txt", laused)

#    elif v==3:
#        text=""
#        for line in laused:
#            text=text+" "+line
#            Heli(text,"et")#text:köik elemendis järjendis
#            ind=int(input("Number: "))#üks element indeksiga ind
#            Heli(laused[ind],"et")







#from класс1 import*


#nimi = input("Sisestage oma nimi:  ")
#number = number(nimi)
#print(f"Teie nime number: {number}")

