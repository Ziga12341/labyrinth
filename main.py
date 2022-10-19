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
        self.file = "path.txt"
        self.labyrinth_in_list = self.open_file()
        # L=Levo | R=Desno | D=Dol | G=Gor (Primer: DDRGLLGDR)
        # L=Left | R=Right | D=Down | U=Up (Primer: DDRULLGDR)
        self.directions = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1) }

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
        print((no_of_dead_crossroad_in_this_iteration))
        return no_of_dead_crossroad_in_this_iteration

    # go through as many iterations as needed
    def marking_crossroads_as_dead(self):
        count = 0
        while self.all_crossroads_mark_dead_as_wall() != 0:
            print(self.labyrinth_in_list)
            count += self.all_crossroads_mark_dead_as_wall()
        return count

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
        self.removed_crossroads.remove(self.find_first_crossroad())  # first crossroad that lead from start
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