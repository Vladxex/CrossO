import time
import random

n = '-'
nai = [[n for i in range(3)] for j in range(3)]


def play():
    return input('GAMExO : ( press any key ) : ')


def ppr(*sam_list):
    return [print(' | ', a, ' | ', b, ' | ', c, ' | ') for a, b, c in sam_list]


def ok(x):
    return x == n


def player():
    return int(input('press ( 1 - 9 )'))-1


def bot():
    y = random.randint(0, 8)
    if nai[y//3][y % 3] == n and not nai[y//3][y % 3] == ('x' or 'o'):
        nai[y // 3][y % 3] = 'o'
    else:
        bot()


def check():
    return any(filter(ok, [*nai[0], *nai[1], *nai[2]]))


def winner():
    stroka = [[nai[i][j] for i in range(3)] for j in range(3)]
    diagonalL = nai[0][0], nai[1][1], nai[2][2]
    diagonalR = nai[0][2], nai[1][1], nai[2][0]
    for i in range(3):
        if set(nai[i]) == {'x'} or set(stroka[i]) == {'x'} or (set(diagonalL) or set(diagonalR)) == {'x'}:
            return 'Player WIN'
        elif set(nai[i]) == {'o'} or set(stroka[i]) == {'o'} or (set(diagonalL) or set(diagonalR)) == {'o'}:
            return 'Computer WIN'

def do_or_diy():
    if winner():
        print(winner())
    else:
        print('Continue')


def game():
    x = player()
    x = x % 8 if x > 8 else x
    nai[x//3][x % 3] = 'x' if nai[x//3][x % 3] == n and not nai[x//3][x % 3] == ('x' or 'o') else game()
    do_or_diy()
    bot() if check() else exit()
    ppr(*nai)
    print(winner()) if winner() else print('>>>>')
    game() if check() else exit()


game() if play() else exit()
