from card import PropertyCard, ActionCard, Space
from player import Player
from utils import board_spaces, display_board
from time import sleep
from dice import Dice

players = [Player("KB", board_spaces), Player("Major", board_spaces)]
dice = Dice(2)
def main():
    turn = 0
    while True:
        display_board(board_spaces, players)
        current_player = players[turn]
        movement = int(input(f"Current Turn ({current_player.name}): "))
        matching = False
        if movement == -1:
            movement, matching = dice.roll()
        current_player.update_location(movement)
        if not matching:
            turn = turn + 1 if turn + 1 < len(players) else 0
        sleep(1.5)

if __name__ == "__main__":
    main()