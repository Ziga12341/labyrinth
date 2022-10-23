"""
Past your labyrinth on path.txt
590 different coordinates to get to finish (appended labyrinth)
"""
import collections


class Labyrinth:
    def __init__(self):
        self.file = "path.txt"
        self.labyrinth_in_list = self.open_file()
        # L=Levo | R=Desno | D=Dol | G=Gor (Primer: DDRGLLGDR)
        # L=Left | R=Right | D=Down | U=Up (Primer: DDRULLGDR)
        self.directions = {"L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1) }
        self.final_directions = {(-1, 0): "L", (1, 0): "R", (0, 1): "D", (0, -1): "U"}

        # all crossroads excluding first and last (on the true way)
        self.all_crossroads = self.all_crossroads()

        self.valid_branches = collections.defaultdict(list)
        self.whole_way_from_start_to_end = []
        self.whole_way_directions = []

    # Open file path.txt and replace symbol that you get " " for free space and "#" for wall
    def open_file(self):
        with open(self.file, "r", encoding="utf-8") as labyrinth_form_page:
            new_labyrinth = []
            lines = labyrinth_form_page.readlines()
            for line in lines:
                line = line.replace("■", "#")
                line = line.replace("\n", "")
                new_labyrinth.append(line)
            return new_labyrinth

    # size of labyrinth
    def labyrinth_size_x(self):
        return len(self.labyrinth_in_list[0])

    def labyrinth_size_y(self):
        return len(self.labyrinth_in_list)

    # from (x, y) get if it is " " or #
    def get_any_points_symbol(self, x, y):
        return self.labyrinth_in_list[y][x]

    # loop through labyrinth and find coordinates of "☺"
    # function return first symbol with specified symbol if in .txt
    def start(self):
        for x in range(self.labyrinth_size_x()):
            for y in range(self.labyrinth_size_y()):
                if self.get_any_points_symbol(x, y) == "☺":
                    return x, y

    # loop through labyrinth and find coordinates of "♥" - which represent finish
    # function return first symbol with specified symbol if in .txt
    def finish(self):
        for x in range(self.labyrinth_size_x()):
            for y in range(self.labyrinth_size_y()):
                if self.get_any_points_symbol(x, y) == "♥":
                    return x, y

    # free directions
    # need to specif previous stem (x, y)
    # direction need to be string "L" = left,"G" = up ,"D" = down , "R" = right
    def next_step(self, previous_step, direction):
        x0, y0 = previous_step
        x1, y1 = self.directions[direction]
        return x0 + x1, y0 + y1

    # return True if free space where you can move around labyrinth " " wall
    def is_not_wall(self, location):
        return self.get_any_points_symbol(*location) == " "

    def start_with_smile(self, location):
        return self.get_any_points_symbol(*location) == "☺"

    def ends_with_heart(self, location):
        return self.get_any_points_symbol(*location) == "♥"

    # you can move in three directions from crossroad - return all three directions from crossroad
    # duplicate of self.point_three_possible_step()
    # possible direction where is heart, smile or not wall
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

    # return all points - specify whole branch with coordinates of specific step
    # if last is None - blind road
    # if last is ☺ - starting position
    # if last is ♥ - ending position
    # if last tuple with info about crossroad - crossroad
    def branch_path(self, your_location, crossroad):
        current_branch_local = [crossroad, your_location]
        # continue if last element is not None and is tuple with two numbers
        while current_branch_local[-1] and type(current_branch_local[-1][0]) == int \
                and not self.start_with_smile(current_branch_local[-1]) \
                and not self.ends_with_heart(current_branch_local[-1]):
            # print(current_branch_local)
            self.useful_step(current_branch_local[-1], current_branch_local[-2])
            current_branch_local.append(self.useful_step(current_branch_local[-1], current_branch_local[-2]))
        return current_branch_local

    # first crossroad on map
    # labyrinth always starts with smile...
    # return whole first branch from start to first crossroad
    def way_to_first_crossroad(self):
        # next possible step from starting position - way where is not wall
        next_step = list(self.step_all_directions(self.start()))[0]
        return self.branch_path(next_step, self.start())[:-1]

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

    # this is the most important method in class
    # adding wall on "dead" crossroads that do not lead anywhere - teo blind roads (branches)
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

    # direction in possible steps that I know which way may I took - no wall
    def point_three_possible_step(self, point):
        three_ways = set()
        for direction in self.directions:
            if self.is_not_wall(self.next_step(point, direction)):
                three_ways.add((self.next_step(point, direction), direction))
        return three_ways

    # three options one/two/three road(s) lead to crossroad
    # collect dict with all three options
    def all_path_from_crossroad(self, crossroad):
        all_path = collections.defaultdict(tuple)
        possible_directions = set(self.point_three_possible_step(crossroad))
        for possible_direction_coordinate, direction in possible_directions:
            # print(possible_direction_coordinate)
            branch_path = self.branch_path(possible_direction_coordinate, crossroad), direction
            all_path[possible_direction_coordinate] = branch_path
        return crossroad, all_path

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
        self.all_crossroads = self.all_crossroads - crossroads
        return reachable_crossroads

    # go through all crossroads and call mark_dead_crossroad_as_wall()
    # count how many crossroads become dead this iteration
    def all_crossroads_mark_dead_as_wall(self):
        no_of_dead_crossroad_in_this_iteration = 0
        for crossroad in self.all_crossroads:
            mark_dead = self.mark_dead_crossroad_as_wall(crossroad)
            if len(mark_dead) == 1:
                no_of_dead_crossroad_in_this_iteration += 1
        return no_of_dead_crossroad_in_this_iteration

    # go through as many iterations as needed
    def marking_crossroads_as_dead(self):
        count = 0
        while self.all_crossroads_mark_dead_as_wall() != 0:
            count += self.all_crossroads_mark_dead_as_wall()
        return self.labyrinth_in_list

    # for valid crossroad exclude blind branch
    # save in init which two valid branches you can take from every crossroad
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

    # collect all valid branches from alive crossroads in dict valid_branches
    # from crossroad to crossroad
    def all_branches_from_valid_crossroads(self):
        for crossroad in self.all_crossroads:
            self.valid_branches_in_alive_crossroad(crossroad)
        return self.valid_branches

    # compose branch by branch to get coordinates for the whole way
    # start with first crossroad that branch is already specified
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
        self.whole_way_from_start_to_end.append(tuple((79, 40)))  # append heart (end of labyrinth)
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


if __name__ == "__main__":
    labyrinth = Labyrinth()
    print("marking_crossroads_as_dead", labyrinth.marking_crossroads_as_dead())
    print("all_branches_from_valid_crossroads", labyrinth.all_branches_from_valid_crossroads())
    print("get_coordinates_for_all_way", labyrinth.get_coordinates_for_all_way())
    print("from_coordinates_to_directions", labyrinth.from_coordinates_to_directions())

