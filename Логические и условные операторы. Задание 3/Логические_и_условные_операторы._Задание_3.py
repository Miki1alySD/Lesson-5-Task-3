summa=int(input("Минимальная сумма для инвестиций - "))
Michel = int(input("Сумма для инвестиции на счету у Майкла - "))
Ivan = int(input("Сумма для инвестиции на счету у Ивана - "))

if (Michel>=summa) and (Ivan>=summa):
    print(2)
elif (Michel>=summa) and (Ivan<=summa):
    print("Michel")
elif (Michel<=summa) and (Ivan>=summa):
    print("Ivan")

elif (Michel<=summa) and (Ivan<=summa) and ((Michel+Ivan)>=summa):
    print(1)
elif (Michel<=summa) and (Ivan<=summa) and ((Michel+Ivan)<=summa):
    print(0)