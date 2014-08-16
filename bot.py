import time
import json
from game import Game
from navigation import navigate
from navigation import get_direction
from navigation import find_path
import random


class VahagnBot(Bot):
    """
    Simple bot that goes to the nearest mine, or to the nearest tavern if HP < 50.
    """
    def move(self, state):
        self.game = Game(state)
        if self.game.player.life < 50:
            return self.go_to_tavern()
        else:
            return self.go_to_next_mine()

    def go_to_tavern(self):
        return self.go_to_closest(self.game.taverns_locs)

    def go_to_next_mine(self):
        possible_locations = [mine for mine, owner in self.game.mines_locs.iteritems()
                              if owner != self.game.player.id]
        return self.go_to_closest(possible_locations)

    def go_to_closest(self, possible_locations):
        paths = [find_path(self.game.player.position, loc, self.game.board) for loc in possible_locations]
        path_to_follow, shortest_length = None, 3 * self.game.board.size
        for path in paths:
            if 0 < len(path) < shortest_length:
                shortest_length, path_to_follow = len(path), path
        if path_to_follow is None:
            return 'Stay'
        aim = get_direction(path_to_follow[0], path_to_follow[1])
        return aim

