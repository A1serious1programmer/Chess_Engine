import copy
import turtle
import socket
import threading
import os
import platform
import time

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
turn = ""
turn1 = ""
oppname = ""
uname = ""


# pens for writing
pen1, pen2, pen3 = turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
pen1.hideturtle(), pen2.hideturtle(), pen3.hideturtle()
pen1.penup(), pen2.penup(), pen3.penup()
pen1.goto(-464.0, 244.0), pen2.goto(-457.0, -232.0), pen3.goto(376.0, 52.0)
pen1.pendown(), pen2.pendown(), pen3.pendown()



# networking part
def receive():
    global turn, turn1, oppname, uname
    print("""\nWAITING FOR AN OPPONENT...\n""")
    while True:
        try:
            data = cli_sock.recv(1024).decode()
        except:
            print("error")
            print("Closing in 5 seconds")
            turtle.bye()
            time.sleep(5)
            quit()
        a = str(data)
        if "turnname" in a:
            cli_sock.close()
            print("error occured try again")
        if "error" in a:
            print(a)
            print("Closing in 5 seconds")
            turtle.bye()
            time.sleep(5)
            quit()
        if a[-4:] == "turn":
            turn = a[0:5]
            turn1 = a[0:5]
            print(turn1)
            print("\nGAME FOUND\n")
            uname = input("Enter your name:")
            cli_sock.send(("name" + uname).encode())
        elif a[0:4] == "name":
            oppname = a[4:]
            print("\nOPPONENT NAME: " + oppname +"\n")
            display_pieces()
            try:
                if turn1 == "white":
                    pen1.write(uname, font=("Times", 25, "bold"))
                    pen2.write(oppname, font=("Times", 25, "bold"))
                    pen3.write(uname + "'s turn", font=("Times", 25, "bold"))
                elif turn1 == "black":
                    pen1.write(oppname, font=("Times", 25, "bold"))
                    pen2.write(uname, font=("Times", 25, "bold"))
                    pen3.write(oppname + "'s turn", font=("Times", 25, "bold"))
            except:
                pass

        elif len(a) == 4:
            makeopp_move(data)


# socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
HOST = "34.131.13.174"
PORT = 3389

try:
    cli_sock.connect((HOST, PORT))
except:
    print("Server didnt accept connection...")
    print("Closing in 5 seconds")
    turtle.bye()
    time.sleep(5)
    quit()
print('CONNECTED TO SERVER...')





# making the move of opponent
def makeopp_move(a):
    global board, turn, coor, coor1
    b = a[0:2]
    c = a[2:4]
    for i in nam:
        for j in i:
            if j == b:
                coor = (nam.index(i), i.index(j))
            elif j == c:
                coor1 = (nam.index(i), i.index(j))
    sel = board[coor[0]][coor[1]]
    opp = board[coor1[0]][coor1[1]]
    board[coor1[0]][coor1[1]] = board[coor[0]][coor[1]]
    board[coor[0]][coor[1]] = "00"
    if opp in names:
        l = names.index(opp)
        names.pop(l), all_pieces[l].speed(0), all_pieces[l].goto(1100, 1100), all_pieces.pop(l)
    m = names.index(sel)
    all_pieces[m].speed(4)
    all_pieces[m].goto(80 * (coor1[1]) - 280, -(80 * coor1[0] - 280))
    pen3.clear()
    turn = "white"
    pen3.write(uname + "'s turn", font=("Times", 25, "bold"))
    board1 = copy.deepcopy(board)
    if Move_Validation.is_check(turn1, board):
        pen3.clear()
        pen3.write(uname + "'s turn" + "\n" + "Check", font=("Times", 25, "bold"))
        if Move_Validation.check_mate(turn1, board):
            pen3.clear()
            pen3.write("Checkmate" + "\n" + oppname + " wins!" , font=("Times", 25, "bold"))
            cli_sock.close()
            print("Closing in 4 seconds")
            time.sleep(4)
            turtle.bye()
            quit()
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
        try:
            if ((7 - j), i) in Move_Validation.validation(turn1, selection, board):
                if not (board[7 - j][i][0] == turn1[0]):
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
                    job3(oppname + "'s turn")
                    board1 = copy.deepcopy(board)
                    if turn1 == "white":
                        if Move_Validation.is_check("black", board):
                            job3(oppname + "'s turn" + "\n" + "Check")
                            if Move_Validation.check_mate("black", board):
                                job3("Checkmate" + "\n" + uname + " wins!")
                                cli_sock.send(na.encode()), checkmate()
                    else:
                        if Move_Validation.is_check("white", board):
                            job3(oppname + "'s turn" + "\n" + "Check")
                            if Move_Validation.check_mate("white", board):
                                job3("Checkmate" + "\n" + uname + " wins!")
                                cli_sock.send(na.encode()), checkmate()
                    board = board1
                    cli_sock.send(na.encode())
                    return
                selection.clear()
                return
            selection.clear()
            return
        except Exception as x:
            print(x)
            pass
        selection.clear()
        return
    elif len(selection) == 0 and (turn == "white"):
        if board[7 - j][i] != "00" and board[7 - j][i][0] == turn1[0]:
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
thread_receive = threading.Thread(target=receive)
thread_receive.start()
turtle.onscreenclick(pvp, 1)
turtle.listen()
turtle.mainloop()
