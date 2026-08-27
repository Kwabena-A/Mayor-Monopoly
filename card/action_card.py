from .card import Card
from .action_type import ActionType
from random import choice


class ActionCard(Card):
    def __init__(self, name, action_type):
        super().__init__(name, "△")
        self.action_type = action_type


    def land_on(self, player): # Dosent account for own player yet.
        from player import Player
        assert isinstance(player, Player)

        print(f"{player} landed on {self.name}")
        if isinstance(self.action_type, ActionType):
            self.action_type.drawn(player)
        elif isinstance(self.action_type, list):
            choice(self.action_type).drawn(player)

