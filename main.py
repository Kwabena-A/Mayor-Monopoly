from card import PropertyCard, ActionCard, Space
from player import Player
from inits import board_spaces
from utils import display_board
from time import sleep
from dice import Dice

player1 = Player("KB", board_spaces)
player2 = Player("Major", board_spaces)

players = [player1, player2]
dice = Dice(2)

from card import ActionType
ActionCard("Test", ActionType(0, set_status="Get out of Jail Free", ownable=True)).land_on(player1)

ActionCard("Test", ActionType(0, set_status="Jail", move_to="Jail")).land_on(player1)

print(*board_spaces)
def main():
    turn = 0
    while True:
        display_board(board_spaces, players)
        current_player = players[turn]
        movement = int(input(f"Current Turn ({current_player.name}) ({current_player.status}): "))
        matching = False
        if movement == -1: # Random Roll.
            movement, matching = dice.roll()
        if movement == -2: # Upgrade Property/Use Card
            print(*[f"{current_player.ownership.index(x)}. {x}\n" for x in current_player.ownership])
            property_indx = int(input("Select a property: "))
            if isinstance(current_player.ownership[property_indx], PropertyCard):
                current_player.upgrade_property(current_player.ownership[property_indx])
            elif isinstance(current_player.ownership[property_indx], ActionType):
                current_player.ownership[property_indx]: ActionType
                current_player.ownership[property_indx].used(current_player)
        if movement == -3: # Downgrade Property.
            print(*[f"{current_player.ownership.index(x)}. {x}\n" for x in current_player.ownership])
            property_indx = int(input("Select a property: "))
            current_player.downgrade_property(current_player.ownership[property_indx])
        if movement == -4: # Leave Jail
            current_player.leave_jail()
            current_player.update_location(movement)

        if movement >= 0:
            if current_player.status == "Active": # Regular Movement
                current_player.update_location(movement)
            elif current_player.status == "in Jail" and matching: # Jailed. Free Exit.
                current_player.update_location(movement)
                matching = False
            elif current_player.status == "in Jail" and not matching: # Jailed. Missed Exit.
                current_player.jail_rolls += 1
                if current_player.jail_rolls == 3:
                    current_player.leave_jail()
                    current_player.update_location(movement)

            if not matching:
                turn = turn + 1 if turn + 1 < len(players) else 0
                print(turn)
        sleep(1.5)

if __name__ == "__main__":
    main()