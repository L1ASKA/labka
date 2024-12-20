import tkinter as tk
import math
#Задание на л.р. №8 ООП 24
#Должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
#Ввод данных из файла с контролем правильности ввода.
#Базы данных не использовать. При необходимости сохранять информацию в файлах,
#разделяя значения запятыми (CSV файлы) или пробелами. Для GUI и визуализации использовать библиотеку tkinter.
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


def load_data(filename, error_label):
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
                        error_label.config(text=f"Ошибка в данных: {line}")
    except FileNotFoundError:
        error_label.config(text="Файл не найден. Убедитесь, что файл существует и указан правильно.")
    return triangles


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Triangle Operations")
        self.geometry("600x600")
        self.configure(bg="#2e2e2e")  # Темный фон для всего окна

        # Canvas для рисования
        self.canvas = tk.Canvas(self, width=500, height=500, bg="white")
        self.canvas.pack(padx=20, pady=20)

        # Фрейм для ошибок с тенью
        self.error_frame = tk.Frame(self, bg="#2e2e2e", bd=2, relief="solid", padx=10, pady=5)
        self.error_frame.pack(padx=20, pady=10, fill=tk.X)
        self.error_label = tk.Label(self.error_frame, text="", fg="red", font=("Arial", 12, "bold"))
        self.error_label.pack()

        # Загружаем данные из файла
        self.triangles = load_data("triangles.csv", self.error_label)

        # Фрейм для кнопок с тенью
        self.button_frame = tk.Frame(self, bg="#2e2e2e")
        self.button_frame.pack(padx=20, pady=20)

        # Современные кнопки с эффектами
        self.btn_visualize = tk.Button(self.button_frame, text="Визуализировать", command=self.visualize,
                                       bg="#4CAF50", fg="white", font=("Arial", 14), relief="flat", bd=2,
                                       width=20, height=2, activebackground="#45a049", pady=10)
        self.btn_visualize.grid(row=0, column=0, padx=10, pady=10)

        self.btn_rotate = tk.Button(self.button_frame, text="Повернуть", command=self.rotate,
                                    bg="#2196F3", fg="white", font=("Arial", 14), relief="flat", bd=2,
                                    width=20, height=2, activebackground="#1976d2", pady=10)
        self.btn_rotate.grid(row=0, column=1, padx=10, pady=10)

        self.btn_color = tk.Button(self.button_frame, text="Изменить цвет", command=self.change_color,
                                   bg="#FF5722", fg="white", font=("Arial", 14), relief="flat", bd=2,
                                   width=20, height=2, activebackground="#e64a19", pady=10)
        self.btn_color.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

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

        self.visualize()  # Перерисовать треугольники


if __name__ == "__main__":
    app = Application()
    app.mainloop()
