from card import PropertyCard, ActionCard, Space
from utils import board_spaces, display_board
from player import Player

players = [Player("KB", board_spaces), Player("Major", board_spaces)]
players[0].update_location(4)
display_board(board_spaces, players)