class ActionType():
    def __init__(self, net = 0, shared = False, move_to = -1, set_status = None):
        self.net = net
        self.shared = shared
        self.move_to = move_to
        self.set_status = set_status

    def drawn(self, player):
        from player import Player
        assert isinstance(player, Player)

        player.update_money(self.net)

        if self.shared:
            from main import players
            for other_player in players:
                if other_player is not player:
                    other_player.update_money(self.net / (len(players) - 1))

        if self.move_to != -1:
            player.update_location(self.move_to, skip_over=True)

        if self.set_status:
            player.status = self.set_status




