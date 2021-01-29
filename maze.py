from random import randint
from player import Player


class Maze:
    """ class maze"""

    def __init__(self, filepath: str):
        # store maze in a 2d array
        self.maze = []
        self.emptySpots = []

        line_num = 0
        for line in open(filepath):
            # self.maze.append([char for char in line if char != "\n"])
            # list comprehension if we cant do self.emptySpots hack
            col_num = 0
            row = []
            for char in line:
                if not char == "\n":
                    row.append(char)
                if char == " ":
                    self.emptySpots.append((line_num, col_num))
                col_num += 1
            line_num += 1
            self.maze.append(row)
        player1 = Player([])


    def can_move_to(self, l_num: int, c_num: int) -> bool:
        """
        Returns whether space is wall or not
        """
        if self.maze[l_num][c_num] == "X":
            return True
        else:
            return 

    def display(self):
        """ Prints visual representation of maze"""
        for line in self.maze:
            print(line)

    def find_random_spot(self):
        """Find Random spot in maze that contains a non-X spot"""

        # method1: Hacks
        return self.emptySpots[randint(0, len(self.emptySpots)-1)]

        # method 2: total randomness
        # while True:
        #     # generate random int from 0 to number of items per row
        #     row = randint(0, len(self.maze[0])-1)
        #     # generate random int from 0 to number of rows
        #     col = randint(0, len(self.maze)-1)
        #     if self.check(row, col):
        #         return True
            # goes on infinitely until this condition met
    

    def is_item(self, l_num: int, c_num: int) -> bool:
        """ Checks to see if the position contains an item """
        items_list = ["A", "D", "E", "R"]
        if self.maze[l_num][c_num] in items_list:
            return True

    def is_exit(self, row_num: int, column_num:int) -> bool:
        """Checks if the position is an exit"""
        if self.maze[row_num][column_num] == "E":
            return True

    def track_player(self):
        """Finds where the player is"""
        row_num = 0
        for line in self.maze:
            row_num+=1
            col_num =0
            for item in line:
                col_num+=1
                if item == "P":
                    return(row_num-1, col_num-1)



if __name__ == "__main__":
    maze = Maze("test.txt")
    maze.display()
    maze.track_player()
    print(maze.find_random_spot())


