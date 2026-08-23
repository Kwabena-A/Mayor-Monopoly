from card import Space
from player import Player


def display_board(board: list[Space], players: list[Player]):
    board_symbols = ""
    player_symbols = [[f"{" ":<3}" for x in range(len(board))] for x in range(len(players))]

    for space in board:
        board_symbols += f"{space.card.symbol:<3}"
        for player in space.currentlyOn:
            player_symbols[space.currentlyOn.index(player)][board.index(space)] = f"{player.name[0]:<3}"

    print(board_symbols)
    for row in player_symbols:
        print(" ".join(row))


