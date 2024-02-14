SEP = "*"
HEADER = "ShipName*planet*coord_place*direction"


def hash_planet(name):
    """Функция для получения хэша строки, хэша названия планеты

    Описание аргументов:
    name - название планеты, строка

    """

    alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ -"
    p = 71
    m = 10 ** 9
    res_hash = 0
    power = 1
    for c in name:
        res_hash = (res_hash + alph.index(c) * power) % m
        power = (power * p) % m

    return int(res_hash)


def generate_hash_table(data):
    """Функция для генерации хэш-таблицы для всех планет,
        ключ - хэш названия планеты, строка
        значение - список названий кораблей(КОД-НОМЕР)

    Описание аргументов:
    data - весь распаршенный датасет из файла `space.txt`, список списков

    """

    hash_table = {}
    for row in data:
        planet_hash = hash_planet(row[1])
        if planet_hash not in hash_table:
            hash_table[planet_hash] = [row[0]]
        else:
            hash_table[planet_hash].append(row[0])

    return hash_table


def find_hashed(hash_table, planet):
    """Функция для поиска всех кораблей, которые запускались с заданной планеты

    Описание аргументов:
    hash_table - словарь, хэш таблица (описана в функции generate_hash_table)
    planet - название планеты, строка

    """

    hash_ = hash_planet(planet)
    if hash_ in hash_table:
        return hash_table[hash_]
    else:
        return []


def get_10_ships(hash_table):
    """Функция для получения первых 10-ти кораблей в формате:
        ключ (хэш названия планеты): номер(а) кораблей, которые взлетали с этой планеты

    Описание аргументов:
    hash_table - словарь, хэш таблица (описана в функции generate_hash_table)
    """

    found_ships = set()
    i = 0
    hash_table_keys = list(hash_table.keys())
    while len(found_ships) < 10:
        curr_key = hash_table_keys[i]
        ships = hash_table[curr_key]
        found_ships.update(ships)
        i += 1
        print(f"{curr_key}: {', '.join(ships)}")


# Чтение файла в список строк
with open("space.txt", encoding="utf-8") as fd:
    data = fd.readlines()

data = data[1:]  # убираем хэдер
# разбиваем каждую строку по сепаратору, указанному в глобальных константах
data = [i.strip().split(SEP) for i in data]
hash_table = generate_hash_table(data)  # генерируем хэш-таблицу

get_10_ships(hash_table)

# Test
# print(find_hashed(hash_table, "Ривенделл"))
