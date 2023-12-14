import json

def addPhone(dph):
    phnName = input("Введите имя -> ")
    phnNum = input("Введите номер телефона -> ")
    dph[phnName] = dph.get(phnName, []) + [phnNum]

def delPhone(dph):
    phnName = input("Введите имя -> ")
    dph.pop(phnName, None)

def changePhone(dph):
    phnName = input("Введите имя -> ")
    phnNumOld = input("Введите старый номер телефон -> ")
    phnNumNew = input("Введите новый номер телефона -> ")
    dph[phnName] = [phnNumNew if x == phnNumOld else x for x in dph[phnName] ]
    

def printPhone(dph):
    for key in dph:
        print(f"{key} - {" ".join(dph[key])}")

def savePhone(dph):
    phnJson = json.dumps(dph)
    with open("phoneBook.json", "w") as my_file:
        my_file.write(phnJson)

def exitProgramm(dph):
    exit(0)

dCommand = {'1' : [printPhone, "Просмотр справочника"],
            '2' : [addPhone, "Добавить значение"],
            '3' : [delPhone, "Удалить значение"],
            '4' : [changePhone, "Изменить номер телефона"],
            '6' : [savePhone, "Сохранить"],
            '7' : [exitProgramm, "Выход"]}


print('Приложение телефонный справочник:')

for key in dCommand:
    print(f"{key} - {dCommand[key][1]}")

dPhone = {}
with open("phoneBook.json", "r") as my_file:
        phnJson = my_file.read()
dPhone = json.loads(phnJson)

while True:
    numCmd = input("Введите действие ")
    comfunc=dCommand.get(numCmd)
    if (comfunc):
        comfunc[0](dPhone)
    else:
        print("Команда указана не корректно")    
