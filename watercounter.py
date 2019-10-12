import os
import shutil


def Start():
    print("----------- Water Counter 1.0 -----------")
    choice1 = input("Доступно:\n1. Создать новый месяц\n2. Посмотреть кол-во выпитой воды\n3. Добавить данные о кол-во выпитой воды\n4. Удалить информацию\nВыбор: ")

    if choice1 == "1":
        os.system('cls')
        def addnewinfo():
            month = input("Введите название месяца: ")

            addMonth = open('inf\\count.txt', 'a')
            addMonth.write(month + '\n')
            addMonth.close()

            fileName = month + '.txt'
            addNewBaza = open("inf\\" + fileName, 'w')
            addNewBaza.write("")
            addNewBaza.close()

            os.system('cls')

            
        addnewinfo();
    elif choice1 == "2":
        os.system('cls')
        print("Доступно: \n")
        if os.path.exists("inf\\count.txt"):
            readBaza = open('inf\\count.txt', 'r')
            readLine = readBaza.readline()
            while readLine:
                print(readLine)
                readLine = readBaza.readline()
            readBaza.close()
            inputName = input("\nВыберите месяц: ")
            os.system('cls')
            fileName = inputName + '.txt'
            openFile = open("inf\\" + fileName, 'r')
            print("Месяц: " + inputName)
            i=0
            for line in openFile.readlines():
                i
                i+=1
                print(line)
            openFile.close()
            choice12 = input("Для продолжения нажмите Enter...")
            os.system('cls')
        else:
            os.system('cls')
            input("Вы еще не добавили ни одного отчета!\n Для продолжения нажмите Enter...")
            os.system('cls')
            return
    elif choice1 == "4":
        if os.path.exists("inf"):
            shutil.rmtree("inf")
            os.mkdir("inf")
        else:
            os.mkdir("inf")
        os.system('cls')
    elif choice1 == "3":
        nameMonth = input("Введите название месяца: ")

        fileName = nameMonth + '.txt'
        if os.path.exists("inf\\" + fileName): 
            def addnewcan(fileName):
                waterCount = []
                os.system('cls')
                time = input("Введите время и дату (01.01.1991 \ 00:00): ")
                waterCount = input("Введите кол-во выпитой воды: ")

                baza = time + " - " + waterCount + '\n'
                changeNewBaza = open("inf\\" + fileName, 'a')
                changeNewBaza.write(baza)
                changeNewBaza.close()
            addnewcan(fileName)
            os.system('cls')
        else:
            os.system('cls')
            input("Вы еще не создали отчет за этот месяц!\nДля продолжения нажмите Enter...")
            os.system('cls')
            return
    else:
        os.system('cls')
        return

while True:
    if os.path.exists("inf"):
        Start()
    else:
        os.mkdir("inf")
        Start()
