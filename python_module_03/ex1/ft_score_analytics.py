import sys


class Score():

    def __init__(self, points: list) -> None:
        self.points = points

    def total_player(self) -> float:
        return (len(self.points))

    def total_score(self) -> float:
        return (sum(self.points))

    def average_score(self) -> float:
        return (sum(self.points)/len(self.points))

    def hight_score(self) -> float:
        return (max(self.points))

    def low_score(self) -> float:
        return (min(self.points))

    def score_range(self) -> float:
        return (max(self.points) - min(self.points))


def validate_input(arg: list) -> None:
    sum = 0
    i = 0
    try:
        while (i < len(arg)):
            sum = sum + arg[i]
            i = i + 1
    except Exception as e:
        print(e)


def ft_skip(arg: list) -> list:
    new_list = []
    i = 1
    while (i < len(arg)):
        new_list.append(int(arg[i]))
        i = i + 1
    return (new_list)


def statistics(sc: Score) -> None:
    print("Scores processed: {}".format(sc.points))
    print(f"Total players: {sc.total_player()}")
    print(f"Total score: {sc.total_score()}")
    print(f"Average score: {sc.average_score()}")
    print(f"High score: {sc.hight_score()}")
    print(f"Low score: {sc.low_score()}")
    print(f"Score range: {sc.score_range()}")


print("=== Player Score Analytics ===")
if (len(sys.argv) == 1):
    print("No scores provided. Usage: ", end="")
    print(" python3 ft_score_analytics.py <score1> <score2> ...")
else:
    sc = Score(sys.argv)
    sc.points = ft_skip(sys.argv)
    statistics(sc)
