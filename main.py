"""
Go to word and replace("■", "#")
590 different coordinates to get to finish
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
        self.file = "path.txt"
        self.labyrinth_in_list = self.open_file()
        # L=Levo | R=Desno | D=Dol | G=Gor (Primer: DDRGLLGDR)
        # L=Left | R=Right | D=Down | U=Up (Primer: DDRULLGDR)
        self.directions = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1) }
        self.final_directions = {(-1, 0) : "L", (1, 0) : "R" , (0, 1): "D", (0, -1) : "U"}

        # crossroads section
        self.all_crossroads_absolute = self.all_crossroads()
        self.removed_crossroads = set()
        self.non_crossroads_anymore = {}
        self.non_crossroads_anymore_2 = {} # when I find other crossroads to be non crossroads 2 because of non crossroads
        self.two_connected_crossroads = set()  # two connected crossroads dead crossroads in between

        self.first_position = self.start()
        self.last_position = self.finish()
        # all crossroads excluding first and last (on the true way)
        self.all_crossroads = self.all_crossroads_absolute # - set(self.find_first_crossroad()) - set(self.find_last_crossroad())
        # probably do not need this anymore
        self.current_branch = []
        self.path = [self.first_position, (2, 2)]
        self.intersections = []

        self.valid_branches = collections.defaultdict(list)
        self.whole_way_from_start_to_end = []
        self.whole_way_directions = []

    def open_file(self):
        with open(self.file, "r", encoding="utf-8") as labyrinth_form_page:
            new_labyrinth = []
            lines = labyrinth_form_page.readlines()
            for line in lines:
                line = line.replace("■", "#")
                # change those two replace with space
                # line = line.replace("☺", "#")
                # line = line.replace("♥", "#")
                line = line.replace("\n", "")
                new_labyrinth.append(line)
            return new_labyrinth

    # adding wall on "dead" crossroads that do not lead anywhere
    # specify crossroad location where you want to put wall
    # rewrite whole labyrinth_in_list
    def replace_dead_crossroads_with_wall(self, crossroad):
        x, y = crossroad
        new_labyrinth = []
        for i, line in enumerate(self.labyrinth_in_list):  # number of line is y
            if i == y:
                # convert string to list and change " " with "#" in particular x and .join back to string
                line = list(line)
                line[x] = "#"
                line = "".join(line)
                new_labyrinth.append(line)
            else:
                new_labyrinth.append(line)
        # update self.labyrinth_in_list that whole project can access to new data
        self.labyrinth_in_list = new_labyrinth
        return new_labyrinth

    # check for every crossroad if it ends up with two dead branches
    # if true place "#" in this crossroad - wall
    def mark_dead_crossroad_as_wall(self, crossroad):
        reachable_crossroads = []
        crossroads = set()
        crossroad, all_path = self.all_path_from_crossroad(crossroad)
        for first_step, path in all_path.items():
            # print(path)
            last_step_in_branch = path[0][-1]  # None if hit the wall, tuple if crossroad
            # in path is direction too (which way you need to turn in crossroad
            if type(last_step_in_branch) == tuple:
                reachable_crossroads.append(last_step_in_branch)
        if len(reachable_crossroads) == 1:  # if just one valid way/branch
            self.replace_dead_crossroads_with_wall(crossroad)
            crossroads.add(crossroad)
            print(crossroad)
        self.all_crossroads = self.all_crossroads - crossroads
        return reachable_crossroads

    # go through all crossroads and all mark_dead_crossroad_as_wall()
    # count how many crossroads become dead this iteration
    def all_crossroads_mark_dead_as_wall(self):
        no_of_dead_crossroad_in_this_iteration = 0
        for crossroad in self.all_crossroads:
            mark_dead = self.mark_dead_crossroad_as_wall(crossroad)
            if len(mark_dead) == 1:
                no_of_dead_crossroad_in_this_iteration += 1
        print(no_of_dead_crossroad_in_this_iteration)
        return no_of_dead_crossroad_in_this_iteration

    # go through as many iterations as needed
    def marking_crossroads_as_dead(self):
        count = 0
        while self.all_crossroads_mark_dead_as_wall() != 0:
            count += self.all_crossroads_mark_dead_as_wall()
        return self.labyrinth_in_list

    # for valid crossroad exclude blind branch
    # save in init which two walid branch you can take from every crossroad
    # call this function when you now which crossroads are alive
    # return set with two values starting point (which is crossroad location and possible next step
    def valid_branches_in_alive_crossroad(self, crossroad):
        _crossroad, path = self.all_path_from_crossroad(crossroad)
        for first_step, branch_and_direction in path.items():
            branch, direction = branch_and_direction
            if branch[-1]:  # if last element in branch is not None - so is not wall than append both branches to dict
                next_step = branch[1:]
                self.valid_branches[crossroad].append(next_step)
        return self.valid_branches

    # collect all valid branches from alive crossroads in dict
    # from crossroad to crossroad
    def all_branches_from_valid_crossroads(self):
        for crossroad in self.all_crossroads:
            self.valid_branches_in_alive_crossroad(crossroad)
        return self.valid_branches

    # first crossroad on map
    # start from smile...
    def way_to_first_crossroad(self, first_step=(1, 1), start=(1, 0)):
        return self.branch_path(first_step, start)[:-1]

    # compose branch by branch to get coordinates for the whole way
    # find first crossroad - optimize this part
    # save coordinates of every step
    def get_coordinates_for_all_way(self):
        self.whole_way_from_start_to_end.extend(self.way_to_first_crossroad())
        crossroad_location = ()
        for i in range(len(self.all_crossroads)):
            crossroad_location = self.whole_way_from_start_to_end[-1]
            last_step = self.whole_way_from_start_to_end[-2]
            for branch in self.valid_branches[crossroad_location]:
                if branch[0] != last_step:
                    self.whole_way_from_start_to_end.extend(branch[:-1])
        self.whole_way_from_start_to_end.extend((79, 40)) # append heart (end of labyrinth)
        return self.whole_way_from_start_to_end

    # get direction to go from one coordinate to another (D, U, L, R)
    def from_coordinates_to_directions(self):
        for first, second in zip(self.whole_way_from_start_to_end, self.whole_way_from_start_to_end[1:]):
            if type(second) == tuple:
                x, y = first
                x1, y1 = second
                direction = self.final_directions[(x1 - x, y1 - y)]
                self.whole_way_directions.append(direction)
        return self.whole_way_directions

    def labyrinth_size_x(self):
        return len(self.labyrinth_in_list[0])

    def labyrinth_size_y(self):
        return len(self.labyrinth_in_list)

    def start(self):
        # add this part on end
        if self.labyrinth_in_list[0][1] == " ":
            return 1, 0

    def finish(self):
        # add this part on end
        if self.labyrinth_in_list[self.labyrinth_size_y() - 1][self.labyrinth_size_x() - 2] == " ":
            return self.labyrinth_size_x() - 2, self.labyrinth_size_y() - 1

    # from (x, y) get if it is " " or #
    def get_any_points_symbol(self, x, y):
        return self.labyrinth_in_list[y][x]



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

    def start_with_smile(self, location):
        return self.get_any_points_symbol(*location) == "☺"

    def ends_with_heart(self, location):
        return self.get_any_points_symbol(*location) == "♥"

    # you can move in three directions from crossroad - return all three directions from crossroad
    # duplicate of self.point_three_possible_step()
    # possible direction where is heart,smile or not wall
    def step_all_directions(self, your_location):
        all_possible_next_steps = set()
        for direction in self.directions:
            if self.is_not_wall(self.next_step(your_location, direction)):
                all_possible_next_steps.add(self.next_step(your_location, direction))
            if self.start_with_smile(self.next_step(your_location, direction)):
                all_possible_next_steps.add(self.next_step(your_location, direction))
            if self.ends_with_heart(self.next_step(your_location, direction)):
                all_possible_next_steps.add(self.next_step(your_location, direction))
        return all_possible_next_steps

    # Function return tuple for detected crossroad, location of next valid state or None for hitting the wall
    def useful_step(self, your_location, crossroad_location):
        next_step = list(self.step_all_directions(your_location))  # all possible steps from current location
        for possible_steps in next_step:
            if possible_steps == crossroad_location:
                next_step.remove(crossroad_location)
        # print(next_step)
        if len(next_step) > 1:
            # print("We reached Crossroad, Crossroad location is: ", your_location)
            return your_location, next_step
        elif len(next_step) == 1:
            return next_step[0]
        else:
            # print("We hit the wall, blind road detected")
            return None

    # return all points
    # if last is None - blind road
    # if last is ☺ - starting position
    # if last is ♥ - ending position
    # if last tuple with info about crossroad - crossroad

    def branch_path(self, your_location, crossroad):
        current_branch_local = [crossroad, your_location]
        # continue if last element is not None and is tuple with two numbers
        while current_branch_local[-1] and type(current_branch_local[-1][0]) == int \
                and not self.start_with_smile(current_branch_local[-1])\
                and not self.ends_with_heart(current_branch_local[-1]):
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
            # print(possible_direction_coordinate)
            branch_path = (self.branch_path(possible_direction_coordinate, crossroad), direction)
            all_path[possible_direction_coordinate] = branch_path
        return crossroad, all_path

    # get all crossroads with two blind branches
    # collect them in non crossroads
    def use_data_from_all_path(self, crossroad):
        reachable_crossroads = []
        crossroad, all_path = self.all_path_from_crossroad(crossroad)
        for first_step, path in all_path.items():
            # in path is direction too (which way you need to turn in crossroad
            if type(path[0][-1]) == tuple:
                reachable_crossroads.append(path[0][-1])
        if len(reachable_crossroads) == 1:
            # print("We find dead crossroad")
            # this part put (17, 39) in non crossroads anymore
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
        print("Non crossroads", self.non_crossroads_anymore)
        print("absolutely all crossroads - removed crossroads", self.all_crossroads_absolute - self.removed_crossroads)
        print("LEN absolutely all crossroads - removed crossroads: ",
              len(self.all_crossroads_absolute - self.removed_crossroads))
        print("Non crossroads", self.non_crossroads_anymore)
        for non_crossroad, two_ways in self.use_data_from_non_crossroads_anymore().items():
            # remove crossroads (non crossroad now) that you cut one branch off in previous function
            # self.all_crossroads_absolute.remove(non_crossroad)

            # add crossroads that has dead branch to other dead crossroad and other branch - dead, to removed_crossroads
            self.removed_crossroads.add(non_crossroad)

            way_1 = two_ways[0]
            way_2 = two_ways[1]

            #  If any of path/branch ends with None print other as non crossroad anymore
            if not way_1[-1]:
                # print(way_2[-1])
                last_element_that_reach_crossroad_1 = way_2[-1]
                reached_crossroad_1 = last_element_that_reach_crossroad_1[0]
                possible_branches_1 = last_element_that_reach_crossroad_1[1]
                self.non_crossroads_anymore_2[reached_crossroad_1] = possible_branches_1

            if not way_2[-1]:
                # print(way_1[-1])
                last_element_that_reach_crossroad_2 = way_1[-1]
                reached_crossroad_2 = last_element_that_reach_crossroad_2[0]
                possible_branches_2 = last_element_that_reach_crossroad_2[1]
                self.non_crossroads_anymore_2[reached_crossroad_2] = possible_branches_2

        print("removed_crossroads: ", self.removed_crossroads)
        print("non_crossroads_anymore: ", self.non_crossroads_anymore)
        print("non_crossroads_anymore_2: ", self.non_crossroads_anymore_2)
        # clear self.non_crossroads_anymore that will be empty
        self.non_crossroads_anymore.clear()
        print("non_crossroads_anymore_after_clear", self.non_crossroads_anymore)
        # run another loop through self.non_crossroads_anymore_2

    # do the same for non corssroad anymore 2
    def use_data_from_non_crossroads_anymore_2(self):
        non_crossroad_data_2 = collections.defaultdict(list)
        # call remap_non_crossroad_and_all_crossroads first to get data non crossroad anymore 2
        for non_crossroad, two_path in self.non_crossroads_anymore_2.items():
            for path in two_path:
                branch = self.branch_path(path, non_crossroad)
                non_crossroad_data_2[non_crossroad].append(branch)
        return non_crossroad_data_2

    def remap_non_crossroad_and_all_crossroads_2(self):
        print("Non crossroads", self.non_crossroads_anymore)
        print("absolutely all crossroads - removed crossroads", self.all_crossroads_absolute - self.removed_crossroads)
        print("LEN absolutely all crossroads - removed crossroads: ",
              len(self.all_crossroads_absolute - self.removed_crossroads))
        for non_crossroad, two_ways in self.use_data_from_non_crossroads_anymore_2().items():
            # remove crossroads (non crossroad now) that you cut one branch off in previous function
            # self.all_crossroads_absolute.remove(non_crossroad)

            # add crossroads that has dead branch to other dead crossroad and other branch - dead, to removed_crossroads
            self.removed_crossroads.add(non_crossroad)

            way_1 = two_ways[0]
            way_2 = two_ways[1]

            #  If any of path/branch ends with None print other as non crossroad anymore
            if not way_1[-1]:
                # print(way_2[-1])
                last_element_that_reach_crossroad_1 = way_2[-1]
                reached_crossroad_1 = last_element_that_reach_crossroad_1[0]
                possible_branches_1 = last_element_that_reach_crossroad_1[1]
                # add data in cleared non_crossroads_anymore ...
                self.non_crossroads_anymore[reached_crossroad_1] = possible_branches_1

            if not way_2[-1]:
                # print(way_1[-1])
                last_element_that_reach_crossroad_2 = way_1[-1]
                reached_crossroad_2 = last_element_that_reach_crossroad_2[0]
                possible_branches_2 = last_element_that_reach_crossroad_2[1]
                # add data in cleared non_crossroads_anymore ...
                self.non_crossroads_anymore[reached_crossroad_2] = possible_branches_2

        print("removed_crossroads: ", self.removed_crossroads)
        print("non_crossroads_anymore: ", self.non_crossroads_anymore)
        print("non_crossroads_anymore_2: ", self.non_crossroads_anymore_2)
        # clear self.non_crossroads_anymore_2 that will be empty and prepared for next iteration
        self.non_crossroads_anymore_2.clear()
        print("non_crossroads_anymore_2_after_clear", self.non_crossroads_anymore_2)
        # run another loop through self.non_crossroads_anymore_2

    # Call non_crossroads_anymore again
    def use_data_from_non_crossroads_anymore_1(self):
        non_crossroad_data_1 = collections.defaultdict(list)
        # call remap_non_crossroad_and_all_crossroads first to get data non crossroad anymore 2
        for non_crossroad, two_path in self.non_crossroads_anymore.items():
            for path in two_path:
                branch = self.branch_path(path, non_crossroad)
                non_crossroad_data_1[non_crossroad].append(branch)
        return non_crossroad_data_1

    # go through both ways in non-crossroads anymore
    # find all crossroads that become non crossroads
    def remap_non_crossroad_and_all_crossroads_1(self):
        print("absolutely all crossroads - removed crossroads", self.all_crossroads_absolute - self.removed_crossroads)
        print("LEN absolutely all crossroads - removed crossroads: ",
              len(self.all_crossroads_absolute - self.removed_crossroads))
        print("Non crossroads", self.non_crossroads_anymore)
        for non_crossroad, two_ways in self.use_data_from_non_crossroads_anymore_1().items():
            # remove crossroads (non crossroad now) that you cut one branch off in previous function
            # self.all_crossroads_absolute.remove(non_crossroad)

            # add crossroads that has dead branch to other dead crossroad and other branch - dead, to removed_crossroads
            self.removed_crossroads.add(non_crossroad)

            way_1 = two_ways[0]
            way_2 = two_ways[1]

            #  If any of path/branch ends with None print other as non crossroad anymore
            if not way_1[-1]:
                # print(way_2[-1])
                last_element_that_reach_crossroad_1 = way_2[-1]
                reached_crossroad_1 = last_element_that_reach_crossroad_1[0]
                possible_branches_1 = last_element_that_reach_crossroad_1[1]
                self.non_crossroads_anymore_2[reached_crossroad_1] = possible_branches_1

            if not way_2[-1]:
                # print(way_1[-1])
                last_element_that_reach_crossroad_2 = way_1[-1]
                reached_crossroad_2 = last_element_that_reach_crossroad_2[0]
                possible_branches_2 = last_element_that_reach_crossroad_2[1]
                self.non_crossroads_anymore_2[reached_crossroad_2] = possible_branches_2

        print("removed_crossroads: ", self.removed_crossroads)
        print("non_crossroads_anymore: ", self.non_crossroads_anymore)
        print("non_crossroads_anymore_2: ", self.non_crossroads_anymore_2)
        # clear self.non_crossroads_anymore that will be empty
        self.non_crossroads_anymore.clear()
        print("non_crossroads_anymore_after_clear", self.non_crossroads_anymore)
        # run another loop through self.non_crossroads_anymore_2



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
        for crossroad in self.all_crossroads:
            # print(crossroad)
            self.use_data_from_all_path(crossroad)
        self.removed_crossroads.remove(self.way_to_first_crossroad())  # first crossroad that lead from start
        self.removed_crossroads.remove(self.find_last_crossroad())  # last crossroad next to finish
        print("Removed crossroads are: ", self.removed_crossroads)
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

    # METOD UNUSED
    # function return next step (coordinate) is there is only one option where to go, if hit the wall return None
    def step_by_step(self, previous_location, crossroad):
        for direction in self.directions:
            next_step = self.next_step(previous_location, direction)
            if self.is_not_wall(next_step) and next_step != crossroad:
                if next_step in self.all_crossroads:   # optimise this part of code it takes 5 seconds to get data
                    # print("We hit another crossroad")
                    return None
                else:
                    return next_step
            else:
                # print("I hit the wall")
                return None

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

    # direction in possible steps that I know which way I took
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

    # not used
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
########################################################################################


##########################################################################################
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
#
# print("All possible crossroads are: ", labyrinth.all_crossroads_absolute)
# print("No of all possible crossroads are: ", len(labyrinth.all_crossroads_absolute))
#
# # print("Two blind streets", labyrinth.crossroads_with_two_blind_alleys())
#
# print(labyrinth.step_by_step((6, 1), (7, 1)))
# print(labyrinth.step_all_directions((9, 1)))
# print("Useful step, next valid step is: ", labyrinth.useful_step((9, 1), (8, 1)))
#
# print("Branch path", labyrinth.branch_path((8, 1), (7, 1)))
# print("--------------------------------------------------------------------------------------")
# print("all_path_from_crossroad", labyrinth.all_path_from_crossroad((7, 1)))
# print("all_path_from_crossroad", labyrinth.all_path_from_crossroad((9, 5)))
#
# print("use ", labyrinth.use_data_from_all_path((7, 1)))
# print("use ", labyrinth.use_data_from_all_path((9, 5)))
# print()
# print(labyrinth.non_crossroads_anymore)
# print()
# print("----------------------------------------------------------------")
# print("GO THROUGH ALL CROSSROADS", labyrinth.go_through())
# print(labyrinth.get_any_points_symbol(76, 40))
#
# print("find first", labyrinth.find_first_crossroad())
# print("find last", labyrinth.find_last_crossroad())
#
# print()
# print("-----------------------")
# # DO NOT WORK - bug
# # (17, 39) append to removed crossroad
# print("Non crossroads anymore", labyrinth.non_crossroads_anymore)
# print(len(labyrinth.non_crossroads_anymore))
#
#
# print("Use data from non-crossroad anymore", labyrinth.use_data_from_non_crossroads_anymore())
# print("remap_non_crossroad_and_all_crossroads", labyrinth.remap_non_crossroad_and_all_crossroads())
#
#
# print("use_data_from_non_crossroads_anymore_2", labyrinth.use_data_from_non_crossroads_anymore_2())
# print("remap_non_crossroad_and_all_crossroads_2", labyrinth.remap_non_crossroad_and_all_crossroads_2())
#
# print("use_data_from_non_crossroads_anymore_1, similar than first time", labyrinth.use_data_from_non_crossroads_anymore_1())
# print(" remap_non_crossroad_and_all_crossroads, call second time", labyrinth.remap_non_crossroad_and_all_crossroads_1())
#
# print("use_data_from_non_crossroads_anymore_2", labyrinth.use_data_from_non_crossroads_anymore_2())
# print("remap_non_crossroad_and_all_crossroads_2", labyrinth.remap_non_crossroad_and_all_crossroads_2())
#
# print("use_data_from_non_crossroads_anymore_1, similar than first time", labyrinth.use_data_from_non_crossroads_anymore_1())
# print(" remap_non_crossroad_and_all_crossroads, call second time", labyrinth.remap_non_crossroad_and_all_crossroads_1())
#
# print("use_data_from_non_crossroads_anymore_2", labyrinth.use_data_from_non_crossroads_anymore_2())
# print("remap_non_crossroad_and_all_crossroads_2", labyrinth.remap_non_crossroad_and_all_crossroads_2())
#
# print("use_data_from_non_crossroads_anymore_1, similar than first time", labyrinth.use_data_from_non_crossroads_anymore_1())
# print(" remap_non_crossroad_and_all_crossroads, call second time", labyrinth.remap_non_crossroad_and_all_crossroads_1())
#
#
# # added later manually
# print("-----------------------------------------------------------------------------------------------------")
# # it only takes two directions
# print("use_data_from_all_path", labyrinth.use_data_from_all_path((17, 39)))
# print("LEN use_data_from_all_path", len(labyrinth.use_data_from_all_path((17, 39))))

########################################################################################################################

print(labyrinth.open_file()[40][80])

# print("replace_dead_crossroads_with_wall", labyrinth.replace_dead_crossroads_with_wall((1, 1)))
print("labyrinth_in_list", labyrinth.labyrinth_in_list)

# print("all_path_from_crossroad - ", labyrinth.all_path_from_crossroad((7, 39)))
# print("(all_path_from_crossroad) - ", (labyrinth.all_path_from_crossroad((7, 39)))[1])
# print("len(all_path_from_crossroad) - ", len(labyrinth.all_path_from_crossroad((7, 39))[1]))
print("crossroad", labyrinth.crossroad((7, 39)))

# print("mark_dead_crossroad_as_wall", labyrinth.mark_dead_crossroad_as_wall((7, 39)))
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)
#
# print("mark_dead_crossroad_as_wall second iteration", labyrinth.mark_dead_crossroad_as_wall((3, 39)))
# print("labyrinth_in_list second iteration", labyrinth.labyrinth_in_list)

# print(labyrinth.branch_path((6, 9), (5, 9)))


#
print("---------------------------------------------------------------------------------------------------------------")

# print("all_crossroads_mark_dead_as_wall", labyrinth.all_crossroads_mark_dead_as_wall())
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)
#
# print("all_crossroads_mark_dead_as_wall", labyrinth.all_crossroads_mark_dead_as_wall())
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)
#
# print("all_crossroads_mark_dead_as_wall", labyrinth.all_crossroads_mark_dead_as_wall())
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)
#
# print("all_crossroads_mark_dead_as_wall", labyrinth.all_crossroads_mark_dead_as_wall())
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)
#
# print("all_crossroads_mark_dead_as_wall", labyrinth.all_crossroads_mark_dead_as_wall())
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)
#
# print("all_crossroads_mark_dead_as_wall", labyrinth.all_crossroads_mark_dead_as_wall())
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)
#
# print("all_crossroads_mark_dead_as_wall", labyrinth.all_crossroads_mark_dead_as_wall())
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)
#
# print("all_crossroads_mark_dead_as_wall", labyrinth.all_crossroads_mark_dead_as_wall())
# print("labyrinth_in_list", labyrinth.labyrinth_in_list)

# print("---------------------------------------------------------------------------------------------------------------")
# print(labyrinth.labyrinth_in_list[0][1])
# print("useful_step", labyrinth.useful_step((1, 0), (1, 1)))
# print("next_step(your_location, direction)", labyrinth.next_step((1, 1), "U"))
# print("get_any_points_symbol", labyrinth.get_any_points_symbol(1, 0))
# print("start_with_smile", labyrinth.start_with_smile((1, 0)))
# print("step_all_directions", labyrinth.step_all_directions((1, 1)))
# print("useful_step", labyrinth.useful_step((1, 1), (2, 1)))
# print("branch_path", labyrinth.branch_path((6, 9), (5, 9)))
# print("useful_step", labyrinth.useful_step((6, 9), (5, 9)))
# print("all_path_from_crossroad", labyrinth.all_path_from_crossroad((5, 9)))
#
# print("ends_with_heart", labyrinth.ends_with_heart((79, 40)))
# print("branch_path", labyrinth.branch_path((76, 39), (75, 39)))
# print("all_path_from_crossroad", labyrinth.all_path_from_crossroad((75, 39)))
# print("---------------------------------------------------------------------------------------------------------------")
print(len(labyrinth.all_crossroads_absolute))

print("marking_crossroads_as_dead", labyrinth.marking_crossroads_as_dead())
print("all_crossroads", labyrinth.all_crossroads)
print("LEN all_crossroads", len(labyrinth.all_crossroads))

print("all_path_from_crossroad", labyrinth.all_path_from_crossroad((5, 9)))
print("all_path_from_crossroad", labyrinth.all_path_from_crossroad((17, 39)))
print("use_data_from_all_path", labyrinth.use_data_from_all_path((5, 9)))
print("use_data_from_all_path", labyrinth.use_data_from_all_path((17, 39)))


print("all_branches_from_valid_crossroads", labyrinth.all_branches_from_valid_crossroads())
all_branches_from_valid_crossroads = {(17, 39): [[(17, 38), (17, 37), (16, 37), (15, 37), (14, 37), (13, 37), (13, 36), (13, 35), (13, 34), (13, 33), (12, 33), (11, 33), (11, 32), (11, 31), (11, 30), (11, 29), (12, 29), (13, 29), (13, 30), (13, 31), (14, 31), (15, 31), (15, 32), (15, 33), (16, 33), (17, 33), (18, 33), (19, 33), (20, 33), (21, 33), (22, 33), (23, 33), (23, 32), (23, 31), (23, 30), (23, 29), (24, 29), (25, 29), (25, 28), (25, 27), (24, 27), (23, 27), (23, 26), (23, 25), (23, 24), (23, 23), (22, 23), (21, 23), (21, 24), (21, 25), (20, 25), (19, 25), (19, 24), (19, 23), (18, 23), (17, 23), (17, 22), (17, 21), (18, 21), (19, 21), (19, 20), (19, 19), (19, 18), (19, 17), (20, 17), (21, 17), (21, 16), (21, 15), (20, 15), (19, 15), (19, 14), (19, 13), (19, 12), (19, 11), (18, 11), (17, 11), (16, 11), (15, 11), (14, 11), (13, 11), (12, 11), (11, 11), (11, 12), (11, 13), (10, 13), (9, 13), (9, 12), (9, 11), (8, 11), (7, 11), (7, 12), (7, 13), (6, 13), (5, 13), (5, 12), (5, 11), (5, 10), (5, 9), ((5, 9), [(6, 9), (5, 8)])], [(18, 39), (19, 39), (20, 39), (21, 39), (21, 38), (21, 37), (22, 37), (23, 37), (23, 38), (23, 39), (24, 39), (25, 39), (26, 39), (27, 39), (27, 38), (27, 37), (28, 37), (29, 37), (30, 37), (31, 37), (31, 36), (31, 35), (32, 35), (33, 35), (33, 34), (33, 33), (32, 33), (31, 33), (30, 33), (29, 33), (29, 34), (29, 35), (28, 35), (27, 35), ((27, 35), [(26, 35), (27, 34)])], [(17, 38), (17, 37), (16, 37), (15, 37), (14, 37), (13, 37), (13, 36), (13, 35), (13, 34), (13, 33), (12, 33), (11, 33), (11, 32), (11, 31), (11, 30), (11, 29), (12, 29), (13, 29), (13, 30), (13, 31), (14, 31), (15, 31), (15, 32), (15, 33), (16, 33), (17, 33), (18, 33), (19, 33), (20, 33), (21, 33), (22, 33), (23, 33), (23, 32), (23, 31), (23, 30), (23, 29), (24, 29), (25, 29), (25, 28), (25, 27), (24, 27), (23, 27), (23, 26), (23, 25), (23, 24), (23, 23), (22, 23), (21, 23), (21, 24), (21, 25), (20, 25), (19, 25), (19, 24), (19, 23), (18, 23), (17, 23), (17, 22), (17, 21), (18, 21), (19, 21), (19, 20), (19, 19), (19, 18), (19, 17), (20, 17), (21, 17), (21, 16), (21, 15), (20, 15), (19, 15), (19, 14), (19, 13), (19, 12), (19, 11), (18, 11), (17, 11), (16, 11), (15, 11), (14, 11), (13, 11), (12, 11), (11, 11), (11, 12), (11, 13), (10, 13), (9, 13), (9, 12), (9, 11), (8, 11), (7, 11), (7, 12), (7, 13), (6, 13), (5, 13), (5, 12), (5, 11), (5, 10), (5, 9), ((5, 9), [(6, 9), (5, 8)])], [(18, 39), (19, 39), (20, 39), (21, 39), (21, 38), (21, 37), (22, 37), (23, 37), (23, 38), (23, 39), (24, 39), (25, 39), (26, 39), (27, 39), (27, 38), (27, 37), (28, 37), (29, 37), (30, 37), (31, 37), (31, 36), (31, 35), (32, 35), (33, 35), (33, 34), (33, 33), (32, 33), (31, 33), (30, 33), (29, 33), (29, 34), (29, 35), (28, 35), (27, 35), ((27, 35), [(26, 35), (27, 34)])]], (47, 1): [[(47, 2), (47, 3), (48, 3), (49, 3), (50, 3), (51, 3), (52, 3), (53, 3), (53, 4), (53, 5), (52, 5), (51, 5), (50, 5), (49, 5), (49, 6), (49, 7), (48, 7), (47, 7), (47, 8), (47, 9), (47, 10), (47, 11), (47, 12), (47, 13), (46, 13), (45, 13), (44, 13), (43, 13), (43, 14), (43, 15), (42, 15), (41, 15), (41, 16), (41, 17), (41, 18), (41, 19), (40, 19), (39, 19), (39, 20), (39, 21), (39, 22), (39, 23), (39, 24), (39, 25), (40, 25), (41, 25), (41, 26), (41, 27), (40, 27), (39, 27), (38, 27), (37, 27), (37, 28), (37, 29), (37, 30), (37, 31), (36, 31), (35, 31), (34, 31), (33, 31), ((33, 31), [(32, 31), (33, 30)])], [(48, 1), (49, 1), (50, 1), (51, 1), (52, 1), (53, 1), (54, 1), (55, 1), (56, 1), (57, 1), (58, 1), (59, 1), (60, 1), (61, 1), (61, 2), (61, 3), (60, 3), (59, 3), (59, 4), (59, 5), (60, 5), (61, 5), (61, 6), (61, 7), (61, 8), (61, 9), (60, 9), (59, 9), (59, 8), (59, 7), (58, 7), (57, 7), (57, 6), (57, 5), (57, 4), (57, 3), (56, 3), (55, 3), (55, 4), (55, 5), (55, 6), (55, 7), (55, 8), (55, 9), (56, 9), (57, 9), (57, 10), (57, 11), (57, 12), (57, 13), (57, 14), (57, 15), (57, 16), (57, 17), (56, 17), (55, 17), (54, 17), (53, 17), (53, 18), (53, 19), (54, 19), (55, 19), (55, 20), (55, 21), (54, 21), (53, 21), (52, 21), (51, 21), (50, 21), (49, 21), (49, 22), (49, 23), (50, 23), (51, 23), (52, 23), (53, 23), (53, 24), (53, 25), (52, 25), (51, 25), (51, 26), (51, 27), (50, 27), (49, 27), (49, 26), (49, 25), (48, 25), (47, 25), (47, 26), (47, 27), (47, 28), (47, 29), (48, 29), (49, 29), (49, 30), (49, 31), (48, 31), (47, 31), (47, 32), (47, 33), (48, 33), (49, 33), (50, 33), (51, 33), (51, 34), (51, 35), (50, 35), (49, 35), (49, 36), (49, 37), (48, 37), (47, 37), (46, 37), (45, 37), (45, 38), (45, 39), ((45, 39), [(46, 39), (44, 39)])]], (75, 39): [[(74, 39), (73, 39), (72, 39), (71, 39), (70, 39), (69, 39), ((69, 39), [(68, 39), (69, 38)])], [(76, 39), (77, 39), (78, 39), (79, 39), (79, 40)]], (67, 13): [[(68, 13), (69, 13), (69, 12), (69, 11), (69, 10), (69, 9), (69, 8), (69, 7), (70, 7), (71, 7), (72, 7), (73, 7), (73, 6), (73, 5), (72, 5), (71, 5), (70, 5), (69, 5), (69, 4), (69, 3), (69, 2), (69, 1), (68, 1), (67, 1), ((67, 1), [(66, 1), (67, 2)])], [(67, 14), (67, 15), (67, 16), (67, 17), (68, 17), (69, 17), (69, 18), (69, 19), (70, 19), (71, 19), (71, 18), (71, 17), (72, 17), (73, 17), (74, 17), (75, 17), (76, 17), (77, 17), (77, 18), (77, 19), (77, 20), (77, 21), (78, 21), (79, 21), ((79, 21), [(79, 20), (79, 22)])]], (69, 39): [[(69, 38), (69, 37), (70, 37), (71, 37), (72, 37), (73, 37), (73, 36), (73, 35), (74, 35), (75, 35), (76, 35), (77, 35), (77, 36), (77, 37), (78, 37), (79, 37), (79, 36), (79, 35), (79, 34), (79, 33), (78, 33), (77, 33), (76, 33), (75, 33), (75, 32), (75, 31), (76, 31), (77, 31), (78, 31), (79, 31), (79, 30), (79, 29), (78, 29), (77, 29), (77, 28), (77, 27), (78, 27), (79, 27), (79, 26), (79, 25), (79, 24), (79, 23), (79, 22), (79, 21), ((79, 21), [(78, 21), (79, 20)])], [(70, 39), (71, 39), (72, 39), (73, 39), (74, 39), (75, 39), ((75, 39), [(75, 38), (76, 39)])]], (45, 39): [[(45, 38), (45, 37), (46, 37), (47, 37), (48, 37), (49, 37), (49, 36), (49, 35), (50, 35), (51, 35), (51, 34), (51, 33), (50, 33), (49, 33), (48, 33), (47, 33), (47, 32), (47, 31), (48, 31), (49, 31), (49, 30), (49, 29), (48, 29), (47, 29), (47, 28), (47, 27), (47, 26), (47, 25), (48, 25), (49, 25), (49, 26), (49, 27), (50, 27), (51, 27), (51, 26), (51, 25), (52, 25), (53, 25), (53, 24), (53, 23), (52, 23), (51, 23), (50, 23), (49, 23), (49, 22), (49, 21), (50, 21), (51, 21), (52, 21), (53, 21), (54, 21), (55, 21), (55, 20), (55, 19), (54, 19), (53, 19), (53, 18), (53, 17), (54, 17), (55, 17), (56, 17), (57, 17), (57, 16), (57, 15), (57, 14), (57, 13), (57, 12), (57, 11), (57, 10), (57, 9), (56, 9), (55, 9), (55, 8), (55, 7), (55, 6), (55, 5), (55, 4), (55, 3), (56, 3), (57, 3), (57, 4), (57, 5), (57, 6), (57, 7), (58, 7), (59, 7), (59, 8), (59, 9), (60, 9), (61, 9), (61, 8), (61, 7), (61, 6), (61, 5), (60, 5), (59, 5), (59, 4), (59, 3), (60, 3), (61, 3), (61, 2), (61, 1), (60, 1), (59, 1), (58, 1), (57, 1), (56, 1), (55, 1), (54, 1), (53, 1), (52, 1), (51, 1), (50, 1), (49, 1), (48, 1), (47, 1), ((47, 1), [(47, 2), (46, 1)])], [(46, 39), (47, 39), (48, 39), (49, 39), (50, 39), (51, 39), (52, 39), (53, 39), (53, 38), (53, 37), ((53, 37), [(54, 37), (52, 37)])]], (59, 15): [[(59, 14), (59, 13), (60, 13), (61, 13), (61, 12), (61, 11), ((61, 11), [(62, 11), (60, 11)])], [(60, 15), (61, 15), (62, 15), (63, 15), (63, 14), (63, 13), (64, 13), (65, 13), (65, 14), (65, 15), (65, 16), (65, 17), (65, 18), (65, 19), (66, 19), (67, 19), (67, 20), (67, 21), (68, 21), (69, 21), (69, 22), (69, 23), (68, 23), (67, 23), (66, 23), (65, 23), (65, 22), (65, 21), (64, 21), (63, 21), (63, 20), (63, 19), (62, 19), (61, 19), (61, 20), (61, 21), (61, 22), (61, 23), (61, 24), (61, 25), (60, 25), (59, 25), (58, 25), (57, 25), (56, 25), (55, 25), (55, 26), (55, 27), (54, 27), (53, 27), (53, 28), (53, 29), ((53, 29), [(52, 29), (53, 30)])]], (53, 29): [[(53, 28), (53, 27), (54, 27), (55, 27), (55, 26), (55, 25), (56, 25), (57, 25), (58, 25), (59, 25), (60, 25), (61, 25), (61, 24), (61, 23), (61, 22), (61, 21), (61, 20), (61, 19), (62, 19), (63, 19), (63, 20), (63, 21), (64, 21), (65, 21), (65, 22), (65, 23), (66, 23), (67, 23), (68, 23), (69, 23), (69, 22), (69, 21), (68, 21), (67, 21), (67, 20), (67, 19), (66, 19), (65, 19), (65, 18), (65, 17), (65, 16), (65, 15), (65, 14), (65, 13), (64, 13), (63, 13), (63, 14), (63, 15), (62, 15), (61, 15), (60, 15), (59, 15), ((59, 15), [(59, 14), (59, 16)])], [(53, 30), (53, 31), (53, 32), (53, 33), (53, 34), (53, 35), (54, 35), (55, 35), (55, 36), (55, 37), (54, 37), (53, 37), ((53, 37), [(53, 38), (52, 37)])]], (33, 31): [[(34, 31), (35, 31), (36, 31), (37, 31), (37, 30), (37, 29), (37, 28), (37, 27), (38, 27), (39, 27), (40, 27), (41, 27), (41, 26), (41, 25), (40, 25), (39, 25), (39, 24), (39, 23), (39, 22), (39, 21), (39, 20), (39, 19), (40, 19), (41, 19), (41, 18), (41, 17), (41, 16), (41, 15), (42, 15), (43, 15), (43, 14), (43, 13), (44, 13), (45, 13), (46, 13), (47, 13), (47, 12), (47, 11), (47, 10), (47, 9), (47, 8), (47, 7), (48, 7), (49, 7), (49, 6), (49, 5), (50, 5), (51, 5), (52, 5), (53, 5), (53, 4), (53, 3), (52, 3), (51, 3), (50, 3), (49, 3), (48, 3), (47, 3), (47, 2), (47, 1), ((47, 1), [(48, 1), (46, 1)])], [(33, 30), (33, 29), (32, 29), (31, 29), (30, 29), (29, 29), (29, 28), (29, 27), (28, 27), (27, 27), (27, 28), (27, 29), (27, 30), (27, 31), ((27, 31), [(27, 32), (26, 31)])]], (27, 31): [[(27, 32), (27, 33), (27, 34), (27, 35), ((27, 35), [(28, 35), (26, 35)])], [(27, 30), (27, 29), (27, 28), (27, 27), (28, 27), (29, 27), (29, 28), (29, 29), (30, 29), (31, 29), (32, 29), (33, 29), (33, 30), (33, 31), ((33, 31), [(32, 31), (34, 31)])]], (27, 35): [[(28, 35), (29, 35), (29, 34), (29, 33), (30, 33), (31, 33), (32, 33), (33, 33), (33, 34), (33, 35), (32, 35), (31, 35), (31, 36), (31, 37), (30, 37), (29, 37), (28, 37), (27, 37), (27, 38), (27, 39), (26, 39), (25, 39), (24, 39), (23, 39), (23, 38), (23, 37), (22, 37), (21, 37), (21, 38), (21, 39), (20, 39), (19, 39), (18, 39), (17, 39), ((17, 39), [(16, 39), (17, 38)])], [(27, 34), (27, 33), (27, 32), (27, 31), ((27, 31), [(27, 30), (26, 31)])]], (5, 9): [[(6, 9), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (6, 5), (5, 5), (5, 4), (5, 3), (4, 3), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 0)], [(5, 10), (5, 11), (5, 12), (5, 13), (6, 13), (7, 13), (7, 12), (7, 11), (8, 11), (9, 11), (9, 12), (9, 13), (10, 13), (11, 13), (11, 12), (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11), (19, 12), (19, 13), (19, 14), (19, 15), (20, 15), (21, 15), (21, 16), (21, 17), (20, 17), (19, 17), (19, 18), (19, 19), (19, 20), (19, 21), (18, 21), (17, 21), (17, 22), (17, 23), (18, 23), (19, 23), (19, 24), (19, 25), (20, 25), (21, 25), (21, 24), (21, 23), (22, 23), (23, 23), (23, 24), (23, 25), (23, 26), (23, 27), (24, 27), (25, 27), (25, 28), (25, 29), (24, 29), (23, 29), (23, 30), (23, 31), (23, 32), (23, 33), (22, 33), (21, 33), (20, 33), (19, 33), (18, 33), (17, 33), (16, 33), (15, 33), (15, 32), (15, 31), (14, 31), (13, 31), (13, 30), (13, 29), (12, 29), (11, 29), (11, 30), (11, 31), (11, 32), (11, 33), (12, 33), (13, 33), (13, 34), (13, 35), (13, 36), (13, 37), (14, 37), (15, 37), (16, 37), (17, 37), (17, 38), (17, 39), ((17, 39), [(18, 39), (16, 39)])]], (61, 11): [[(62, 11), (63, 11), (64, 11), (65, 11), (65, 10), (65, 9), (64, 9), (63, 9), (63, 8), (63, 7), (63, 6), (63, 5), (63, 4), (63, 3), (64, 3), (65, 3), (65, 4), (65, 5), (65, 6), (65, 7), (66, 7), (67, 7), (67, 6), (67, 5), (67, 4), (67, 3), (67, 2), (67, 1), ((67, 1), [(68, 1), (66, 1)])], [(61, 12), (61, 13), (60, 13), (59, 13), (59, 14), (59, 15), ((59, 15), [(60, 15), (59, 16)])]], (79, 21): [[(78, 21), (77, 21), (77, 20), (77, 19), (77, 18), (77, 17), (76, 17), (75, 17), (74, 17), (73, 17), (72, 17), (71, 17), (71, 18), (71, 19), (70, 19), (69, 19), (69, 18), (69, 17), (68, 17), (67, 17), (67, 16), (67, 15), (67, 14), (67, 13), ((67, 13), [(68, 13), (67, 12)])], [(79, 22), (79, 23), (79, 24), (79, 25), (79, 26), (79, 27), (78, 27), (77, 27), (77, 28), (77, 29), (78, 29), (79, 29), (79, 30), (79, 31), (78, 31), (77, 31), (76, 31), (75, 31), (75, 32), (75, 33), (76, 33), (77, 33), (78, 33), (79, 33), (79, 34), (79, 35), (79, 36), (79, 37), (78, 37), (77, 37), (77, 36), (77, 35), (76, 35), (75, 35), (74, 35), (73, 35), (73, 36), (73, 37), (72, 37), (71, 37), (70, 37), (69, 37), (69, 38), (69, 39), ((69, 39), [(70, 39), (68, 39)])]], (67, 1): [[(67, 2), (67, 3), (67, 4), (67, 5), (67, 6), (67, 7), (66, 7), (65, 7), (65, 6), (65, 5), (65, 4), (65, 3), (64, 3), (63, 3), (63, 4), (63, 5), (63, 6), (63, 7), (63, 8), (63, 9), (64, 9), (65, 9), (65, 10), (65, 11), (64, 11), (63, 11), (62, 11), (61, 11), ((61, 11), [(61, 12), (60, 11)])], [(68, 1), (69, 1), (69, 2), (69, 3), (69, 4), (69, 5), (70, 5), (71, 5), (72, 5), (73, 5), (73, 6), (73, 7), (72, 7), (71, 7), (70, 7), (69, 7), (69, 8), (69, 9), (69, 10), (69, 11), (69, 12), (69, 13), (68, 13), (67, 13), ((67, 13), [(67, 14), (67, 12)])]], (53, 37): [[(54, 37), (55, 37), (55, 36), (55, 35), (54, 35), (53, 35), (53, 34), (53, 33), (53, 32), (53, 31), (53, 30), (53, 29), ((53, 29), [(52, 29), (53, 28)])], [(53, 38), (53, 39), (52, 39), (51, 39), (50, 39), (49, 39), (48, 39), (47, 39), (46, 39), (45, 39), ((45, 39), [(45, 38), (44, 39)])]]}
for crossroad, branches in all_branches_from_valid_crossroads.items():
    print((crossroad, branches))


print("get_coordinates_for_all_way", labyrinth.get_coordinates_for_all_way())
print("find_first_crossroad", labyrinth.way_to_first_crossroad())
print("whole_way_from_start_to_end", labyrinth.whole_way_from_start_to_end)

print("from_coordinates_to_directions", labyrinth.from_coordinates_to_directions())

