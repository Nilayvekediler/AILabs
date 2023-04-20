import tkinter as tk  # tkinter GUI kütüphanesi import edilir.
from tkinter import messagebox
import random as rndm
import math

def update_board(board):  # board'un üzerine sayıları yerleştiren fonk.
    for i in range(9):
        if board[i] == 0:
            button_text = ""
        else:
            button_text = str(board[i])
        buttons[i].config(text=button_text)


def button_click(i):
    global board
    clicked_tile = board[i]
    # listenin içindeki 0 değerinin indeksini yani boş kareyi oluşturacak indeksi empty_tile değişkenine atar. 0 değeri listede yoksa ValueError hatası verir.
    empty_tile = board.index(0)

    # tıklanan kare hareket ettirilebilir mi kontrol et :
    if i - 3 == empty_tile or i + 3 == empty_tile \
            or (i % 3 != 0 and i - 1 == empty_tile) \
            or (i % 3 != 2 and i + 1 == empty_tile):

        # hareket ettirilebilirse ettir
        board[i], board[empty_tile] = board[empty_tile], clicked_tile
        update_board(board)

        # her tıklamada oyun bitti mi diye kontrol ettir.
        if check_win():
            messagebox.showinfo("Oyun Sonu", "Tebrikler, oyunu kazandınız!")


def check_win():
    return board == [1, 2, 3, 4, 5, 6, 7, 8, 0]


root = tk.Tk()
root.title("8-Puzzle Oyunu")

frame = tk.Frame(root)
frame.grid()

buttons = []
for row in range(3):
    for col in range(3):
        button = tk.Button(frame, text="", width=20, height=10,
                           command=lambda i=row*3+col: button_click(i), background="#eed5d2")
        button.grid(row=row, column=col)
        buttons.append(button)

board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
#rndm.shuffle(board)
update_board(board)

root.mainloop()  # GUI'ı çalıştıran hazır fonk
# ---------------------------------------------

class LocalBeamSearch:
    def __init__(self):
        self.initialS = [1, 2, 3, 4, 5, 6, 7, 8, None]
        self.targetS = [1, 2, 3, 4, 5, 6, 7, 8, None]

        self.moves = {'up': -3, 'down': 3, 'left': -1, 'right': 1} # taşların hareketleri

    def TargetLocation(self, state):  # taşların hedef konumlarını bulan fonk.
        return sum([1 if state[i] != self.targetS[i] else 0 for i in range(9)])

    def GetCurrentS(self, state):  #taşların bulunduğu konumu getiren fonk.
        for i in range(0, 9, 3):
            print(state[i:i + 3])

    def GenerateRandomS(self): 
        randomS = self.initialS.copy()
        rndm.shuffle(randomS)
        return randomS

    def Move(self, state, index, step): #taşları hareket ettiren fonk.
        newS = state.copy()
        newS[index], newS[index + step] = newS[index + step], newS[index]
        return newS

    def LocalBeamSearch(self, k, n, steps):
        beams = [self.GenerateRandomS() for _ in range(n)]
        for i in range(steps):
            candidates = []
            for beam in beams:
                for moveName, moveStep in self.moves.items():
                    blankIndex = beam.index(None)
                    if (moveName == 'up' and blankIndex >= 3) or \
                            (moveName == 'down' and blankIndex < 6) or \
                            (moveName == 'left' and blankIndex % 3 != 0) or \
                            (moveName == 'right' and blankIndex % 3 != 2):
                        
                        newS = self.Move(beam, blankIndex, moveStep)
                        candidates.append(newS)

            candidates.sort(key=lambda x: self.TargetLocation(x))
            beams = candidates[:k]
    
            if self.TargetLocation(beams[0]) == 0:  # hedef olduysa durdur
                break
            print(f"Step {i+1}:")
            for beam in beams:
                self.GetCurrentS(beam)
            print("----------------------------")
        return beams[0]


localBeamSearch = LocalBeamSearch()
print("***8-Puzzle Probleminin Local Beam Search (Yerel Işın Araması) Algoritması İle Çözüm Adımları:")
result = localBeamSearch.LocalBeamSearch(k=5, n=10, steps=100)
localBeamSearch.GetCurrentS(result)
