class BreakIt(Exception): pass

import numpy as np

valid_moves = []

def rook_moves(board, i, j, a):
    global valid_moves
    t = a[0]
    jk = []
    l = [board[i][j + 1::], board[i][j - 1::-1], board[i + 1::], board[i - 1::-1]]
    for k in l:
        if l.index(k) < 2:
            for g in range(len(k)):
                v, b = j + g + 1, j - g - 1
                if k[g] == "00":
                    if l.index(k) == 0:
                        valid_moves.append((i, v))
                    elif l.index(k) == 1:
                        valid_moves.append((i, b))
                else:
                    if k[g][0] == t:
                        break
                    elif k[g][0] != t:
                        if l.index(k) == 0:
                            valid_moves.append((i, v))
                        elif l.index(k) == 1:
                            valid_moves.append((i, b))
                        break
        else:
            break
    try:
        for p in range(len(l[2])):
            for g in range(len(l[2][p])):
                if g == j:
                    n = i + p + 1
                    if l[2][p][g] == "00":
                        valid_moves.append((n, j))
                    else:
                        if l[2][p][g][0] == t:
                            raise BreakIt
                        elif l[2][p][g][0] != t:
                            valid_moves.append((n, j))
                            raise BreakIt
    except BreakIt:
        pass
    try:
        for p in range(len(l[3])):
            for g in range(len(l[3][p])):
                if g == j:
                    m = i - p - 1
                    if l[3][p][g] == "00":
                        valid_moves.append((m, j))
                    else:
                        if l[3][p][g][0] == t:
                            raise BreakIt
                        elif l[3][p][g][0] != t:
                            valid_moves.append((m, j))
                            raise BreakIt
    except BreakIt:
        pass
    for t in valid_moves:
        if t[0] < 0 or t[1] < 0 or t[0] > 7 or t[1] > 7:
            jk.append(t)
    for i in jk:
         valid_moves.remove(i)
    return valid_moves

def pawn_moves(board, i, j, a):
    jk = []
    global valid_moves
    if a[0] == "w":
        try:
            if board[i + 1][j] == "00":
                valid_moves.append((i + 1, j))
                if board[i + 2][j] == "00" and i == 1:
                    valid_moves.append((i + 2, j))
        except:
            pass
        try:
            if board[i + 1][j + 1] != "00" and board[i + 1][j + 1][0] != "w":
                valid_moves.append((i + 1, j + 1))
        except:
            pass
        try:
            if board[i + 1][j - 1] != "00" and board[i + 1][j - 1][0] != "w":
                valid_moves.append((i + 1, j - 1))
        except:
            pass
    elif a[0] == "b":
        try:
            if board[i - 1][j] == "00":
                valid_moves.append((i - 1, j))
                if board[i - 2][j] == "00" and i == 6:
                    valid_moves.append((i - 2, j))
        except:
            pass
        try:
            if board[i - 1][j + 1] != "00" and board[i - 1][j + 1][0] != "b":
                valid_moves.append((i - 1, j + 1))
        except:
            pass
        if board[i - 1][j - 1] != "00" and board[i - 1][j - 1][0] != "b":
            valid_moves.append((i - 1, j - 1))
    for t in valid_moves:
        if t[0] < 0 or t[1] < 0 or t[0] > 7 or t[1] > 7:
            jk.append(t)
    for i in jk:
         valid_moves.remove(i)
    return valid_moves

def knight_moves(board, i, j, a):
    global valid_moves
    jk = []
    moves = [(i + 1, j + 2), (i + 1, j - 2), (i - 1, j + 2), (i - 1, j - 2), (i + 2, j + 1), (i - 2, j + 1),
             (i + 2, j - 1), (i - 2, j - 1)]
    t = a[0]
    for k in moves:
        try:
            if board[k[0]][k[1]] == "00" or board[k[0]][k[1]][0] != t and k[0] > -1 and k[1] > -1:
                valid_moves.append(k)
        except:
            pass
    for t in valid_moves:
        if t[0] < 0 or t[1] < 0 or t == (-1, -1) or t[0] > 7 or t[1] > 7:
            jk.append(t)
    for i in jk:
         valid_moves.remove(i)
    return valid_moves

def king_moves(board, i, j, a):
    jk = []
    global valid_moves
    moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i+1, j+1), (i-1, j+1), (i-1, j-1), (i+1, j-1)]
    t = a[0]
    for k in moves:
        try:
            if board[k[0]][k[1]] == "00" or board[k[0]][k[1]][0] != t and k[0] > -1 and k[1] > -1:
                valid_moves.append(k)
        except:
            pass
    for t in valid_moves:
        if t[0] < 0 or t[1] < 0 or t[0] > 7 or t[1] > 7:
            jk.append(t)
    for i in jk:
         valid_moves.remove(i)

    return valid_moves

def queen_moves(board, i, j, a):
    global valid_moves
    bishop_moves(board, i, j, a)
    y = rook_moves(board, i, j, a)
    return y
def validation(turn, c, board):
    global valid_moves
    i, j = c[0]
    valid_moves = []
    a = board[i][j]

    if i > -1 and j > -1:
        if len(c) == 1:
            if a[1] == "p":
                return pawn_moves(board, i, j, a)
            elif a[1] == "r":
                return rook_moves(board, i, j, a)
            elif a[1] == "n":
                return knight_moves(board, i, j, a)
            elif a[1] == "k":
                return king_moves(board, i, j, a)
            elif a[1] == "b":
                return bishop_moves(board, i, j, a)
            elif a[1] == "q":
                return queen_moves(board, i, j, a)
        else:
            o = board[c[1][0]][c[1][1]]
            board[c[1][0]][c[1][1]] = board[i][j]
            board[i][j] = "00"
            if is_check(turn, board) != True:
                board[i][j] = board[c[1][0]][c[1][1]]
                board[c[1][0]][c[1][1]] = o
                if a[1] == "p":
                    return pawn_moves(board, i, j, a)
                elif a[1] == "r":
                    return rook_moves(board, i, j, a)
                elif a[1] == "n":
                    return knight_moves(board, i, j, a)
                elif a[1] == "k":
                    return king_moves(board, i, j, a)
                elif a[1] == "b":
                    return bishop_moves(board, i, j, a)
                elif a[1] == "q":
                    return queen_moves(board, i, j, a)
            else:
                board[i][j] = board[c[1][0]][c[1][1]]
                board[c[1][0]][c[1][1]] = o
                return []
    else:
        return []

def bishop_moves(board, i, j, a):
    jk = []
    global valid_moves
    t = a[0]
    temp = np.fliplr(board)
    b = list(np.diagonal(temp, offset=(7 - j - i)))
    lst = np.array(board)
    h = list(np.diagonal(lst, offset=(j - i)))
    o, f = h.index(board[i][j]), b.index(board[i][j])
    z, r = h[0:o][::-1], h[o + 1:]
    e, q = b[0:f][::-1], b[f + 1:]
    moves = [(z, (-1, -1)), (r, (1, 1)), (e, (-1, 1)), (q, (1, -1))]
    try:
        for k in range(len(moves)):
            for l in range(len(moves[k][0])):
                if moves[k][0][l] == "00":
                    valid_moves.append((i + (l + 1) * moves[k][1][0], j + (l + 1) * moves[k][1][1]))
                else:
                    if moves[k][0][l][0] != t:
                        valid_moves.append((i + (l + 1) * moves[k][1][0], j + (l + 1) * moves[k][1][1]))
                        break
                    elif moves[k][0][l][0] == t:
                        break
    except:
        pass
    for t in valid_moves:
        if t[0] < 0 or t[1] < 0:
            jk.append(t)
    for i in jk:
         valid_moves.remove(i)
    return valid_moves

def is_check(t, board):
    k = []
    if t == "white":
        d = "wk"
    else:
        d = "bk"
    l = 0
    for i in board:
        for j in i:
            if j != t:
                try:
                    k.extend(validation(t, [(board.index(i), board[board.index(i)].index(j))], board))
                except:
                    pass
        try:
            l = (board.index(i), board[board.index(i)].index(d))
        except:
            pass
    if l in k:
        return True
    else:
        return False

def check_mate(t, board):
    for i in board:
        for j in i:
            if j[0] == t[0]:
                for k in validation(t, [(board.index(i), i.index(j))], board):
                    o = board[k[0]][k[1]]
                    i1 = board.index(i)
                    i2 = i.index(j)
                    board[k[0]][k[1]] = board[board.index(i)][i.index(j)]
                    board[board.index(i)][i.index(j)] = "00"
                    if not is_check(t, board):
                        board[i1][i2] = board[k[0]][k[1]]
                        board[k[0]][k[1]] = o
                        return False
                    else:
                        board[i1][i2] = board[k[0]][k[1]]
                        board[k[0]][k[1]] = o
    return True



