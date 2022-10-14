"""
Go to word and replace("■", "#")
"""


labyrinth_raw_copied_image_from_page = """
■☺■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
■   ■       ■   ■           ■             ■                   ■       ■ ■       ■
■■■ ■■■ ■ ■■■ ■ ■ ■■■■■■■■■ ■ ■ ■■■■■ ■■■■■ ■■■ ■■■■■■■■■■■■■ ■■■■■ ■ ■ ■ ■■■ ■ ■
■ ■   ■ ■ ■   ■   ■       ■   ■   ■   ■   ■   ■       ■   ■   ■   ■ ■ ■   ■   ■ ■
■ ■■■ ■■■ ■ ■■■■■■■■■■■ ■ ■■■■■■■ ■■■■■ ■ ■■■ ■■■■■■■ ■ ■ ■ ■■■ ■ ■ ■ ■■■■■ ■■■■■
■   ■   ■   ■         ■ ■       ■       ■   ■   ■     ■ ■ ■   ■ ■ ■ ■     ■ ■   ■
■■■ ■■■ ■ ■■■ ■■■ ■■■ ■ ■■■ ■■■ ■■■■■■■ ■ ■■■ ■■■ ■■■■■ ■ ■■■ ■ ■ ■ ■■■■■ ■ ■ ■ ■
■   ■ ■ ■ ■   ■   ■   ■   ■   ■   ■   ■ ■ ■   ■   ■   ■ ■   ■ ■ ■   ■     ■ ■ ■ ■
■ ■ ■ ■ ■ ■■■■■ ■■■ ■■■■■■■ ■ ■■■ ■ ■ ■■■ ■ ■■■ ■■■ ■ ■ ■■■ ■ ■ ■■■■■ ■■■■■ ■ ■ ■
■ ■ ■   ■       ■         ■ ■ ■ ■ ■ ■     ■   ■ ■   ■ ■   ■   ■   ■ ■ ■   ■   ■ ■
■ ■■■ ■■■■■■■■■■■■■■■■■■■ ■ ■ ■ ■ ■ ■■■■■■■■■ ■ ■ ■■■ ■■■ ■■■■■■■ ■ ■ ■ ■ ■■■■■ ■
■   ■ ■   ■         ■     ■ ■ ■   ■ ■         ■ ■ ■ ■ ■ ■ ■       ■ ■ ■ ■       ■
■■■ ■ ■ ■ ■ ■■■■■■■ ■ ■■■■■ ■ ■ ■■■ ■ ■■■■■■■■■ ■ ■ ■ ■ ■ ■■■ ■■■■■ ■ ■ ■■■■■■■ ■
■   ■   ■   ■     ■ ■   ■   ■ ■ ■ ■   ■   ■     ■ ■   ■ ■ ■   ■   ■   ■       ■ ■
■ ■ ■■■■■■■■■ ■■■ ■ ■■■ ■■■ ■ ■ ■ ■■■■■ ■■■ ■■■■■ ■ ■■■ ■ ■ ■■■ ■ ■ ■■■ ■■■■■ ■■■
■ ■ ■   ■     ■ ■ ■   ■   ■ ■ ■     ■   ■   ■   ■ ■     ■ ■     ■ ■ ■       ■   ■
■ ■■■ ■ ■ ■ ■■■ ■ ■■■ ■■■ ■■■ ■■■■■ ■ ■ ■ ■■■ ■ ■ ■ ■■■■■ ■ ■■■■■ ■ ■■■■■■■■■■■ ■
■     ■   ■ ■     ■   ■ ■     ■ ■   ■ ■ ■ ■   ■ ■ ■ ■     ■     ■ ■   ■       ■ ■
■ ■■■■■■■■■ ■■■■■ ■ ■■■ ■■■■■■■ ■ ■■■ ■■■ ■ ■■■ ■ ■ ■ ■■■■■ ■■■■■ ■■■ ■ ■■■■■ ■ ■
■ ■       ■ ■   ■ ■ ■   ■     ■ ■ ■   ■   ■ ■     ■ ■   ■   ■   ■   ■   ■   ■ ■ ■
■■■ ■■■■■ ■ ■ ■ ■■■ ■ ■■■ ■ ■ ■ ■ ■■■ ■ ■■■ ■ ■■■■■■■■■ ■ ■■■ ■ ■■■ ■■■■■ ■ ■ ■ ■
■   ■   ■ ■   ■ ■   ■     ■ ■   ■   ■ ■ ■   ■   ■       ■ ■ ■ ■   ■   ■   ■ ■   ■
■ ■■■ ■ ■ ■■■■■ ■ ■■■■■■■ ■ ■■■■■■■ ■ ■ ■ ■ ■■■ ■ ■■■■■■■ ■ ■ ■■■ ■■■ ■ ■■■ ■■■ ■
■   ■ ■         ■   ■   ■ ■   ■   ■   ■ ■ ■ ■   ■     ■     ■ ■ ■     ■ ■     ■ ■
■ ■ ■■■■■■■■■■■ ■■■ ■ ■ ■ ■■■ ■ ■ ■■■ ■ ■■■ ■■■■■■■■■ ■■■■■■■ ■ ■■■■■■■■■ ■■■ ■ ■
■ ■ ■   ■       ■ ■   ■ ■   ■   ■     ■   ■   ■   ■   ■       ■           ■   ■ ■
■ ■ ■ ■ ■■■ ■■■■■ ■■■■■ ■■■■■■■ ■■■■■■■■■ ■ ■ ■ ■ ■ ■■■ ■■■■■■■■■ ■■■ ■■■■■ ■■■ ■
■ ■   ■   ■       ■   ■   ■   ■     ■     ■ ■ ■ ■   ■   ■   ■   ■   ■     ■ ■   ■
■ ■■■■■■■ ■■■■■■■ ■ ■ ■■■ ■ ■ ■■■■■ ■ ■■■■■■■ ■ ■■■■■ ■■■ ■ ■ ■ ■■■■■■■■■ ■ ■ ■■■
■   ■   ■ ■   ■     ■ ■   ■ ■     ■ ■ ■       ■   ■   ■   ■   ■ ■         ■ ■   ■
■ ■■■ ■ ■ ■ ■ ■■■■■■■ ■ ■■■ ■■■■■ ■■■ ■ ■■■■■ ■■■ ■ ■ ■ ■■■■■■■ ■ ■■■■■■■ ■■■■■ ■
■ ■   ■   ■ ■   ■     ■ ■   ■         ■   ■ ■ ■   ■ ■ ■     ■     ■       ■     ■
■ ■ ■■■■■ ■ ■■■ ■■■■■■■ ■ ■ ■■■■■■■■■■■■■ ■ ■ ■ ■■■■■ ■ ■■■ ■■■■■■■ ■■■■■■■ ■■■■■
■ ■     ■ ■   ■         ■ ■ ■     ■       ■ ■ ■     ■ ■   ■     ■         ■     ■
■ ■■■■■ ■■■■■ ■■■■■■■■■■■■■ ■ ■■■ ■ ■■■ ■■■ ■ ■■■■■ ■ ■■■ ■■■■■ ■■■■■■■ ■■■■■■■ ■
■     ■     ■ ■               ■   ■ ■ ■ ■ ■     ■   ■   ■ ■   ■     ■   ■     ■ ■
■■■■■ ■■■ ■■■ ■■■■■ ■■■■■ ■■■■■ ■■■ ■ ■ ■ ■ ■■■■■ ■■■■■ ■ ■ ■ ■■■■■ ■■■■■ ■■■ ■ ■
■ ■   ■ ■   ■     ■ ■   ■ ■     ■   ■ ■ ■   ■     ■     ■   ■   ■ ■ ■     ■ ■   ■
■ ■ ■■■ ■■■ ■■■■■ ■■■ ■ ■■■ ■■■■■ ■■■ ■ ■■■■■ ■■■■■■■ ■■■■■■■■■ ■ ■ ■ ■■■■■ ■■■■■
■         ■           ■     ■         ■               ■           ■             ■
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■♥■
"""

a = ['# ###############################################################################',
     '#   #       #   #           #             #                   #       # #       #',
     '### ### # ### # # ######### # # ##### ##### ### ############# ##### # # # ### # #',
     '# #   # # #   #   #       #   #   #   #   #   #       #   #   #   # # #   #   # #',
     '# ### ### # ########### # ####### ##### # ### ####### # # # ### # # # ##### #####',
     '#   #   #   #         # #       #       #   #   #     # # #   # # # #     # #   #',
     '### ### # ### ### ### # ### ### ####### # ### ### ##### # ### # # # ##### # # # #',
     '#   # # # #   #   #   #   #   #   #   # # #   #   #   # #   # # #   #     # # # #',
     '# # # # # ##### ### ####### # ### # # ### # ### ### # # ### # # ##### ##### # # #',
     '# # #   #       #         # # # # # #     #   # #   # #   #   #   # # #   #   # #',
     '# ### ################### # # # # # ######### # # ### ### ####### # # # # ##### #',
     '#   # #   #         #     # # #   # #         # # # # # # #       # # # #       #',
     '### # # # # ####### # ##### # # ### # ######### # # # # # ### ##### # # ####### #',
     '#   #   #   #     # #   #   # # # #   #   #     # #   # # #   #   #   #       # #',
     '# # ######### ### # ### ### # # # ##### ### ##### # ### # # ### # # ### ##### ###',
     '# # #   #     # # #   #   # # #     #   #   #   # #     # #     # # #       #   #',
     '# ### # # # ### # ### ### ### ##### # # # ### # # # ##### # ##### # ########### #',
     '#     #   # #     #   # #     # #   # # # #   # # # #     #     # #   #       # #',
     '# ######### ##### # ### ####### # ### ### # ### # # # ##### ##### ### # ##### # #',
     '# #       # #   # # #   #     # # #   #   # #     # #   #   #   #   #   #   # # #',
     '### ##### # # # ### # ### # # # # ### # ### # ######### # ### # ### ##### # # # #',
     '#   #   # #   # #   #     # #   #   # # #   #   #       # # # #   #   #   # #   #',
     '# ### # # ##### # ####### # ####### # # # # ### # ####### # # ### ### # ### ### #',
     '#   # #         #   #   # #   #   #   # # # #   #     #     # # #     # #     # #',
     '# # ########### ### # # # ### # # ### # ### ######### ####### # ######### ### # #',
     '# # #   #       # #   # #   #   #     #   #   #   #   #       #           #   # #',
     '# # # # ### ##### ##### ####### ######### # # # # # ### ######### ### ##### ### #',
     '# #   #   #       #   #   #   #     #     # # # #   #   #   #   #   #     # #   #',
     '# ####### ####### # # ### # # ##### # ####### # ##### ### # # # ######### # # ###',
     '#   #   # #   #     # #   # #     # # #       #   #   #   #   # #         # #   #',
     '# ### # # # # ####### # ### ##### ### # ##### ### # # # ####### # ####### ##### #',
     '# #   #   # #   #     # #   #         #   # # #   # # #     #     #       #     #',
     '# # ##### # ### ####### # # ############# # # # ##### # ### ####### ####### #####',
     '# #     # #   #         # # #     #       # # #     # #   #     #         #     #',
     '# ##### ##### ############# # ### # ### ### # ##### # ### ##### ####### ####### #',
     '#     #     # #               #   # # # # #     #   #   # #   #     #   #     # #',
     '##### ### ### ##### ##### ##### ### # # # # ##### ##### # # # ##### ##### ### # #',
     '# #   # #   #     # #   # #     #   # # #   #     #     #   #   # # #     # #   #',
     '# # ### ### ##### ### # ### ##### ### # ##### ####### ######### # # # ##### #####',
     '#         #           #     #         #               #           #             #',
     '############################################################################### #']

print(a[40][80]) # last position

class Labyrinth:
    def __init__(self):
        # L=Levo | R=Desno | D=Dol | G=Gor (Primer: DDRGLLGDR)
        # L=Left | R=Right | D=Down | U=Up (Primer: DDRULLGDR)
        self.directions = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1) }
        self.initial_step = self.start()
        self.path = [self.initial_step, (2,2)]
        self.intersections = []

    def open_file(self):
        with open("path.txt", "r", encoding="utf-8") as labyrinth_form_page:
            labyrinth = []
            lines = labyrinth_form_page.readlines()
            for line in lines:
                line = line.replace("■", "#")
                line = line.replace("☺", " ")
                line = line.replace("♥", " ")
                line = line.replace("\n", "")
                labyrinth.append(line)
            return labyrinth


    def labyrinth_size_x(self):
        return len(self.open_file()[0])

    def labyrinth_size_y(self):
        return len(self.open_file())

    def start(self):
        if self.open_file()[0][1] == " ":
            return 1, 0

    def finish(self):
        if self.open_file()[self.labyrinth_size_y() - 1][self.labyrinth_size_x() - 2] == " ":
            return self.labyrinth_size_x() - 2, self.labyrinth_size_y() - 1

    # from (x, y) get if it is " " or #
    def get_any_points_symbol(self, x, y):
        return self.open_file()[y][x]

    # free directions
    #need to specif previous stem (x, y)
    #direction need to be string "L" = left,"G" = up ,"D" = down , "R" = right
    def next_step(self, previous_step, direction):
        x0, y0 = previous_step
        x1, y1 = self.directions[direction]

        return x0 + x1, y0 + y1

    # is specified direction free
    def is_free(self, direction):
        location = self.next_step(self.path[-1], direction)
        return self.get_any_points_symbol(*location) == " "

    def one_way(self, previous_location):
        possible_steps = []
        for direction in self.directions:
            if self.is_free(direction) and previous_location not in self.path:
                print("Direction is", direction)
                possible_steps.append(self.next_step(previous_location, direction))
        if len(possible_steps) == 1:
            self.path.extend(possible_steps)
        else:
            self.intersections.extend(possible_steps)
        print(self.path)
        print(self.intersections)

    def is_not_wall(self, location):
        return self.get_any_points_symbol(*location) == " "

    def point_three_possible_step(self, point):
        three_ways = set()
        for direction in self.directions:
            if self.is_not_wall(self.next_step(point, direction)):
                three_ways.add(self.next_step(point, direction))
        return three_ways

    def crossroad(self, point):
        return len(self.point_three_possible_step(point)) == 3

    # I excluded edge - wall around labyrinth
    def all_possible_points(self):
        all_points = set()
        for x in range(1, self.labyrinth_size_x() - 1):
            for y in range(1, self.labyrinth_size_y() - 1):
                all_points.add((x, y))
        return all_points

    def all_possible_three_directions(self):
        three_directions = set()
        for point in self.all_possible_points():
            if self.is_not_wall(point) and self.crossroad(point):
                three_directions.add(point)
        return three_directions


labyrinth = Labyrinth()
# print(labyrinth.open_file())
print(labyrinth.labyrinth_size_x())
print(labyrinth.labyrinth_size_y())
print(labyrinth.start())
print(labyrinth.finish())
print(labyrinth.get_any_points_symbol(1, 1))
print(labyrinth.next_step((1, 0), "D"))
print("---------------")
print(labyrinth.is_free("D"))
print(labyrinth.one_way((2,2)))
print(labyrinth.all_possible_points())

print("---------------")
print("Next step function", labyrinth.next_step((1, 1), "R"))
print("get symbole of specified field: ", labyrinth.get_any_points_symbol(8, 0))

print(labyrinth.point_three_possible_step((9, 1)))
print(labyrinth.crossroad((9, 1)))
print(labyrinth.get_any_points_symbol(80, 40))

print("---------------")

print("All possible crossroads are: ", labyrinth.all_possible_three_directions())
print("No of all possible crossroads are: ", len(labyrinth.all_possible_three_directions()))

"""
print(labyrinth)
labyrinth = labyrinth.replace("■", "#")
print(labyrinth)
"""
