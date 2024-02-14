
SEP = "*"
HEADER = "ShipName*planet*coord_place*direction"


def calc_coords(n, m, t, xd, yd):
    """Функция для восстановления координат корабля(x, y) по данным из его названия и кол-ва букв в родной планете

    Описание аргументов:
    n - первая цифра в номере корабля, int
    m - вторая цифра в номере корабля, int
    t - кол-во букв в родной планете корабля, int

    """

    if n > 5:
        x = n + xd
    else:
        x = -(n + xd) * 4 + t

    if m > 3:
        y = m + t + yd
    else:
        y = -(n + yd) * m

    return x, y


# Чтение файла в список строк
with open("space.txt", encoding="utf-8") as fd:
    data = fd.readlines()

data = data[1:]  # убираем хэдер
# разбиваем каждую строку по сепаратору, указанному в глобальных константах
data = [i.strip().split(SEP) for i in data]

with open("space_new.txt", "w", encoding="utf-8") as fd:
    print(HEADER, file=fd) # записываем хэдер в файл результат
    for row in data:
        if row[-2] == "0 0": # если координаты корабля нулевые, то восстанавливаем их по известным данным
            ship_id = int(row[0].split("-")[1][0])
            ship_id_ = int(row[0].split("-")[1][1])
            t = len(row[1])
            xd_, xy_ = row[-1].split(" ")
            x_, y_ = calc_coords(ship_id, ship_id_, t, int(xd_), int(xy_))
            # Заменяем нулевые координаты на восстановленные
            row[-2] = f"{x_} {y_}"
        
        print(SEP.join(row), file=fd) # Записываем строку в файл

        if row[0].split("-")[0][-1] == "V": # Если название корабля заканчивается на V
            coords = row[-2].split(" ")
            print(f"{row[0]} - ({coords[0]}, {coords[1]})")
