import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")

        self.board = [""] * 9  # Игровое поле (9 клеток)
        self.current_player = None  # Текущий игрок
        self.player_choice = None  # Символ игрока (X или O)

        self.buttons = []  # Список для хранения кнопок
        self.create_widgets()

    def create_widgets(self):
        """Создание всех графических элементов."""
        # Создаем контейнер для игрового поля
        self.game_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.game_frame.pack(pady=20)

        # Создаем кнопки для игрового поля
        for i in range(9):
            button = tk.Button(self.game_frame, text="", font=('Arial', 30), width=5, height=2,
                               command=lambda i=i: self.make_move(i),
                               bg="#ffffff", fg="#000000", bd=3, relief="raised",
                               activebackground="#ddd", activeforeground="#333", highlightthickness=2)
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        # Добавляем кнопки для выбора стороны (X или O)
        self.choose_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.choose_frame.pack(pady=10)

        self.x_button = tk.Button(self.choose_frame, text="Играть за X", font=('Arial', 18),
                                  command=lambda: self.set_player_choice("X"),
                                  bg="#4CAF50", fg="#ffffff", width=12, height=2, bd=0, relief="raised",
                                  activebackground="#45a049")
        self.x_button.grid(row=0, column=0, padx=10, pady=10)

        self.o_button = tk.Button(self.choose_frame, text="Играть за O", font=('Arial', 18),
                                  command=lambda: self.set_player_choice("O"),
                                  bg="#2196F3", fg="#ffffff", width=12, height=2, bd=0, relief="raised",
                                  activebackground="#0b7dda")
        self.o_button.grid(row=0, column=1, padx=10, pady=10)

        # Кнопка для сброса игры
        self.new_game_button = tk.Button(self.root, text="Новая игра", font=('Arial', 14), command=self.reset_game,
                                         bg="#FF5733", fg="#ffffff", width=20, height=2, bd=0, relief="raised",
                                         activebackground="#FF2E00")
        self.new_game_button.pack(pady=20)

    def set_player_choice(self, choice):
        """Устанавливает выбор игрока (X или O) и начинает игру."""
        self.player_choice = choice
        if choice == "X":
            self.current_player = "O"  # Бот ходит первым, если игрок выбрал X
            self.choose_frame.pack_forget()  # Скрываем выбор
            self.bot_move()  # Бот делает первый ход
        else:
            self.current_player = "O"  # Игрок ходит первым, если выбрал O
            self.choose_frame.pack_forget()  # Скрываем выбор

    def make_move(self, i):
        """Делает ход игрока, если клетка пустая и игра не завершена."""
        if self.board[i] == "" and self.check_winner() is None and self.current_player == self.player_choice:
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player, bg="#ddd", fg="#333", state=tk.DISABLED)
            if self.check_winner():
                self.show_winner()
            else:
                self.switch_player()
                if self.current_player != self.player_choice:
                    self.bot_move()

    def bot_move(self):
        """Ход бота (более умный ход)."""
        if self.current_player != self.player_choice:
            best_move = self.best_move()
            self.board[best_move] = self.current_player
            self.buttons[best_move].config(text=self.current_player, bg="#ddd", fg="#333", state=tk.DISABLED)
            if self.check_winner():
                self.show_winner()
            else:
                self.switch_player()

    def best_move(self):
        """Находит наилучший ход для бота: блокирует победу игрока, пытается выиграть."""
        # Проверка на победу бота
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.current_player
                if self.check_winner() == self.current_player:
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Блокировка победы игрока
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.player_choice
                if self.check_winner() == self.player_choice:
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Центральная клетка
        if self.board[4] == "":
            return 4

        # Пробуем углы
        for i in [0, 2, 6, 8]:
            if self.board[i] == "":
                return i

        # Пробуем боковые клетки
        for i in [1, 3, 5, 7]:
            if self.board[i] == "":
                return i

        # Если нет других ходов, выбираем случайный
        return random.choice([i for i in range(9) if self.board[i] == ""])

    def switch_player(self):
        """Переключение между игроками."""
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def check_winner(self):
        """Проверка на наличие победителя."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Ряды
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Колонки
            [0, 4, 8], [2, 4, 6]              # Диагонали
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return self.board[combo[0]]
        if "" not in self.board:
            return "Ничья"  # Ничья, если все клетки заполнены
        return None

    def show_winner(self):
        """Отображение победителя или ничьей."""
        winner = self.check_winner()
        if winner == "Ничья":
            messagebox.showinfo("Результат игры", "Ничья!")
        else:
            messagebox.showinfo("Результат игры", f"Победил {winner}!")
        self.reset_game()

    def reset_game(self):
        """Сброс игры."""
        self.board = [""] * 9
        self.current_player = None
        self.player_choice = None
        for button in self.buttons:
            button.config(text="", bg="#ffffff", state=tk.NORMAL)  # Сброс кнопок
        self.choose_frame.pack(pady=10)  # Показываем выбор игрока


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()