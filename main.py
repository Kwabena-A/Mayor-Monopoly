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
# ActionCard("Test", ActionType(0, set_status="Get out of Jail Free", ownable=True)).land_on(player1)

# ActionCard("Test", ActionType(0, set_status="Jail", move_to="Jail")).land_on(player1)

def main():
    turn = 0
    while True:
        display_board(board_spaces, players)
        current_player = players[turn]

        if current_player.status == "in Jail": # Pay out jail
            if input("Leave jail? (Y/N)").lower() == "y":
                current_player.leave_jail()

        while True: # Dev Custom movement option
            try:
                movement = int(input(f"Current Turn ({current_player.name}) ({current_player.status}): "))
            except ValueError:
                pass
            else:
                break


        matching = False
        if movement < 0: # Random Roll.
            movement, matching = dice.roll()

        if current_player.status == "Active": # Regular Movement
            current_player.update_location(movement)
        elif current_player.status == "in Jail" and matching: # Jailed. Free Exit.
            current_player.update_location(movement)
            current_player.status = "Active"
            matching = False
        elif current_player.status == "in Jail" and not matching: # Jailed. Missed Exit.
            current_player.jail_rolls += 1
            if current_player.jail_rolls == 3:
                current_player.leave_jail()
                current_player.update_location(movement)

        if not matching: # Update Turn
            turn = turn + 1 if turn + 1 < len(players) else 0

        display_board(board_spaces, players)

        print("""
1. Upgrade Property\t2. Downgrade Property
3. Use Card\t\t\t4. View Properties
5. Offer Trade\t\t6. End Turn""")

        while True:  # Player Custom movement option
            try:
                decision = int(input(f"Current Turn ({current_player.name}) ({current_player.status}): "))

                if decision in [1, 2, 3]:  # Upgrade Property/Use Card
                    print(*[f"{current_player.ownership.index(x)}. {x}\n" for x in current_player.ownership])
                    try:
                        property_indx = int(input("Select a property (Non-int to exit): "))
                        assert property_indx < len(current_player.ownership)
                    except ValueError or AssertionError:
                        print("Invalid Property")
                        continue

                    if decision == 1 and isinstance(current_player.ownership[property_indx], PropertyCard):
                        current_player.upgrade_property(current_player.ownership[property_indx])

                    elif decision == 2 and isinstance(current_player.ownership[property_indx], PropertyCard):
                        current_player.downgrade_property(current_player.ownership[property_indx])

                    elif decision == 3 and isinstance(current_player.ownership[property_indx], ActionType):
                        current_player.ownership[property_indx].used(current_player)

                    else:
                        print("Passed Wrong card type")

                    continue

                elif decision == 4:
                    print(current_player.all_info())
                elif decision == 5:
                    other_players = [f"{x}. {players[x]}\t" for x in range(len(players))]
                    print(*other_players)
                    try:
                        other_player = players[int(input("Select a property (Non-int to exit): "))]
                        assert other_player != current_player
                    except ValueError or IndexError or AssertionError:
                        print("Invalid Player")
                        continue
                    print()
                    current_player.offer_trade(other_player)

                elif decision == 6:
                    break
            except ValueError:
                pass



        sleep(0.5)

if __name__ == "__main__":
    main()