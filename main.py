"""
Go to word and replace("■", "#")
"""
import collections

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

print(a[40][79]) # last position

class Labyrinth:
    def __init__(self):
        # L=Levo | R=Desno | D=Dol | G=Gor (Primer: DDRGLLGDR)
        # L=Left | R=Right | D=Down | U=Up (Primer: DDRULLGDR)
        self.directions = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1) }
        self.initial_step = self.start()
        self.all_crossroads_absolute = self.all_crossroads()
        self.removed_crossroads = set()
        self.non_crossroads_anymore = {}
        self.first_position = self.start()
        self.last_position = self.finish()
        self.two_connected_crossroads = set()  # two connected crossroads dead crossroads in between
        self.current_branch = []
        self.path = [self.initial_step, (2,2)]
        self.intersections = []

    def open_file(self):
        with open("path.txt", "r", encoding="utf-8") as labyrinth_form_page:
            labyrinth = []
            lines = labyrinth_form_page.readlines()
            for line in lines:
                line = line.replace("■", "#")
                # change those tvo replace with space
                line = line.replace("☺", "#")
                line = line.replace("♥", "#")
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

    # first crossroad on map
    def find_first_crossroad(self, first_step=(1, 1), start=(1, 0)):
        return self.branch_path(first_step, start)[-1][0]

    # find last crossroad
    def find_last_crossroad(self, last_step=(79, 39), finish=(79, 40)):
        return self.branch_path(last_step, finish)[-1][0]

    # free directions
    #need to specif previous stem (x, y)
    #direction need to be string "L" = left,"G" = up ,"D" = down , "R" = right
    def next_step(self, previous_step, direction):
        x0, y0 = previous_step
        x1, y1 = self.directions[direction]
        return x0 + x1, y0 + y1

    def is_not_wall(self, location):
        return self.get_any_points_symbol(*location) == " "

    # you can move in three directions from crossroad - return all three directions from crossroad
    # write in one line...
    # duplicate of self.point_three_possible_step()
    def step_all_directions(self, your_location):
        all_possible_next_steps = set()
        for direction in self.directions:
            if self.is_not_wall(self.next_step(your_location, direction)):
                all_possible_next_steps.add(self.next_step(your_location, direction))
        return all_possible_next_steps

    # Function return tuple for detected crossroad, location of next valid state or None for hitting the wall
    def useful_step(self, your_location, crossroad_location):
        next_step = list(self.step_all_directions(your_location))  # all possible steps from current location
        for possible_steps in next_step:
            if possible_steps == crossroad_location:
                next_step.remove(crossroad_location)
        if len(next_step) > 1:
            print("We reached Crossroad, Crossroad location is: ", your_location)
            return your_location, next_step
        elif len(next_step) == 1:
            return next_step[0]
        else:
            print("We hit the wall, blind road detected")
            return None

    # return all points
    # if last is None - blind road
    # if last tuple with info about crossroad - crossroad

    def branch_path(self, your_location, crossroad):
        current_branch_local = [crossroad, your_location]
        # continue if last element is not None and is tuple with two numbers
        while current_branch_local[-1] and type(current_branch_local[-1][0]) == int:
            # print(current_branch_local)
            self.useful_step(current_branch_local[-1], current_branch_local[-2])
            current_branch_local.append(self.useful_step(current_branch_local[-1], current_branch_local[-2]))
        return current_branch_local

    # three options one/two/three road(s) lead to crossroad
    # collect dict with all three options
    def all_path_from_crossroad(self, crossroad):
        all_path = collections.defaultdict(list)
        possible_directions = set(self.point_three_possible_step(crossroad))
        for possible_direction_coordinate, direction in possible_directions:
            print(possible_direction_coordinate)
            branch_path = (self.branch_path(possible_direction_coordinate, crossroad), direction)
            all_path[possible_direction_coordinate] = branch_path
        return crossroad, all_path

    def use_data_from_all_path(self, crossroad):
        reachable_crossroads = []
        crossroad, all_path = self.all_path_from_crossroad(crossroad)
        for first_step, path in all_path.items():
            # in path is direction too (which way yu need to turn in crossroad
            if type(path[0][-1]) == tuple:
                reachable_crossroads.append(path[0][-1])
        if len(reachable_crossroads) == 1:
            print("We find dead crossroad")
            self.non_crossroads_anymore[reachable_crossroads[0][0]] = reachable_crossroads[0][1]
            self.removed_crossroads.add(crossroad)
        return reachable_crossroads

    # one way crossroad other way blind street
    # send reached crossroad to non_crossroads_anymore
    # first you need to fill data in self.non_crossroads_anymore
    # call self.go_through first
    # delete all crossroad reach from non crossroads and
    def use_data_from_non_crossroads_anymore(self):
        non_crossroad_data = collections.defaultdict(list)
        reachable_crossroads_from_non_crossroad = []
        self.go_through()
        for non_crossroad, two_path in self.non_crossroads_anymore.items():
            for path in two_path:
                branch = self.branch_path(path, non_crossroad)
                non_crossroad_data[non_crossroad].append(branch)
        return non_crossroad_data

    # go through both ways in non-crossroads anymore
    # find all crossroads that become non crossroads
    def remap_non_crossroad_and_all_crossroads(self):
        for non_crossroad, two_ways in self.use_data_from_non_crossroads_anymore().items():
            way_1 = two_ways[0]
            way_2 = two_ways[1]
            # print("Way 1: ", way_1)
            # print("Way 2: ", way_2)
            if not way_1[-1]:
                print(way_2[-1])

            if not way_2[-1]:
                print(way_1[-1])

            # for way in two_ways:
            #     if not way[-1]:
            #         print(way[0])
            #     else:
            #         print("ELSEEEEEEEEEEEE", way)

        # for non_crossroad, path in non_crossroad_data.items():
        #     # in path is direction too (which way yu need to turn in crossroad
        #     if type(path[0][-1]) == tuple:
        #         reachable_crossroads_from_non_crossroad.append(path[0][-1])
        # if len(reachable_crossroads_from_non_crossroad) == 1:
        #     print("We find dead crossroad")
        #     self.non_crossroads_anymore[reachable_crossroads_from_non_crossroad[0][0]] = reachable_crossroads_from_non_crossroad[0][1]
        #     self.removed_crossroads.add(crossroad)
        # return reachable_crossroads_from_non_crossroad

    # loop through all crossroads
    def go_through(self):
        for crossroad in self.all_crossroads_absolute:
            print(crossroad)
            self.use_data_from_all_path(crossroad)
        self.removed_crossroads.remove(self.find_first_crossroad())  # first crossroad that lead from start
        self.removed_crossroads.remove(self.find_last_crossroad())  # last crossroad next to finish
        print(self.removed_crossroads)
        return len(self.removed_crossroads)

    # when you come to crossroad you need to know witch directions you took

    # def delete_crossroad(self, crossroad):
    #     if len(self.use_data_from_all_path()) == 1:
    #

    # def next_valid_step(self, possible_ways):
    #     self.current_branch.append(possible_ways)
    #     for direction in self.directions:
    #         next_step = self.next_step(self.current_branch[-1], direction)
    #         if self.is_not_wall(next_step) or next_step in self.current_branch:
    #             self.current_branch.append(next_step)
    #         else:
    #             return self.current_branch[0]

    # function return next step (coordinate) is there is only one option where to go, if hit the wall return None
    def step_by_step(self, previous_location, crossroad):
        for direction in self.directions:
            next_step = self.next_step(previous_location, direction)
            if self.is_not_wall(next_step) and next_step != crossroad:
                if next_step in self.all_crossroads_absolute:   # optimise this part of code it takes 5 seconds to get data
                    print("We hit another crossroad")
                else:
                    return next_step
            else:
                print("I hit the wall")

    # is specified direction free
    def is_free(self, direction):
        location = self.next_step(self.path[-1], direction)
        return self.get_any_points_symbol(*location) == " "

    # return start of one way dead roads
    def dead_road_start_coordinates(self, start, crossroad):
        where_i_come_from = crossroad
        #stop if you hit crossroad or wall
        while ...:
            for direction in self.directions:
                next_step = self.next_step(where_i_come_from, direction)
        # pojdi naprej, če ni stene in če nisi iz tam prišel

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

    # direction in possible steps that i know which way I took
    def point_three_possible_step(self, point):
        three_ways = set()
        for direction in self.directions:
            if self.is_not_wall(self.next_step(point, direction)):
                three_ways.add((self.next_step(point, direction), direction))
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

    def all_crossroads(self):
        # add start and finish to all crossroads
        three_directions = set()  # {(1, 0), (40, 79)}
        for point in self.all_possible_points():
            if self.is_not_wall(point) and self.crossroad(point):
                three_directions.add(point)
        return three_directions

        # zapomneš si kje si bil - to je corssroad
        # dve poti imaš - greš pač kontra od crossroada - tja kjer greš edino lahko
        # če ne moreš iti naprej si v slepi ulici
        # če si slučajno na (1, 0) ali na (40, 79)} javi da si povezal konec ali začetek
        # pojdi gledat še ostale dve smeri
        # prideš pri dveh od treh ugotoviš da si v slepi ulici potem izbriši ta križišče
        # tretji poti pridi do sorodnjega križišča in tistemu izbij eno od poti stran
        # potem pa na temu drugemu križišču ki si mu izbil eno pot poglej če sta na obeh možnih smereh krišišča
        # če je na eni strani slepa ulica to križišče izbriši in pojdi do naslednjega
        # v naslednjem poglej ali po obeh poteh prideš do križišča - če ja si zapomni katera sta povezaa križišča
        # krake teh križišč primerjaj z drugimi povezanimi križišči da vidiš če kje lahko povežeš
        # če sta dva povezljiva imaš kačo, verigo in izločiš še eno pot med njima
        # če se dva križišča lahko povežeta je to sigurno edina pot, pomeni da imaš daljši kačo

    #
    # def one_branch(self, previous_location, crossroad):
    #     self.current_branch
    #     ...
    #

    def crossroads_with_two_blind_alleys(self, crossroad=(7,1)):
        possible_directions = set(self.point_three_possible_step(crossroad))
        for possible_direction in possible_directions:
            self.step_by_step(possible_direction, crossroad)

        return possible_directions

    # 1. hit the wall
    # 2. hit the crossroad
    # 3. hit self.start()
    # 4. hit self.finish()
    # goal is to remove dead crossroads from all_crossroads
    # and to connect alive crossroads


    def connect_two_crossroads(self):
        ...

labyrinth = Labyrinth()
# print(labyrinth.open_file())
print(labyrinth.labyrinth_size_x())
print(labyrinth.labyrinth_size_y())
print(labyrinth.first_position)
print(labyrinth.last_position)
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

print("All possible crossroads are: ", labyrinth.all_crossroads_absolute)
print("No of all possible crossroads are: ", len(labyrinth.all_crossroads_absolute))

# print("Two blind streets", labyrinth.crossroads_with_two_blind_alleys())

print(labyrinth.step_by_step((6, 1), (7, 1)))
print(labyrinth.step_all_directions((9, 1)))
print("Useful step, next valid step is: ", labyrinth.useful_step((9, 1), (8, 1)))

print("Branch path", labyrinth.branch_path((8, 1), (7, 1)))
print("--------------------------------------------------------------------------------------")
print("all_path_from_crossroad", labyrinth.all_path_from_crossroad((7, 1)))
print("all_path_from_crossroad", labyrinth.all_path_from_crossroad((9, 5)))

print("use ", labyrinth.use_data_from_all_path((7, 1)))
print("use ", labyrinth.use_data_from_all_path((9, 5)))
print()
print(labyrinth.non_crossroads_anymore)
print()
print("----------------------------------------------------------------")
print("GO THROUGH ALL CROSSROADS", labyrinth.go_through())
print(labyrinth.get_any_points_symbol(76, 40))

print("find first", labyrinth.find_first_crossroad())
print("find last", labyrinth.find_last_crossroad())

print()
print("-----------------------")
print("Non crossroads anymore", labyrinth.non_crossroads_anymore)
print(len(labyrinth.non_crossroads_anymore))


print("Use data from non-crossroad anymore", labyrinth.use_data_from_non_crossroads_anymore())
print("remap_non_crossroad_and_all_crossroads", labyrinth.remap_non_crossroad_and_all_crossroads())