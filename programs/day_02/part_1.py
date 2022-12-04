from common import *


class Move_list:
    def __init__(self, rock, paper, scissors):
        self.rock = rock
        self.paper = paper
        self.scissors = scissors


class Part_1(BaseClass):

    def __init__(self):
        super().__init__(2)

    # Rock:         A (opponent), X (me)
    # Paper:        B (opponent), Y (me)
    # Scissors:     C (opponent), Z (me)
    opponent_move_list = Move_list("A", "B", "C")
    my_move_list = Move_list("X", "Y", "Z")

    # Loss: 0 points
    # Tie: 3 points
    # Win: 6 points
    loss_points = 0
    tie_points = 3
    win_points = 6

    # Bonus points
    # Rock: 1 points
    # Paper: 2 points
    # Scissors: 3 points
    bonus_points = {
        my_move_list.rock: 1,
        my_move_list.paper: 2,
        my_move_list.scissors: 3
    }

    # 2-level dictionary:
    #   - first key: opponent's move
    #   - second key: my move
    #   - value: result in points
    resultDictionary = {
        opponent_move_list.rock: {
            my_move_list.rock: tie_points,
            my_move_list.paper: win_points,
            my_move_list.scissors: loss_points
        },
        opponent_move_list.paper: {
            my_move_list.rock: loss_points,
            my_move_list.paper: tie_points,
            my_move_list.scissors: win_points
        },
        opponent_move_list.scissors: {
            my_move_list.rock: win_points,
            my_move_list.paper: loss_points,
            my_move_list.scissors: tie_points
        }
    }

    def execute_internal(self, filepath):
        round_list = open_file_lines(filepath)
        points = 0

        for cur_round in round_list:
            opponent_move, my_move = cur_round.split(" ")
            points += self.resultDictionary[opponent_move][my_move]
            points += self.bonus_points[my_move]

        return points


p1 = Part_1()
p1.test(15)
p1.execute()

