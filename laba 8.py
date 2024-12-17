import tkinter as tk
import math
#Требуется написать ООП с графическим интерфейсом в соответствии со своим вариантом.
#Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
#Ввод данных из файла с контролем правильности ввода.
#Базы данных не использовать. При необходимости сохранять информацию в файлах, разделяя значения запятыми (CSV файлы) или пробелами.
#Для GUI и визуализации использовать библиотеку tkinter.
#Объекты – треугольники
#Функции:	проверка пересечения
#визуализация
#раскраска
#поворот вокруг одной из вершин



class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, color="blue"):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.color = color

    def visualize(self, canvas):
        """Отображение треугольника на канвасе."""
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, fill=self.color, outline='black')

    def colorize(self, new_color):
        """Изменение цвета треугольника."""
        self.color = new_color

    def rotate(self, angle, vertex="A"):
        """Поворот треугольника вокруг одной из вершин на заданный угол."""
        angle = math.radians(angle)
        if vertex == "A":
            cx, cy = self.x1, self.y1
            self.x2, self.y2 = self.rotate_point(self.x2, self.y2, cx, cy, angle)
            self.x3, self.y3 = self.rotate_point(self.x3, self.y3, cx, cy, angle)
        elif vertex == "B":
            cx, cy = self.x2, self.y2
            self.x1, self.y1 = self.rotate_point(self.x1, self.y1, cx, cy, angle)
            self.x3, self.y3 = self.rotate_point(self.x3, self.y3, cx, cy, angle)
        elif vertex == "C":
            cx, cy = self.x3, self.y3
            self.x1, self.y1 = self.rotate_point(self.x1, self.y1, cx, cy, angle)
            self.x2, self.y2 = self.rotate_point(self.x2, self.y2, cx, cy, angle)

    def rotate_point(self, x, y, cx, cy, angle):
        """Поворот одной точки вокруг другой."""
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        x_new = cos_theta * (x - cx) - sin_theta * (y - cy) + cx
        y_new = sin_theta * (x - cx) + cos_theta * (y - cy) + cy
        return x_new, y_new


def load_data(filename):
    """Загрузка данных треугольников из файла."""
    triangles = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 6:
                    try:
                        x1, y1, x2, y2, x3, y3 = map(float, parts)
                        triangles.append(Triangle(x1, y1, x2, y2, x3, y3))
                    except ValueError:
                        print(f"Ошибка в данных: {line}")
    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что файл существует и указан правильно.")
    return triangles


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Triangle Operations")
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        # Загружаем данные из файла
        self.triangles = load_data("triangles.csv")

        # Кнопки для действий
        self.btn_visualize = tk.Button(self, text="Визуализировать", command=self.visualize)
        self.btn_visualize.pack()
        self.btn_rotate = tk.Button(self, text="Повернуть", command=self.rotate)
        self.btn_rotate.pack()
        self.btn_color = tk.Button(self, text="Изменить цвет", command=self.change_color)
        self.btn_color.pack()

        # Список цветов для цикличного изменения
        self.colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        self.color_index = 0  # Индекс текущего цвета

    def visualize(self):
        """Отобразить все треугольники на холсте."""
        self.canvas.delete("all")  # Очистить холст перед рисованием
        for triangle in self.triangles:
            triangle.visualize(self.canvas)

    def rotate(self):
        """Повернуть все треугольники на 30 градусов вокруг вершины A."""
        for triangle in self.triangles:
            triangle.rotate(30)  # Повернуть на 30 градусов
        self.visualize()  # Перерисовать треугольники

    def change_color(self):
        """Циклически изменяет цвет всех треугольников."""
        new_color = self.colors[self.color_index]
        for triangle in self.triangles:
            triangle.colorize(new_color)

        # Обновить индекс для следующего цвета
        self.color_index = (self.color_index + 1) % len(self.colors)

        self.visualize()  # Перерисовать треугольники с новым цветом


if __name__ == "__main__":
    app = Application()
    app.mainloop()