
total_runs = 100
total_balls = 80
total_matches = 4

class CricketPlayer:
    def strike_rate(self):
       
        sr = (total_runs / total_balls) * 100
        return sr

    def average_runs(self):
      
        avg = total_runs / total_matches
        return avg

player = CricketPlayer()


player_strike_rate = player.strike_rate()
player_average = player.average_runs()


print("Total Runs:", total_runs)
print("Total Balls:", total_balls)
print("Total Matches:", total_matches)
print("Strike Rate:", round(player_strike_rate, 2))
print("Average Runs per Match:", round(player_average, 2))
