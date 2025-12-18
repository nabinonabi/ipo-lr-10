# Импортируем всё из нашего пакета
from collision import *

# Пример 1: Проверка прямоугольника
print("1. Проверка прямоугольника:")
rect1 = [(-3.4, 1), (9.2, 10)]
rect2 = [(-7, 9), (3, 6)]
print(f"   {rect1} - {isCorrectRect(rect1)}")  # True
print(f"   {rect2} - {isCorrectRect(rect2)}")  # False

# Пример 2: Проверка пересечения
print("\n2. Проверка пересечения:")
a = [(-3.4, 1), (9.2, 10)]
b = [(-7.4, 0), (13.2, 12)]
c = [(1, 1), (2, 2)]
d = [(3, 0), (13, 1)]
print(f"   {a} и {b} - {isCollisionRect(a, b)}")  # True
print(f"   {c} и {d} - {isCollisionRect(c, d)}")  # False

# Пример 3: Площадь пересечения
print("\n3. Площадь пересечения:")
print(f"   {a} и {b} = {intersectionAreaRect(a, b):.2f}")
print(f"   {c} и {d} = {intersectionAreaRect(c, d):.2f}")

# Пример 4: Несколько прямоугольников
print("\n4. Несколько прямоугольников:")
rects = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)]
]
print(f"   3 прямоугольника: {intersectionAreaMultiRect(rects):.2f}")

# Пример 5: Ошибка
print("\n5. Проверка ошибки:")
bad = [(3, 17), (13, 1)]  # Неправильный!
try:
    isCollisionRect(c, bad)
except RectCorrectError as e:
    print(f"   Ошибка: {e}")

print("\n Работает!")
