SEP = "*"
HEADER = "ShipName*planet*coord_place*direction"
RES_HEADER = "ShipName;planet;coord_place;direction;password"
RES_SEP = ";"


def password_gen(ship_name, planet):
    """Функция генерации пароля

    Описание аргументов:
    ship_name - названия корбля, строка
    planet - название планеты, строка
    
    """

    return (planet[-3:-1] + planet[-1] + ship_name[2] + ship_name[1] + planet[:3][::-1]).upper()


with open("space.txt", encoding="utf-8") as fd:
    data = fd.readlines()

data = data[1:]
data = [i.strip().split(SEP) for i in data]

with open("space_uniq_password.csv", "w", encoding="utf-8") as fd:
    print(RES_HEADER, file=fd)
    for row in data:
        password = password_gen(row[0], row[1])
        print(f"{RES_SEP.join(row)}{RES_SEP}{password}", file=fd)
