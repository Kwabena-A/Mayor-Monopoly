from player import Player
from .card import Card
from .action_type import ActionType
from random import choice


class ActionCard(Card):
    def __init__(self, name, action_type, isPassOnAction = False):
        super().__init__(name, "△")
        self.action_type = action_type
        self.isPassOnAction = isPassOnAction


    def land_on(self, player, roll): # Dosent account for own player yet.
        from player import Player
        assert isinstance(player, Player)

        print(f"{player} landed on {self.name}")
        if isinstance(self.action_type, ActionType):
            self.action_type.drawn(player)
        elif isinstance(self.action_type, list):
            while True:
                randomCard = choice(self.action_type)
                randomCard: ActionType
                if not randomCard.owned:
                    randomCard.drawn(player)
                    break

    def pass_on(self, player: Player):
        if self.isPassOnAction:
            self.action_type.drawn(player)
        else:
            super().pass_on(player)


