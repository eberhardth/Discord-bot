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
        if len(self.fighters) < len(self.players):
            winner= self.get_winner()
            return f'The winner is:\n {winner}'
        
        matchups = zip(self.players, self.fighters)
        self.fighters = self.fighters[len(self.players):]
        return ''.join([f'{player}: {fighter}\n' for player, fighter in matchups])

    def leaderboard(self):
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1], reverse = True)
        return 'Leaderboard:\n' + ''.join([f'{name}: {score}\n' for name, score in sorted_scores])
    
    def get_winner(self):
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1], reverse=True)
        
        max_score = sorted_scores[0][1]
        best_players = [player for player, score in sorted_scores if score == max_score]

        if len(best_players) == 1:
            return best_players[0]
        
        elif len(best_players) == len(self.players):
            return "...it's a tie!"
        
        else:
            return sorted_scores[-1][0]


    def remaining_fighters(self):
        return ''.join(f'{name}, ' for name in sorted(self.fighters))[:-2]
    
    def add_point(self, name:str) -> bool:
        if name not in self.players:
            return False
        else:
            self.scores[name] += 1
            return True





if __name__ == '__main__':
    test_smash = Smashdown(player_names=['Albin', 'Ebba', 'Sofia'])
    print(test_smash.add_point('Albin'))
    print(test_smash.add_point('Sofia'))
    print(test_smash.leaderboard())
    print(test_smash.get_winner())
    print(test_smash.matchup())
    print(test_smash.remaining_fighters())
    