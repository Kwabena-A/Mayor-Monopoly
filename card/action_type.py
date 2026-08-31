class ActionType():
    def __init__(self, net = 0, shared = False, move_to = "", set_status = None, ownable = False):
        self.net = net
        self.shared = shared
        self.move_to = move_to
        self.set_status = set_status
        self.ownable = ownable
        self.owned = False

    def drawn(self, player):
        from player import Player
        assert isinstance(player, Player)
        print(self.full_info())

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

        if self.ownable:
            player.ownership.append(self)
            self.owned = True

        if self.move_to != "":
            if "Jail" in self.move_to:
                player.update_location(move_to=self.move_to, skip_over=True)
            else:
                player.update_location(move_to=self.move_to, skip_over=False)

        if self.set_status and not self.ownable:
            player.status = self.set_status

    def used(self, player): # Only used by get of jail cards
        assert self.ownable
        from player import Player
        assert isinstance(player, Player)

        self.owned = False
        player.status = "Active"
        player.ownership.remove(self)

    def full_info(self) -> str:
        return f"""
                | Net: {self.net}
                | Shared: {self.shared}
                | Move To: {self.move_to}
                | Status: {self.set_status}
                """

    def __str__(self):
        return self.set_status




