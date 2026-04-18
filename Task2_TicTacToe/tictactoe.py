import tkinter as tk
from tkinter import messagebox

player_score = 0
ai_score = 0
draw_score = 0

board = [""] * 9
buttons = []

def check_winner(b):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]

    for a,b1,c in win:
        if b[a] == b[b1] == b[c] and b[a] != "":
            return b[a]

    if "" not in b:
        return "Draw"
    return None

def reset_board():
    global board
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")

def minimax(board, is_ai):
    result = check_winner(board)

    if result == "O": return 1
    if result == "X": return -1
    if result == "Draw": return 0

    if is_ai:
        best = -999
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best = max(score, best)
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best = min(score, best)
        return best

def ai_move():
    best_score = -999
    move = 0
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"
    buttons[move]["text"] = "O"
    buttons[move]["state"] = "disabled"
    check_game()

def player_move(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i]["text"] = "X"
        buttons[i]["state"] = "disabled"
        check_game()
        if "" in board:
            ai_move()

def check_game():
    global player_score, ai_score, draw_score
    result = check_winner(board)

    if result:
        if result == "X":
            player_score += 1
            messagebox.showinfo("Result", "You Win 🎉")
        elif result == "O":
            ai_score += 1
            messagebox.showinfo("Result", "AI Wins 🤖")
        else:
            draw_score += 1
            messagebox.showinfo("Result", "Draw 🤝")

        update_scoreboard()
        reset_board()

def update_scoreboard():
    score_label.config(
        text=f"Player: {player_score}   AI: {ai_score}   Draw: {draw_score}"
    )

window = tk.Tk()
window.title("AI Tic Tac Toe")

score_label = tk.Label(window, text="Player: 0   AI: 0   Draw: 0",
                       font=("Arial", 14))
score_label.grid(row=0, column=0, columnspan=3)

for i in range(9):
    btn = tk.Button(window, text="", font=("Arial",22),
                    width=6, height=3,
                    command=lambda i=i: player_move(i))
    btn.grid(row=(i//3)+1, column=i%3)
    buttons.append(btn)

window.mainloop()
