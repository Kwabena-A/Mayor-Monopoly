from card import PropertyCard, ActionCard, Space
from player import Player
from inits import board_spaces
from utils import display_board
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
        if movement == -1: # Random Roll.
            movement, matching = dice.roll()
        if movement == -2: # Upgrade Property.
            print(*[f"{current_player.ownership.index(x)}. {x}\n" for x in current_player.ownership])
            property_indx = int(input("Select a property: "))
            current_player.upgrade_property(current_player.ownership[property_indx])
        if movement == -3: # Downgrade Property.
            print(*[f"{current_player.ownership.index(x)}. {x}\n" for x in current_player.ownership])
            property_indx = int(input("Select a property: "))
            current_player.downgrade_property(current_player.ownership[property_indx])

        if movement >= 0:
            current_player.update_location(movement)
            if not matching:
                turn = turn + 1 if turn + 1 < len(players) else 0
        sleep(1.5)

if __name__ == "__main__":
    main()