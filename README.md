Лабораторная работа №10

Разработка и отладка алгоритмов содержащих функции, модули и пакеты

Цели и задачи

· Создать пакет collision для работы с прямоугольниками
· Реализовать функции для проверки корректности, пересечения и вычисления площадей
· Научиться вызывать пользовательские исключения
· Создать главный файл с примерами использования

Структура проекта

ipo-lr-10/
├── collision/           # Пакет с функциями
│   └── __init__.py     # Все функции находятся здесь
├── main.py             # Главный файл с примерами
└── README.md           # Этот файл
Функции пакета collision

1. isCorrectRect(rect) - Проверяет, корректно ли задан прямоугольник. Принимает список из двух кортежей: [(x1,y1), (x2,y2)]. Возвращает True, если x1 < x2 и y1 < y2, иначе False.
2. isCollisionRect(rect1, rect2) - Проверяет, пересекаются ли два прямоугольника. Если любой прямоугольник некорректен, вызывает исключение RectCorrectError.
3. intersectionAreaRect(rect1, rect2) - Вычисляет площадь пересечения двух прямоугольников. Возвращает 0, если прямоугольники не пересекаются.
4. intersectionAreaMultiRect(rectangles) - Вычисляет площадь пересечения нескольких прямоугольников. Принимает список прямоугольников.
5. RectCorrectError - Пользовательское исключение, вызывается при некорректном прямоугольнике.

Примеры использования

from collision import *

# 1. Проверка корректности
print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  # True
print(isCorrectRect([(-7, 9), (3, 6)]))       # False

# 2. Проверка пересечения
rect1 = [(-3.4, 1), (9.2, 10)]
rect2 = [(-7.4, 0), (13.2, 12)]
print(isCollisionRect(rect1, rect2))  # True

# 3. Площадь пересечения
area = intersectionAreaRect(rect1, rect2)
print(f"Площадь: {area:.2f}")

# 4. Несколько прямоугольников
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)]
]
area_multi = intersectionAreaMultiRect(rectangles)
print(f"Общая площадь: {area_multi:.2f}")

# 5. Обработка ошибок
try:
    bad_rect = [(3, 17), (13, 1)]  # Некорректный!
    isCollisionRect(rect1, bad_rect)
except RectCorrectError as e:
    print(f"Ошибка: {e}")
Как запустить

1. Клонируйте репозиторий
2. Запустите файл main.py:

python main.py
История коммитов

· Task 2 complete - создана функция isCorrectRect
· Task 3 complete - создана функция isCollisionRect
· Task 4 complete - создана функция intersectionAreaRect
· Task 5 complete - создана функция intersectionAreaMultiRect
· Task 6 complete - создан главный файл main.py

