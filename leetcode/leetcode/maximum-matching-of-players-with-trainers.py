class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        play = 0
        tra =0
        match =0
        while play <len(players) and tra< len(trainers):
            if trainers[tra] >= players[play]:
                match +=1
                play +=1
                tra +=1
            else:
                tra +=1
        return match
            