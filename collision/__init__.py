

class RectCorrectError(Exception):
    """ исключение для некорректных прямоугольников."""
    pass


def isCorrectRect(rect):
    """
    Проверяет, корректно ли задан прямоугольник.
    
    True -- если x1 < x2 и y1 < y2
    False -- в другом случае
    """
    (x1, y1), (x2, y2) = rect
    return x1 < x2 and y1 < y2


def isCollisionRect(rect1, rect2):
    """
    Проверяет, пересекаются ли два прямоугольника.
   
    True -- если прямоугольники пересекаются
    False -- если не пересекаются
    
    
    RectCorrectError -- если любой из прямоугольников некорректен
    """
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")
    
    (ax1, ay1), (ax2, ay2) = rect1
    (bx1, by1), (bx2, by2) = rect2
    
    # Проверка пересечения по осям X и Y
    if ax2 <= bx1 or bx2 <= ax1 or ay2 <= by1 or by2 <= ay1:
        return False
    return True


def intersectionAreaRect(rect1, rect2):
    """
    Вычисляет площадь пересечения двух прямоугольников.
    RectCorrectError -- если любой из прямоугольников некорректен
    """
    if not isCollisionRect(rect1, rect2):
        return 0.0
    
    (ax1, ay1), (ax2, ay2) = rect1
    (bx1, by1), (bx2, by2) = rect2
    
    # Находим координаты пересечения
    x_left = max(ax1, bx1)
    x_right = min(ax2, bx2)
    y_bottom = max(ay1, by1)
    y_top = min(ay2, by2)
    
    width = x_right - x_left
    height = y_top - y_bottom
    
    return width * height


def intersectionAreaMultiRect(rectangles):
    """
    вычисляет площадь пересечения всех переданных прямоугольников.
    RectCorrectError -- если любой прямоугольник некорректен
    """
    if not rectangles:
        return 0.0
    
    # Начинаем с первого прямоугольника
    (x_left, y_bottom), (x_right, y_top) = rectangles[0]
    
    # Проверяем все прямоугольники
    for i, rect in enumerate(rectangles):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Прямоугольник {i+1} некоректный")
        
        (x1, y1), (x2, y2) = rect
        
        # Находим общую область пересечения
        x_left = max(x_left, x1)
        y_bottom = max(y_bottom, y1)
        x_right = min(x_right, x2)
        y_top = min(y_top, y2)
        
        # Если область исчезла, пересечения нет
        if x_left >= x_right or y_bottom >= y_top:
            return 0.0
    
    # Вычисляем площадь общей области
    width = x_right - x_left
    height = y_top - y_bottom
    
    return width * height
