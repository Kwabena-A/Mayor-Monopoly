def display_board(board, players):
    from card import Space
    from player import Player

    assert isinstance(board, list)
    assert all(isinstance(x, Space) for x in board)
    board: list[Space]

    assert isinstance(players, list)
    assert all(isinstance(x, Player) for x in players)
    players: list[Player]

    print(*players)


    board_symbols = ""
    player_symbols = [[f" " for x in range(len(board))] for x in range(len(players))]

    for space in board:
        board_symbols += f"{space.card.symbol}\t"
        for player in space.currentlyOn:
            player_symbols[space.currentlyOn.index(player)][board.index(space)] = f"{player.name[0]}"

    print(board_symbols)
    for row in player_symbols:
        print("\t".join(row))


