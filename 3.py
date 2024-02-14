SEP = "*"
HEADER = "ShipName*planet*coord_place*direction"
NOT_FOUND_MSG = "error.. er.. ror.."

def search(data, name):
    """Функция поиска корабля в датасете по его названию.

    Описание аргументов:
    data: датасет из файла `space.txt`, список списков
    name: название корабля, строка
    
    """

    found = False
    for row in data:
        if row[0] == name:
            print(f"Корабль {name} был отправлен с планеты: {row[1]} и его направление движения было: {row[-1]}")
            found = True
            break
    if not found:
        print(NOT_FOUND_MSG)

with open("space.txt", encoding="utf-8") as fd:
    data = fd.readlines()

data = data[1:]
data = [i.strip().split(SEP) for i in data]

name = input()
while name != "stop":
    search(data, name)
    name = input()
