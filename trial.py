import Move_Validation
import math
import random

scores = {"p":1, "b":3, "n":5, "r":7, "q":9, "k":10}

class Board:
    def __init__(self, board):
        self.turn = "black"
        self.board = board
        self.last_move = []
        self.temp_piece = None
        
    def gameover(self):
        if Move_Validation.is_check("white", self.board) or Move_Validation.is_check("black", self.board):
            return True
        
    def get_moves(self):
        all_moves = []
        for i in self.board:
            for j in i:
                if j != "00":
                    if j[0] == "w" and self.turn == "white":
                        for k in Move_Validation.validation("white" , [(self.board.index(i), i.index(j))], self.board):
                            all_moves.extend([((self.board.index(i), i.index(j)), k)])
                    elif j[0] =="b" and self.turn == "black":
                        for k in Move_Validation.validation("black", [(self.board.index(i), i.index(j))], self.board):
                            all_moves.extend([((self.board.index(i), i.index(j)), k)])
        return all_moves

    def make_move(self, a, b):
        self.temp_piece = self.board[b[0]][b[1]]
        self.board[b[0]][b[1]] = self.board[a[0]][a[1]]
        self.board[a[0]][a[1]] = "00"
        self.last_move.append((a, b, self.temp_piece))
        
    def unmake_move(self):
        self.board[self.last_move[-1][0][0]][self.last_move[-1][0][1]] = self.board[self.last_move[-1][1][0]][self.last_move[-1][1][1]]
        self.board[self.last_move[-1][1][0]][self.last_move[-1][1][1]] = self.last_move[-1][2]
        self.last_move.pop()

        

def evaluate(board):
    global scores
    score = 0
    for i in board.board:
        for j in i:
            if j[0] == "w":
                score -= scores[j[1]]
            elif j[0] == "b":
                score += scores[j[1]]
    return score
    
t_eval = 0
def minimax(board, depth, alpha, beta, maximizing_player):
    global t_eval
    if depth == 0 or board.gameover():
       t_eval += 1
       #print(board.last_move[-1])
       return None, evaluate(board)
    moves = board.get_moves()
    best_move = random.choice(moves)

    if maximizing_player:
       board.turn = "black"
       max_eval = -math.inf
       for move in moves:
           board.make_move(move[0], move[1])
           current_eval = minimax(board, depth - 1, alpha, beta, False)[1]
           board.unmake_move()
           if current_eval > max_eval:
               max_eval = current_eval
               best_move = move
           alpha = max(alpha, current_eval)
           if beta <= alpha:
               break
       return best_move, max_eval
    else:
       board.turn = "white"
       min_eval = math.inf
       for move in moves:
           board.make_move(move[0], move[1])
           current_eval = minimax(board, depth - 1, alpha, beta, True)[1]
           board.unmake_move()
           if current_eval < min_eval:
               min_eval = current_eval
               best_move = move
           beta = min(beta, current_eval)
           if beta <= alpha:
               break
       return best_move, min_eval
nextmove = []

def findmove(board, validmoves):
    global nextmove
    nextmove = None
    random.shuffle(validmoves)
    negamax(board, 3, -1, validmoves)
    return nextmove
def negamax(board, depth, turnmultiplier, validmoves):
    global nextmove
    if depth == 0:
        return turnmultiplier * evaluate(board)
    
    maxscore = -9999
    for move in validmoves:
        board.make_move(move[0], move[1])
        nextmoves = board.get_moves()
        score = -negamax(board, depth-1, -turnmultiplier, nextmoves)
        if score > maxscore:
            maxscore = score
            if depth == 3:
                nextmove = move
        board.unmake_move()
    return maxscore

import copy
import turtle
import socket
import threading
import os
import platform
import time
"""
if platform.system() == "Windows":
    try:
        os.system("pip install numpy")
    except:
        print("Please install numpy module")
        quit()
elif platform.system() == "Darwin":
    try:
        os.system("conda install numpy")
    except:
        try:
            os.system("pip install numpy")
        except:
            print("please install numpy module")
"""
import Move_Validation

# initialising all the values
nam = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
       ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
       ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
       ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
       ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
       ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
       ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
       ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]

board = [["wr1", "wn1", "wb1", "wq", "wk", "wb2", "wn2", "wr2"],
         ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],
         ["00", "00", "00", "00", "00", "00", "00", "00"],
         ["00", "00", "00", "00", "00", "00", "00", "00"],
         ["00", "00", "00", "00", "00", "00", "00", "00"],
         ["00", "00", "00", "00", "00", "00", "00", "00"],
         ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"],
         ["br1", "bn1", "bb1", "bq", "bk", "bb2", "bn2", "br2"]]
Board = Board(board)

wr1, wn1, wb1, wq, wk, wb2, wn2, wr2, wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()

br1, bn1, bb1, bq, bk, bb2, bn2, br2, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()

all_pieces = [wr1, wn1, wb1, wq, wk, wb2, wn2, wr2, wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8,
              br1, bn1, bb1, bq, bk, bb2, bn2, br2, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8]

names = ["wr1", "wn1", "wb1", "wq", "wk", "wb2", "wn2", "wr2", "wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8",
         "br1", "bn1", "bb1", "bq", "bk", "bb2", "bn2", "br2", "bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"]

turtle.register_shape("wk.gif"), turtle.register_shape("wq.gif"), turtle.register_shape(
    "wb.gif")
turtle.register_shape("wr.gif"), turtle.register_shape("wp.gif"), turtle.register_shape(
    "wn.gif")
turtle.register_shape("bk.gif"), turtle.register_shape("bq.gif"), turtle.register_shape(
    "bb.gif")
turtle.register_shape("br.gif"), turtle.register_shape("bp.gif"), turtle.register_shape(
    "bn.gif")
turtle.register_shape("outline_red.gif")


# setting up the screen
scrn = turtle.Screen()
scrn.setup(1100, 720)
scrn.colormode(255)
scrn.bgcolor((173, 216, 230))
scrn.bgpic("Board.gif")
scrn.title("Chess")


# variables

selection = []
o = 0
na = ""
turn = "white"
uname = input("enter your name")

# pens for writing
pen1, pen2, pen3 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
pen1.hideturtle(), pen2.hideturtle(), pen3.hideturtle()
pen1.penup(), pen2.penup(), pen3.penup()
pen1.goto(-464.0, 244.0), pen2.goto(-457.0, -232.0), pen3.goto(376.0, 52.0)
pen1.pendown(), pen2.pendown(), pen3.pendown()








# making the move of opponent
def makeopp_move(a):
    global board, turn, names
    Board.board = board

    move1 = findmove(Board, Board.get_moves())
    move = (move1, ())
    print(move)
    print(t_eval)
    print(Board.last_move)
    if board[move[0][1][0]][move[0][1][1]] in names:
        l = names.index(board[move[0][1][0]][move[0][1][1]])
        names.pop(l), all_pieces[l].speed(0), all_pieces[l].goto(1100, 1100), all_pieces.pop(l)
    print(move)
    board[move[0][1][0]][move[0][1][1]] = board[move[0][0][0]][move[0][0][1]]
    m = names.index(board[move[0][0][0]][move[0][0][1]])
    board[move[0][0][0]][move[0][0][1]] = "00"
    all_pieces[m].speed(4)
    all_pieces[m].goto(80 * (move[0][1][1]) - 280, -(80 * (move[0][1][0]) - 280))
    turn = "white"
    board1 = copy.deepcopy(board)
    
    if Move_Validation.is_check("white", board):
        job3(uname+"'s turn" + "\n" + "Check")
        if Move_Validation.check_mate("white", board):
            job3("Checkmate" + "\n" + "cpu wins!")
                                
    board = board1
    
# for getting the full name of the piece

def full_name(a):
    if a[1] == "r":
        return "rook"
    elif a[1] == "n":
        return "knight"
    elif a[1] == "b":
        return "bishop"
    elif a[1] == "q":
        return "queen"
    elif a[1] == "k":
        return "king"
    elif a[1] == "p":
        return "pawn"



# for getting the team of the piece

def team(a):
    if a[0] == "w":
        return "white"
    else:
        return "black"



# for displaying the pieces

def display_pieces():
    print("\nSetting up board\n")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "00":
                l = names.index(board[i][j])
                all_pieces[l].shape(str(board[i][j][0:2]) + ".gif")
                all_pieces[l].speed(0), all_pieces[l].penup(), all_pieces[l].goto(80 * j - 280, -(80 * i - 280))



def job1(a):
    pen1.write(a, font=("Times", 25, "bold"))

def job2(a):
    pen2.write(a, font=("Times", 25, "bold"))

def job3(a):
    pen3.clear()
    pen3.write(a, font=("Times", 25, "bold"))
def checkmate():
    time.sleep(4)
    turtle.bye()
    cli_sock.close()
    print("Connection closed")
    quit()

def pvp(x, y):
    global board, turn, o, names, tc, p1, p2
    i = round((280 + x) / 80)
    j = round((280 + y) / 80)
    if len(selection) == 1 and (turn == "white"):
        for n in lis[:o + 1]:
            n.goto(1100, 1100)
        for n in lis1[:o+1]:
            n.goto(1100, 1100)
        selection.append((7 - j, i))
        if selection[0] == selection[1]:
            selection.clear()
            return
        
        if ((7 - j), i) in Move_Validation.validation(turn, selection, board):
            if not (board[7 - j][i][0] == turn[0]):
                if board[7 - j][i] in names:
                    l = names.index(board[7 - j][i])
                    names.pop(l), all_pieces[l].speed(0), all_pieces[l].goto(1100, 1100), all_pieces.pop(l)
                board[7 - j][i] = board[selection[0][0]][selection[0][1]]
                m = names.index(board[selection[0][0]][selection[0][1]])
                board[selection[0][0]][selection[0][1]] = "00"
                na = nam[selection[0][0]][selection[0][1]] + nam[selection[1][0]][selection[1][1]]
                selection.clear()
                all_pieces[m].speed(4)
                all_pieces[m].goto(80 * (i) - 280, -(80 * (7 - j) - 280))
                turn = "black"
                job3("cpu's turn")
                board1 = copy.deepcopy(board)

                if Move_Validation.is_check("black", board):
                    job3("cpu's turn" + "\n" + "Check")
                    if Move_Validation.check_mate("black", board):
                        job3("Checkmate" + "\n" + uname + " wins!")
                             
                board = board1
                makeopp_move(2)
        
                return
            selection.clear()
            return
        selection.clear()
        return
        
        selection.clear()
        return
    elif len(selection) == 0 and (turn == "white"):
        if board[7 - j][i] != "00" and board[7 - j][i][0] == turn[0]:
            selection.append((7 - j, i))
            ust = Move_Validation.validation(turn, selection, board)
            for n in lis:
                try:
                    if not ust[lis.index(n)] == (-1, -1):
                        if board[ust[lis.index(n)][0]][ust[lis.index(n)][1]] != "00":
                            lis1[lis.index(n)].shape("outline_red.gif")
                            lis1[lis.index(n)].goto(80 * ust[lis.index(n)][1] - 280, -(80 * ust[lis.index(n)][0] - 280))
                        else:
                            n.goto(80 * ust[lis.index(n)][1] - 280, -(80 * ust[lis.index(n)][0] - 280))
                        o = lis.index(n)
                except:
                    pass
            return
    selection.clear()



# calling the functions
from Marker import lis, lis1
display_pieces()
turtle.onscreenclick(pvp, 1)
turtle.listen()
turtle.mainloop()



        


