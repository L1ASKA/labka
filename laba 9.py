import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.geometry("400x500")  # Размер окна
        self.root.config(bg="#f0f0f0")

        self.board = [""] * 9  # игровое поле (9 клеток)
        self.current_player = None  # еще не выбран игрок
        self.player_choice = None  # символ игрока (X или O)

        self.buttons = []  # список для хранения кнопок

        self.create_widgets()

    def create_widgets(self):
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

    def set_player_choice(self, choice):
        """Выбор стороны игрока"""
        self.player_choice = choice
        self.current_player = "X"  # Игрок начинает первым
        self.choose_frame.pack_forget()  # Прячем кнопки выбора стороны
        if self.player_choice == "X":
            self.current_player = "O"  # Бот начинает игру за "O"
            self.bot_move()
        else:
            self.start_game()

    def start_game(self):
        """Запуск игры после выбора стороны"""
        if self.player_choice == "O":
            self.bot_move()  # Если игрок выбрал "O", то ходит бот первым

    def make_move(self, i):
        if self.board[i] == "" and self.check_winner() is None and self.current_player == "X":
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player, bg="#ddd", fg="#333")
            if self.check_winner():
                self.show_winner()
            else:
                self.switch_player()
                self.bot_move()

    def bot_move(self):
        """Ход бота, который выбирает оптимальный ход"""
        if self.current_player == "O":  # Бот ходит только когда его ход
            best_move = self.best_move()
            self.board[best_move] = "O"
            self.buttons[best_move].config(text="O", bg="#ddd", fg="#333")
            if self.check_winner():
                self.show_winner()
            else:
                self.switch_player()

    def best_move(self):
        """Находит наилучший ход для бота"""
        # Проверка, можно ли победить
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                if self.check_winner() == "O":
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Блокировка хода игрока (если он может победить)
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "X"
                if self.check_winner() == "X":
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Взять центральную клетку, если она пустая
        if self.board[4] == "":
            return 4

        # Пробуем углы
        for i in [0, 2, 6, 8]:
            if self.board[i] == "":
                return i

        # Пробуем брать боковые клетки
        for i in [1, 3, 5, 7]:
            if self.board[i] == "":
                return i

        return random.choice([i for i in range(9) if self.board[i] == ""])  # если не осталось выигрышных ходов

    def switch_player(self):
        """Меняет текущего игрока"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Проверка на победу"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные линии
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные линии
            [0, 4, 8], [2, 4, 6]  # Диагонали
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != "":
                return self.board[combination[0]]

        if "" not in self.board:
            return "Draw"  # Ничья

        return None  # Игра продолжается

    def show_winner(self):
        """Показывает сообщение о победе"""
        winner = self.check_winner()
        if winner == "Draw":
            messagebox.showinfo("Ничья", "Игра завершена. Ничья!")
        else:
            messagebox.showinfo("Победа", f"Победил игрок {winner}!")
        self.reset_game()

    def reset_game(self):
        """Сбрасывает игру"""
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", bg="#ffffff", fg="#000000")
        self.current_player = None
        self.choose_frame.pack()  # Показываем кнопки выбора стороны снова


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()

