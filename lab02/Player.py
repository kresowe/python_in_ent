__author__ = 'michal'


class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.pl_id = player_id

    def get_name(self):
        return self.name

    def get_pl_id(self):
        return self.pl_id
