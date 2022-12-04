from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    # Rock:         A (opponent), X (me)
    # Paper:        B (opponent), Y (me)
    # Scissors:     C (opponent), Z (me)
    opponent_move_list = {
        "rock": "A",
        "paper": "B",
        "scissors": "C"
    }
    round_result_list = {
        "loss": "X",
        "tie": "Y",
        "win": "Z"
    }

    # Loss: 0 points
    # Tie: 3 points
    # Win: 6 points
    round_result_points = {
        round_result_list["loss"]: 0,
        round_result_list["tie"]: 3,
        round_result_list["win"]: 6
    }

    # Bonus points
    # Rock: 1 points
    # Paper: 2 points
    # Scissors: 3 points
    bonus_points_rock = 1
    bonus_points_paper = 2
    bonus_points_scissors = 3

    # 2-level dictionary:
    #   - first key: opponent's move
    #   - second key: my move
    #   - value: result in points
    resultDictionary = {
        opponent_move_list["rock"]: {
            round_result_list["loss"]: bonus_points_scissors,
            round_result_list["tie"]: bonus_points_rock,
            round_result_list["win"]: bonus_points_paper
        },
        opponent_move_list["paper"]: {
            round_result_list["loss"]: bonus_points_rock,
            round_result_list["tie"]: bonus_points_paper,
            round_result_list["win"]: bonus_points_scissors
        },
        opponent_move_list["scissors"]: {
            round_result_list["loss"]: bonus_points_paper,
            round_result_list["tie"]: bonus_points_scissors,
            round_result_list["win"]: bonus_points_rock
        }
    }

    def execute_internal(self, filepath):
        round_list = open_file_lines(filepath)
        points = 0

        for cur_round in round_list:
            opponent_move, my_result = cur_round.split(" ")
            points += self.resultDictionary[opponent_move][my_result]
            points += self.round_result_points[my_result]

        return points


p2 = Part_2()
p2.test(12)
p2.execute()
