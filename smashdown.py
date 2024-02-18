from typing import List
import random

class Smashdown:

    def _read_fighters(self):
        with open('smash_characters.txt', 'r') as file:
              lines = file.readlines()
        fighter_list = [line.strip() for line in lines]
        random.shuffle(fighter_list)
        return fighter_list

    def __init__(self, player_names:List[str]) -> None:
        self.players = player_names
        self.scores = {player:0 for player in self.players}
        self.fighters = self._read_fighters()
        
    def matchup(self):
        matchups = zip(self.players, self.fighters)
        self.fighters = self.fighters[len(self.players):]
        return ''.join([f'{player}: {fighter}\n' for player, fighter in matchups])

    def leaderboard(self):
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1])
        return ''.join([f'{name}: {score}\n' for name, score in sorted_scores])
    
    def remaining_fighters(self):
        return ''.join(f'{name}, ' for name in sorted(self.fighters))[:-2]





if __name__ == '__main__':
    test_smash = Smashdown(player_names=['Albin', 'Ebba'])
    print(test_smash.leaderboard())
    print(test_smash.matchup())
    print(test_smash.remaining_fighters())
    