class Figure():
    def print_create(self):
        print("Object create")

    def get_coords(self, n):
        self.x = []
        self.y = []
        for i in range(n):
            coord = []
            while True:
                try:
                    coord1, coord2 = map(int, input('Введите через пробел координаты ' + str(i+1) + ' точки: \n').split())
                    break
                except:
                    print("Введены неккоректные координаты")
            self.x.append(coord1)
            self.y.append(coord2)
    def large(self):
        x_max = max(self.x)
        x_min = min(self.x)
        y_max = max(self.y)
        y_min = min(self.y)
        return x_min, x_max, y_min, y_max

    def move(self, n, deltaX, deltaY):
        for i in range(n):
            self.x[i], self.y[i] = self.x[i] + deltaX, self.y[i] + deltaY

class triangle(Figure):
    def __init__(self):
        Figure.get_coords(self, 3)

    def __str__(self):
        self.a = self.x[0], self.y[0]
        self.b = self.x[1], self.y[1]
        self.c = self.x[2], self.y[2]
        return "Triangle ({0.a}; {0.b}; {0.c})".format(self)

    def print_create(self):
        print("Triangle create!")

    def move(self, deltaX: float, deltaY: float):
       Figure.move(self, 3, deltaX, deltaY)

class rectangle(Figure):
    def __init__(self):
        Figure.get_coords(self, 4)

    def checkr(self):
        if ((((self.x[0]==self.x[1]) or (self.x[0]==self.x[2]) or (self.x[0]==self.x[3]))
                and((self.x[1]==self.x[0]) or (self.x[1]==self.x[2]) or (self.x[1]==self.x[3]))
                    and((self.x[2]==self.x[0]) or (self.x[2]==self.x[1]) or (self.x[2]==self.x[3])))
                        and(((self.y[0]==self.y[1]) or (self.y[0]==self.y[2]) or (self.y[0]==self.y[3]))
                            and((self.y[1]==self.y[0]) or (self.y[1]==self.y[2]) or (self.y[1]==self.y[3]))
                                and((self.y[2]==self.y[0]) or (self.y[2]==self.y[1]) or (self.y[2]==self.y[3])))):
            return 1


    def __str__(self):
        self.a = self.x[0], self.y[0]
        self.b = self.x[1], self.y[1]
        self.c = self.x[2], self.y[2]
        self.d = self.x[3], self.y[3]
        return "Pentagon ({0.a}; {0.b}; {0.c}; {0.d})".format(self)

    def print_create(self):
        print("Pentagon create!")

    def move(self, deltaX: float, deltaY: float):
        Figure.move(self, 4, deltaX, deltaY)

def textMenu():
    print("Выберите действие или завершите программу:")
    print(" [1] Создать треугольник")
    print(" [2] Создать прямоугольник")
    print(" [3] Найти пересечение")
    print(" [0] Выход")

def textTriangle():
    print("     Выберите действие:")
    print("     [1] Переместить треугольник в пространстве")
    print("     [2] Показать положение треугольника в пространстве")
    print("     [0] Выход")

def textRectangle():
    print("     Выберите действие:")
    print("     [1] Переместить прямоугольник в пространстве")
    print("     [2] Показать положение прямоугольник в пространстве")
    print("     [0] Выход")


def IsIntersect(t,r):
    x_min1, x_max1, y_min1, y_max1 = t.large()
    x_min2, x_max2, y_min2, y_max2 = r.large()
    if ((x_min1<=x_min2 and x_max2<=x_max1) or (x_min2<=x_min1 and x_max1<=x_max2) or (x_min1<=x_min2 and x_max1<=x_max2 and x_min2<=x_max1) or
            (x_min2<=x_min1 and x_max2<=x_max1 and x_min1<=x_max2)
        and (y_min1<=y_min2 and y_max2<=y_max1) or (y_min2<=y_min1 and y_max1<=y_max2) or (y_min1<=y_min2 and y_max1<=y_max2 and y_min2<=y_max1) or
            (y_min2<=y_min1 and y_max2<=y_max1 and y_min1<=y_max2)):
        print("Пересечение есть")
    else:
        print("Пересечение отсутствует")

def mainmenu():
    flag1 = flag2 = 0
    textMenu()
    try:
        option = int(input())
    except ValueError:
        option = 5
    while option:
        if option == 1:
            flag1 = 1
            t = triangle()
            t.print_create()
            textTriangle()
            try:
                option_of_triangle = int(input())
            except ValueError:
                option_of_triangle = 5
            while option_of_triangle:
               if option_of_triangle == 1:
                   print(
                       "Введите через пробел координаты смещения фигуры (смещение по X и смещение по Y соответственно)")
                   check = True
                   while check:
                       try:
                           a, b = map(float, input().split())
                           check = False
                       except ValueError:
                           print("Введены неккоректные координаты перемещения")
                   t.move(a, b)
                   print(t)
               elif option_of_triangle == 2:
                   print(t)
               else:
                   print("Введена неккоректная команда")
               textTriangle()
               try:
                option_of_triangle = int(input())
               except ValueError:
                   option_of_triangle = 5
        elif option == 2:
            r = rectangle()
            flag2 = r.checkr()
            if flag2:
                r.print_create()
                textRectangle()
                try:
                    option_of_Rectangle = int(input())
                except ValueError:
                    option_of_Rectangle = 5
                while option_of_Rectangle:
                    if option_of_Rectangle == 1:
                        print(
                            "Введите через пробел координаты смещения фигуры (смещение по X и смещение по Y соответственно)")
                        check = True
                        while check:
                            try:
                                a, b = map(float, input().split())
                                check = False
                            except ValueError:
                                print("Введены неккоректные координаты перемещения")
                        r.move(a, b)
                        print(r)
                    elif option_of_pentagon == 2:
                        print(r)
                    else:
                        print("Введена неккоректная команда")
                    textRectangle()
                    try:
                        option_of_pentagon = int(input())
                    except ValueError:
                        option_of_pentagon = 5
            else:
                print("Данные координаты не образуют прямоугольник,прямоугольник не создан")
        elif option == 3:
            if flag1 and flag2:
                IsIntersect(t,r)
            elif not flag1 and not flag2:
                print("Для начала создайте треугольник и прямоугольник")
            elif not flag1:
                print("Для начала создайте треугольник")
            else:
                print("Для начала создайте прямоугольник")
        else:
            print("Введена неккоректная команда")
        textMenu()
        try:
            option = int(input())
        except ValueError:
            option = 5

if __name__ == '__main__':
    mainmenu()