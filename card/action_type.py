class ActionType():
    def __init__(self, net = 0, shared = False, move_to = "", set_status = None):
        self.net = net
        self.shared = shared
        self.move_to = move_to
        self.set_status = set_status

    def drawn(self, player):
        from player import Player
        assert isinstance(player, Player)
        print(self)

        player.update_money(self.net)

        if self.shared:
            from main import players
            if self.net < 0: # Giving Money
                for other_player in players:
                    if other_player is not player:
                        other_player.update_money(self.net / (len(players) - 1))

            else: # Collecting Money
                for other_player in players:
                    if other_player is not player:
                        other_player.update_money(self.net * -1)

                player.update_money(self.net * (len(players) - 2)) # Extra from uncollected

        if self.move_to != "":
            player.update_location(move_to=self.move_to)

        if self.set_status:
            player.status = self.set_status

    def __str__(self):
        return f"""
        | Net: {self.net}
        | Shared: {self.shared}
        | Move To: {self.move_to}
        | Status: {self.set_status}
        """




