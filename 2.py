SEP = "*"
HEADER = "ShipName*planet*coord_place*direction"


def insertion_sort(arr):
    """Функция сортировки вставками. Принимает на вход весь датасет из файла space.txt (список списков)

    Описание аргументов:
    arr: датасет, список списков

    """

    for i in range(1, len(arr)):
        j = i - 1
        value = arr[i]
        while j >= 0 and int(arr[j][0].split("-")[1]) > int(value[0].split("-")[1]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value

    return arr


# Чтение файла в список строк
with open("space.txt", encoding="utf-8") as fd:
    data = fd.readlines()

data = data[1:]  # убираем хэдер
# разбиваем каждую строку по сепаратору, указанному в глобальных константах
data = [i.strip().split(SEP) for i in data]

# сортируем и выводим
sorted_ship = insertion_sort(data)
for i in range(0, 10):
    print(sorted_ship[i][0])
