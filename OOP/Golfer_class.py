class Golfer:
    def __init__(self, name, wins, tournaments):
        self.name = name
        self.wins = wins
        self.tournaments = tournaments

    def win_percentage(self):
        if self.tournaments == 0:
            return 0
        return (self.wins / self.tournaments) * 100
    
    def tourn_wins(self):
        return f"{self.name} has won {self.wins} tournaments."
    
if __name__ == "__main__":
    golf_data = [
        ["Jack Nicklaus", 73, 595],
        ["Tiger Woods", 82, 359],
        ["Ben Hogan", 64, 300],
    ]

    golfers = []
    for data in golf_data:
        player = Golfer(data[0], data[1], data[2])
        golfers.append(player)

    for golfer in golfers:
        print(golfer.tourn_wins())
        print(f"Win percentage: {golfer.win_percentage():.2f}%\n")