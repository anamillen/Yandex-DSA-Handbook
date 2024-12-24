"""
Вы играете в игру "Камни": игру для двух игроков с двумя наборами камней по n и m штук. 
С каждым ходом один игрок может взять один камень (из любого набора) или два камня (по одному из обоих). 
Когда камень забрали, он выходит из игры. Побеждает игрок, который заберет последний камень. 
Первый ход за вами.

Вы и ваш оппонент играете оптимально.
"""

def initialize_game(n, m):
    """Returns a 2d array n x m"""
    game = []
    for _ in range(m+1):
        game.append(list([""]*(n+1)))
    return game

def loose_or_win(n, m):
    """Determines if the player will win depending on the state of the game
    (Both players play optimally here)"""
    W = "Win"
    L = "Lose"
    game = initialize_game(n, m)
    game[0][0] = L
    # filling out the first row
    for i in range(1, n+1):
        if game[0][i-1]==W:
            game[0][i]=L
        else: # if game[0][i-1]!=W (which means that it equals L)
            game[0][i]=W

    # filling out the first column
    for j in range(1, m+1):
        if game[j-1][0]==W:
            game[j][0]=L
        else: # if game[j-1][0]!=W (which means that it equals L)
            game[j][0]=W
        
    # filling out the rest 
    for j in range(1,m+1):
        for i in range(1, n+1):

            if L not in [game[j-1][i-1], game[j][i-1], game[j-1][i]]:
                game[j][i] = L
            else:   # if any of the neighboring cases (left, upper, left-upper diagonal) is equal to L then
                game[j][i] = W
    return game[-1][-1]

# main programm
n, m = input().split()
n, m = int(n), int(m)
print(loose_or_win(n, m))





