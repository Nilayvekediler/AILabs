import tkinter as tk  # GUI için tkinter kütüphanesi import edilir.
from tkinter import messagebox

class Game:
    def __init__(self, board, current_player):  # oyunun genel durumu tutulur
        self.board = board
        self.current_player = current_player

    def is_valid_move(self, x, y):  # belirtilen koordinatlarda yapılacak bir hamle var mı?
        return self.board[3*x+y] == " "

    def make_move(self, x, y):  # belirtilen koordinatlarda hamle yapar ve oyun durumunu günceller
        new_board = self.board[:]
        new_board[3*x+y] = self.current_player
        return Game(new_board, "O" if self.current_player == "X" else "X")

    def check_win(self):  # kazanma durumu kontrol edilir
        for i in range(3):
            if self.board[3*i] == self.board[3*i+1] == self.board[3*i+2] != " ":
                return True
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True

    def minimax(self):  # minimax algosu ile en iyi hamle seçilir. Oyun sonucunda ya bilgisayar kazanır ya da berabere biter
        game = Game(self.board, "O")
        best_score = float("-inf")
        best_move = None
        for i in range(3):
            for j in range(3):
                # Verilen koordinatlar için oyun tahtasında kare boş mu değil mi kontrol eder. Boşsa True, doluysa False döner
                if game.is_valid_move(i, j):
                    # Verilen koordinatlar için yeni bir Game nesnesi oluşturur ve bu nesnenin tahtasındaki belirtilen kareyi sıradaki oyuncunun işareti ile doldurur
                    new_game = game.make_move(i, j)
                    score = self.max_value(new_game)
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def max_value(self, game):
        if game.check_win():  # Oyunun kazananı olup olmadığını kontrol eder. Eğer herhangi bir oyuncu üçünü bir arada yapmışsa (yatay, dikey veya çapraz), True döner. Aksi takdirde False döner.
            return 1
        if game.check_tie():
            return 0
        v = float("-inf")
        for i in range(3):
            for j in range(3):
                if game.is_valid_move(i, j):
                    v = max(v, self.min_value(game.make_move(i, j)))
        return v

    def min_value(self, game):
        if game.check_win():
            return -1
        if game.check_tie():
            return 0
        v = float("inf")
        for i in range(3):
            for j in range(3):
                if game.is_valid_move(i, j):
                    v = min(v, self.max_value(game.make_move(i, j)))
        return v

    def check_tie(self):  # oyunun berabere bitip bitmediğini kontrol eder
        return " " not in self.board


class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]  # oyun tahtası
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.create_board()
        self.root.mainloop()

    def create_board(self):
        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = tk.Button(self.root, text=" ", font=("Arial", 40),
                                 width=5, height=2, command=lambda x=i, y=j: self.on_click(x, y))
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

    def on_click(self, x, y):
        if self.board[3*x+y] == " ":
            self.cells[x][y].config(text=self.current_player)
            self.board[3*x+y] = self.current_player
            if self.check_win():
                messagebox.showinfo(
                    "Oyun Sonucu", f"{self.current_player} kazandı!")
                self.root.quit()
            elif self.check_tie():
                messagebox.showinfo("Oyun Sonucu", "Berabere!")
                self.root.quit()
            else:
                self.current_player = "O"
                game = Game(self.board, "O")
                x, y = game.minimax()
                self.cells[x][y].config(text="O")
                self.board[3*x+y] = "O"
                if game.check_win():
                    messagebox.showinfo("Oyun Sonucu", "Bilgisayar Kazandı!")
                    self.root.quit()
                elif game.check_tie():
                    messagebox.showinfo("Berabere", "Berabere!")
                    self.root.quit()
                else:
                    self.current_player = "X"

    def check_win(self):
        for i in range(3):
            if self.board[3*i] == self.board[3*i+1] == self.board[3*i+2] != " ":
                return True
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True

    def check_tie(self):
        return " " not in self.board

if __name__ == "__main__":
    TicTacToe()
