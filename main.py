from card import PropertyCard, ActionCard, Space
from utils import board_spaces, display_board
from player import Player
from time import sleep
from random import randint
players = [Player("KB", board_spaces), Player("Major", board_spaces)]

def main():
    turn = 0
    while True:
        display_board(board_spaces, players)
        current_player = players[turn]
        movement = int(input(f"Current Turn ({current_player.name}): "))
        if movement == -1:
            movement = randint(2, 12)
            print(f"dice rolled: {movement}")
        current_player.update_location(movement)
        turn = turn + 1 if turn + 1 < len(players) else 0
        sleep(3)

if __name__ == "__main__":
    main()